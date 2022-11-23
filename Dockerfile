FROM python:3.8-slim
RUN apt-get update && apt-get -y install \
    git \
    && rm -rf /var/lib/apt/lists/*
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python Controller.py