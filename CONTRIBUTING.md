# Contributing

Thanks for your interest in improving Expense Tracker API!

## Getting started

1. Fork the repository.
2. Clone your fork:
   ```bash
   git clone https://github.com/<your-username>/expense-tracker-api.git
   cd expense-tracker-api
   ```
3. Create and activate a virtual environment.
4. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```

## Making changes

- Keep changes focused and consistent with the existing project structure.
- Use clear names and add or update tests when changing behavior.
- Do not commit local databases, virtual environments, secrets, or environment-specific files.
- Update the README when adding or changing API functionality.

## Running tests

Run the test suite from the project root:

```bash
python -m pytest -q
```

Please make sure the tests pass before opening a pull request.

## Pull requests

1. Create a feature branch for your change.
2. Describe what you changed and why.
3. Include relevant test results.
4. Link related issues, if applicable.

Thanks for helping make the project better!
