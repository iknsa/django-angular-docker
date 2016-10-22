FROM python:2.7
MAINTAINER Philippe Bazard "bazard.philippe@gmail.com"
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/