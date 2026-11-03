from sqlalchemy import Column, Date, Integer, Numeric, String, Text
from datetime import date

from .database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, index=True)
    amount = Column(Numeric(10, 2), nullable=False)
    category = Column(String(50), nullable=False, index=True)
    description = Column(Text, nullable=True)
    spent_on = Column(Date, nullable=False, default=date.today)
