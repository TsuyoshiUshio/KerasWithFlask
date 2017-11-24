FROM ubuntu:16.04

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install python3-pip python3-dev -y

RUN pip3 install tensorflow
RUN pip3 install keras
RUN pip3 install flask
RUN pip3 install azure
RUN pip3 install azure-storage-blob

EXPOSE 5000
