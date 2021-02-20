# docker image rm pytest_check
# docker image ls

# docker build -t pytest_check .
# docker run --rm --mount type=bind,src=$(pwd),target=/tests/ pytest_check

FROM python

WORKDIR /tests

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV TEAMCITY_VERSION=85899

#ENV PYTEST_DOMAIN="https://playground.learnqa.ru/ajax/"

CMD python -m pytest -s --alluredir=test_results/ tests/