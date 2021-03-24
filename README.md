# TeamCity webinar - python API tests

## Installation to run from a terminal

1. Download [Python 3.9](https://www.python.org/downloads/)
2. Install Python from the downloaded package.
3. Clone the project, navigate to project directory from your terminal, run:
```pip3 install -r requirements.txt```

## Running from a terminal
Set domain variable PYTEST_DOMAIN, then:
```python3 -m pytest --alluredir=test_results/ tests```

## Report
To generate the report, run ```allure serve test_results```

More about Allure implementation for pytest is [here](https://docs.qameta.io/allure/#_pytest).

## Running inside the Docker
```docker build -t pytest_check .```

```docker run --rm --mount type=bind,src=$(pwd),target=/tests/ pytest_check```





