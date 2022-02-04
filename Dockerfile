FROM python:3.8

# Install system dependencies
RUN apt-get update
RUN apt-get install git -y

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
