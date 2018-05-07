FROM ubuntu:16.04

MAINTAINER Bee Lilac "b@curious.o"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# docker cache the reqs
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
