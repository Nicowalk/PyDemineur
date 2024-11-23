.PHONY: all install test coverage sphinx black pylint clean

all: install black pylint test coverage sphinx

install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

test:
	@echo "Running tests..."
	pytest ./tests/

# Coverage analysis
coverage:
	@echo "Running coverage analysis..."
	coverage run --source ./src -m pytest
	coverage report

sphinx:
	@echo "Building Sphinx documentation..."
	sphinx-build -b html docs/ docs/_build/html

black:
	@echo "Formatting code with Black..."
	black .

pylint:
	@echo "Linting code with Pylint..."
	pylint .\src\

clean:
	rm -rf docs/_build
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov