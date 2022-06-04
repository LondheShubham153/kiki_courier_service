FROM python:3.8-slim-buster
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
RUN pytest

CMD [ "python3", "cli_app.py" , "100", "5"]

# author
MAINTAINER Shubham Londhe

# extra metadata
LABEL version="1.0"
LABEL description="KiKi's Courier Service with Dockerfile."



