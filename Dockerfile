FROM ubuntu:16.04

MAINTAINER Bee Lilac "i@i.i"

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y \
    python-pip \
    python-dev \
    sqlite3 \
    libsqlite3-dev

# docker cache the reqs
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

COPY ./data.sql /app

# initialize database with initial users
RUN sqlite3 cops.db < data.sql && rm data.sql

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
