FROM python:2.7
ENV PYTHONUNBUFFERED 1

MAINTAINER Philippe Bazard "bazard.philippe@gmail.com"

RUN mkdir /app
COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt
ADD . /app/

COPY ./run_web.sh /app/run_web.sh
RUN sed -i 's/\r//' /app/run_web.sh
RUN chmod +x /app/run_web.sh

WORKDIR /app