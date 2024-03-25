FROM ubuntu:22.04

ENV TZ=Europe/Warsaw

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y vim software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y python3.8

ENV DEBIAN_FRONTEND=

WORKDIR /app
