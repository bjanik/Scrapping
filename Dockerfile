FROM python:latest

WORKDIR /scrap

RUN pip3 install requests bs4 mysql-connector-python

COPY *.py .