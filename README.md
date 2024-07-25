# Google Search Automation with Selenium, POM, and Allure Reporting

## Project Description

This project demonstrates how to automate the Google search page using Selenium WebDriver with the Page Object Model (POM) design pattern. It includes positive and negative test cases and generates test reports using Allure.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Google Chrome browser
- ChromeDriver (make sure it's in your system PATH)

You can install the required Python packages using pip:

```bash
pip install selenium pytest allure-pytest



project  structure
google_search_automation/
│
├── page_objects/
│   └── google_search_page.py
│
├── tests/
│   └── test_google_search.py
│
├── allure_report/
│
├── requirements.txt
└── conftest.py
