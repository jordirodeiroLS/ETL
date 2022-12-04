FROM python:3.8-slim
RUN apt-get update && apt-get -y install \
    pip \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
#CMD python Controller.py
CMD python Application.py

# TODO: create volume
# TODO: Add stuff to requirements.txt

# Docker command:
# docker build -t etl:1.0 .
# docker run -it --rm --name etl_v1 --volume "$(pwd)/data:/app/data" etl:1.0
