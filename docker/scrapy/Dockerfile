FROM --platform=linux/x86_64 python:3.9.16-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip && pip install --no-cache-dir -r ./requirements.txt