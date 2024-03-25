FROM ubuntu:22.04

ENV TZ=Europe/Warsaw

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y vim software-properties-common wget unzip

# Python3.8
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y python3.8
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1 \
    && update-alternatives --set python3 /usr/bin/python3.8

# Java 8
RUN apt-get install -y openjdk-8-jdk

# Kotlin
RUN wget https://github.com/JetBrains/kotlin/releases/download/v1.9.23/kotlin-compiler-1.9.23.zip \
    && unzip kotlin-compiler-*.zip -d /opt/ \
    && rm kotlin-compiler-*.zip

ENV PATH="${PATH}:/opt/kotlinc/bin"

ENV DEBIAN_FRONTEND=

WORKDIR /home/jaknow