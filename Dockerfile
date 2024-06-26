FROM ubuntu

RUN apt-get update
RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get -y install python3.7
RUN apt-get -y install python3-pip
# RUN apt-get -y install build-essential libssl-dev libffi-dev python-dev


WORKDIR /seshat

COPY requirements.txt ./requirements.txt
RUN pip3 --no-cache-dir install -r requirements.txt
# RUN apt install -y nodejs
RUN apt install -y npm
RUN npm install -g pm2
RUN apt install -y nano

ARG AWS_DEFAULT_REGION
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

ENV AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

COPY . ./
EXPOSE 8002
EXPOSE 8001
