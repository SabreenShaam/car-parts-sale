FROM python:3.10
LABEL author='Label A'

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app/

RUN apt-get update
RUN apt-get install -y bash vim nano postgresql-client
RUN pip install --upgrade pip

RUN pip3.10 install --no-cache-dir -r requirements.txt

COPY . /app
