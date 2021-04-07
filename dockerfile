FROM python:3.8.8-slim-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
COPY . /code/
WORKDIR /code/
RUN pip install -r ../requirements.txt
RUN pip install gunicorn