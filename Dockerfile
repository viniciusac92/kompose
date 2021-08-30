# imagem base
FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN apt update \
    && apt install -y libpq-dev gcc
RUN pip install psycopg2

COPY . /code/
WORKDIR /code
