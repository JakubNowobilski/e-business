FROM ubuntu:22.04

ENV TZ=Europe/Warsaw

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /home/jaknow

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y vim software-properties-common wget unzip curl zip

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

# Gradle
RUN curl -s "https://get.sdkman.io?rcupdate=false" | bash
RUN bash -c "source /root/.sdkman/bin/sdkman-init.sh && sdk install gradle 8.7"
CMD ["bash", "-c", "source /root/.sdkman/bin/sdkman-init.sh && gradle build"]
CMD ["bash", "-c", "source /root/.sdkman/bin/sdkman-init.sh && gradle run"]

COPY build.gradle /home/jaknow
ADD src /home/jaknow/src

ENV DEBIAN_FRONTEND=