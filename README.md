#Hybrid UI + API Automation Framework (Selenium + Pytest)
##Project Overview
This is a Hybrid Test Automation Framework built using:
- Selenium WebDriver (UI Automation)
- Pytest (Test Runner)
- Requests (API Testing)
- Jenkins (CI/CD Integration)
- Allure Reports (Test Reporting)
- pytest-xdist (Parallel Execution)

The framework supports both **UI and API testing together** and is designed for enterprise-level automation.

##Project Structure
Automation Framework Architecture
│
├── tests/ # UI + API test cases
├── pages/ # Page Object Model classes
├── utils/ # Helper utilities (agentic, config, etc.)
├── conftest.py # Fixtures
├── requirements.txt # Dependencies
├── pytest.ini # Pytest configuration
├── Jenkinsfile # CI/CD pipeline
└── README.md # Project documentation

##Features

##UI Automation
- Login functionality
- Create Note
- Delete Note
- Form validations

##API Automation
- Authentication API
- Create / Update / Delete notes via API
- Negative test cases

##Hybrid Testing
- UI created data verified using API
- API created data verified in UI

##Parallel Execution
- Implemented using `pytest-xdist`
```bash
pytest -n 2

## CI/CD Integration
- Jenkins pipeline for automated execution
- GitHub integration for source control
- Automatic test execution on commit/build

## Reporting
- Allure Reports for detailed test results
- allure serve allure-results

## How to Run Tests
- Install dependencies
- pip install -r requirements.txt
- Run all tests
- pytest
- Run in parallel
- pytest -n 2

# Generate Allure report
- pytest --alluredir=allure-results
- allure generate allure-results -o allure-report --clean

##CI/CD Pipeline (Jenkins)
- Pipeline stages:
- Checkout Code from GitHub
- Install Dependencies
- Clean old reports
- Run tests in parallel
- Generate Allure Report

## Advanced Features (Agentic Layer)
- Smart Waits (flaky element handling)
- Retry mechanism for unstable tests
- Self-healing locator strategy (fallback locators)
- Intelligent execution flow handling


## Test Coverage
- UI Functional Testing
- API Functional Testing
- Negative Testing
- End-to-End Hybrid Scenarios

## Tools & Technologies

- Python 3.x
- Selenium WebDriver
- Pytest
- Jenkins
- GitHub
- Allure Reports


