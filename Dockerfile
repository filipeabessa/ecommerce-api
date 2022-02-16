FROM python:3.8

# Install system dependencies
RUN apt-get update
RUN apt-get install git -y

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# install psycopg2
RUN apt-get update \
    && apt-get -y install gcc \
    && pip install psycopg2

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# run gunicorn
CMD gunicorn hello_django.wsgi:application --bind 0.0.0.0:$PORT