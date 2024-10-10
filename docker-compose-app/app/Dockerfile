FROM python:alpine

LABEL authors="semyon"

WORKDIR ./app

RUN pip install pymongo

COPY . .

CMD ["python", "main.py"]