FROM python:3.7-slim-stretch

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN apt-get update && apt-get install gunicorn -y && pip3 install -r requirements.txt
