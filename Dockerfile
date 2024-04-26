FROM python:3.11.5-slim-bullseye

WORKDIR /app
ENV FLASK_APP=main.py

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt