.PHONY: all install test coverage sphinx black pylint clean

all: install black pylint test coverage sphinx

install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt || exit 1

test:
	@echo "Running tests..."
	pytest ./tests/ || exit 1

# Coverage analysis
coverage:
	@echo "Running coverage analysis..."
	coverage run --source ./src -m pytest || exit 1
	coverage report

sphinx:
	@echo "Building Sphinx documentation..."
	sphinx-build -b html docs/ docs/_build/html || exit 1

black:
	@echo "Formatting code with Black..."
	black . || exit 1

pylint:
	@echo "Linting code with Pylint..."
	pylint .\src\ || exit 1

clean:
	@echo "Cleaning up..."
ifeq ($(OS),Windows_NT)
	@echo "Windows..."
	@del /s /q docs\\_build || true
	@del /s /q .pytest_cache || true
	@del /s /q htmlcov >nul 2>&1 || true
	@del .coverage >nul 2>&1 || true
else
	@rm -rf docs/_build .pytest_cache htmlcov .coverage || true
endif