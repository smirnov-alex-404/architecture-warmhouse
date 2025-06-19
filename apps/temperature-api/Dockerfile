FROM python:3.12-slim

WORKDIR /temperature_app

COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./main.py

EXPOSE 8081
