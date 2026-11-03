from calendar import monthrange
from datetime import date
from decimal import Decimal

from fastapi import Depends, FastAPI, HTTPException, Query, status
from sqlalchemy import extract, func
from sqlalchemy.orm import Session

from . import models, schemas
from .database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Expense Tracker API",
    description="A beginner-friendly REST API to create, view, update and delete expenses.",
    version="1.0.0",
)


@app.get("/", tags=["General"])
def home():
    return {"message": "Welcome to the Expense Tracker API", "docs": "/docs"}


@app.get("/health", tags=["General"])
def health_check():
    return {"status": "healthy"}


@app.post(
    "/expenses",
    response_model=schemas.ExpenseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Expenses"],
)
def create_expense(payload: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    expense = models.Expense(**payload.model_dump())
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense


@app.get("/expenses", response_model=list[schemas.ExpenseResponse], tags=["Expenses"])
def list_expenses(
    category: str | None = None,
    start_date: date | None = None,
    end_date: date | None = None,
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
):
    query = db.query(models.Expense)

    if category:
        query = query.filter(models.Expense.category.ilike(f"%{category}%"))
    if start_date:
        query = query.filter(models.Expense.spent_on >= start_date)
    if end_date:
        query = query.filter(models.Expense.spent_on <= end_date)
    if start_date and end_date and start_date > end_date:
        raise HTTPException(status_code=400, detail="start_date cannot be after end_date")

    return query.order_by(models.Expense.spent_on.desc(), models.Expense.id.desc()).offset(offset).limit(limit).all()


@app.get("/expenses/{expense_id}", response_model=schemas.ExpenseResponse, tags=["Expenses"])
def get_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense


@app.patch("/expenses/{expense_id}", response_model=schemas.ExpenseResponse, tags=["Expenses"])
def update_expense(
    expense_id: int,
    payload: schemas.ExpenseUpdate,
    db: Session = Depends(get_db),
):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")

    updates = payload.model_dump(exclude_unset=True)
    for field, value in updates.items():
        setattr(expense, field, value)

    db.commit()
    db.refresh(expense)
    return expense


@app.delete("/expenses/{expense_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Expenses"])
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")

    db.delete(expense)
    db.commit()
    return None


@app.get("/summary/{year}/{month}", response_model=schemas.ExpenseSummary, tags=["Summary"])
def monthly_summary(year: int, month: int, db: Session = Depends(get_db)):
    if month < 1 or month > 12:
        raise HTTPException(status_code=400, detail="month must be between 1 and 12")
    if year < 2000 or year > 2100:
        raise HTTPException(status_code=400, detail="year must be between 2000 and 2100")

    result = (
        db.query(
            func.coalesce(func.sum(models.Expense.amount), 0).label("total_amount"),
            func.count(models.Expense.id).label("expense_count"),
        )
        .filter(
            extract("year", models.Expense.spent_on) == year,
            extract("month", models.Expense.spent_on) == month,
        )
        .one()
    )

    return {
        "month": month,
        "year": year,
        "total_amount": Decimal(str(result.total_amount)),
        "expense_count": result.expense_count,
    }
