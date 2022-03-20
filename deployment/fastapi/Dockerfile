FROM python:3.8.1-slim-buster
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

LABEL MAINTAINER="Iqbal Maulana <iqbalmaulana@programmer.net>"

WORKDIR /app

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /app

EXPOSE 3004

RUN groupadd -r mnist && useradd -g mnist mnist
RUN chown -R mnist:mnist /app

USER mnist

WORKDIR /app

RUN chmod +x /app/bin/deploy.sh
ENTRYPOINT [ "/app/bin/deploy.sh" ]