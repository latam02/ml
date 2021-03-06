FROM tensorflow/tensorflow:2.6.0

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && \
    apt-get -y install ffmpeg libsm6 libxext6  -y && \
    pip install --upgrade pip && \
    apt -y install python3-dev libpq-dev

COPY ./requirements-prod.txt requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000

ENTRYPOINT ["bash", "./entrypoint.sh" ]
