# syntax=docker/dockerfile:1
FROM python:3.10-slim-bullseye as base
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

RUN apt-get update && \
  apt-get install -y gcc libpq-dev

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --deploy --system

RUN useradd --create-home appuser
WORKDIR /home/appuser/online_menu/
USER appuser

COPY . .
