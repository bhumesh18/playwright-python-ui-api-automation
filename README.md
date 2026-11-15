# Python Playwright UI & API Automation Framework

A practice automation framework built with **Python, Playwright and Pytest**. It demonstrates browser-based end-to-end testing and REST API testing, with reusable fixtures, Page Object Model (POM), an API client, response validation, logging, screenshots on failure and HTML test reports.

> **Project purpose:** demonstrate practical UI and API automation techniques in a small, understandable framework. The UI and public API endpoints used here are demo services, not production systems.

## Features

### UI automation

- Browser automation with Playwright for Python (synchronous API).
- Pytest fixtures for browser, page and test setup.
- Page Object Model with separate page classes for login, inventory, cart and checkout.
- User-facing locators such as role and placeholder locators, as well as stable CSS/test-attribute locators.
- Positive and negative login scenarios.
- Product listing, cart operations and checkout workflow checks.
- Playwright assertions with automatic waiting and retrying.

### API automation

- HTTP methods: `GET`, `POST`, `PUT`, `PATCH` and `DELETE`.
- Response status, headers and JSON-body validation.
- Query-parameter and path-parameter checks.
- Positive and negative API scenarios.
- Pytest parameterization for data-driven tests.
- Bearer authorization-header checks.
- A reusable `APIClient` wrapper around Playwright's `APIRequestContext`.
- Shared response-validation helpers.

### Test diagnostics

- Pytest logging to the terminal and a log file.
- Screenshots and Playwright traces retained on test failure, as configured in `pytest.ini`.
- HTML reports generated with `pytest-html`.

## Technology stack

- Python
- Playwright for Python
- Pytest
- `pytest-playwright`
- `pytest-html`

The exact dependency versions are maintained in [`requirements.txt`](requirements.txt).

## Project structure

```text
playwright-python-ui-api-automation/
│
├── pages/                         # UI Page Object classes
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── ui_tests/                      # Browser-based UI tests
│   ├── test_login_pom.py
│   ├── test_login_parametrize.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── api_tests/                     # API tests and API framework code
│   ├── utils/
│   │   └── response_validator.py
│   ├── api_client.py
│   ├── config.py
│   ├── test_api_client.py
│   ├── test_posts_parametrize.py
│   └── test_auth_api.py
│
├── reports/                       # Generated HTML reports (not committed)
├── logs/                          # Generated log files (not committed)
├── test-results/                  # Playwright screenshots and traces (not committed)
│
├── conftest.py                    # Shared Pytest fixtures
├── pytest.ini                     # Test discovery, logging and Playwright options
├── requirements.txt               # Python dependencies
├── .gitignore
└── README.md
```

## Prerequisites

- Python installed (Python 3.10 or later recommended).
- Git, if you plan to clone or contribute to the repository.
- Internet access to reach the public demo applications and APIs.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-github-username>/playwright-python-ui-api-automation.git
cd playwright-python-ui-api-automation
```

Replace `<your-github-username>` with the GitHub account that owns the repository.

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Install the Playwright browser

```bash
python -m playwright install chromium
```

## Configuration

API base URLs and the request timeout are maintained in `api_tests/config.py`. The default demo endpoints are:

- JSONPlaceholder: `https://jsonplaceholder.typicode.com`
- HTTPBin: `https://httpbin.io`

The configuration supports environment-variable overrides:

- `API_BASE_URL`
- `AUTH_API_BASE_URL`

For example, in Windows PowerShell:

```powershell
$env:API_BASE_URL = "https://jsonplaceholder.typicode.com"
$env:AUTH_API_BASE_URL = "https://httpbin.io"
```

Do not commit real API keys, passwords, access tokens or other secrets. Use environment variables or an approved secrets manager for credentials.

## Running the tests

Run commands from the repository root, where `pytest.ini` and `conftest.py` are located.

### Run the complete test suite

```bash
python -m pytest -v
```

### Run only UI tests

```bash
python -m pytest -v ui_tests/
```

Run UI tests with a visible browser:

```bash
python -m pytest -v --headed ui_tests/
```

### Run only API tests

```bash
python -m pytest -v api_tests/
```

### Run a specific test file

```bash
python -m pytest -v api_tests/test_api_client.py
```

### Generate an HTML report

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

Open `reports/report.html` in a browser to review the test results. The `pytest.ini` configuration also enables terminal/file logging and Playwright failure artifacts.

## Framework design

### UI test flow

1. Pytest discovers the tests and loads shared fixtures from the root `conftest.py`.
2. The fixtures create a Playwright browser page and the required page objects.
3. Test functions call reusable page-object methods.
4. Playwright assertions verify the expected UI state.

### API test flow

1. A Pytest fixture creates an `APIRequestContext` with the configured base URL.
2. The `APIClient` provides reusable methods for the supported HTTP verbs and centralizes common request handling and logging.
3. Tests call the API client and receive Playwright API responses.
4. Shared helpers in `api_tests/utils/response_validator.py` validate common response properties.
5. Individual tests assert endpoint-specific response data and expected behavior.

## Demo services and testing limitations

This project uses public demo services so that the examples can be run without access to a private application.

- **SauceDemo** is used for UI login, inventory, cart and checkout scenarios. Use only the publicly provided demo environment and test credentials documented by the service.
- **JSONPlaceholder** is used for REST API examples. Its write operations (`POST`, `PUT`, `PATCH` and `DELETE`) are simulated; changes are not persisted as they would be in a production API.
- **HTTPBin `/bearer`** is used to check Bearer authorization-header presence and format. It is not a real identity provider and does not validate JWT signatures, token expiry, user identity or permissions.

The tests require network access and can be affected by availability or behavior changes in these external demo services. They are intended for learning and demonstration, not production acceptance testing.

## Notes on generated files and secrets

The repository's `.gitignore` excludes local virtual environments, Python caches, generated reports, logs, screenshots, traces and other test artifacts. These files are created locally when tests run and are not required to use the framework.

Never commit `.env` files or real credentials. Review `git status` before committing or pushing changes.

## Possible future improvements

- Add API schema validation and reusable business-level assertions.
- Add token acquisition against a dedicated test authentication service.
- Add CI execution (for example, GitHub Actions).
- Add richer test data management and environment-specific configuration.

## License

This project is intended as a learning and portfolio project. Add a `LICENSE` file if you choose to distribute it under a specific open-source license.
