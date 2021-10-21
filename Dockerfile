FROM tensorflow/tensorflow:latest

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
RUN apt-get -y install ffmpeg libsm6 libxext6  -y

RUN pip install --upgrade pip

COPY ./requeriments.txt .

RUN pip install -r requeriments.txt --no-cache-dir

COPY . .

EXPOSE 8000
