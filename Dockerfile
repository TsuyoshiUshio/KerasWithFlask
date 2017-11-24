FROM ubuntu:16.04
RUN apt-get update && apt upgrade -y 
RUN apt-get install wget -y
RUN wget https://packages.microsoft.com/config/ubuntu/16.04/packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb
RUN apt-get install apt-transport-https -y
RUN apt-get update
RUN apt-get -y upgrade
RUn apt-get install blobfuse -y
RUN apt-get install python3-pip python3-dev -y

RUN pip3 install tensorflow
RUN pip3 install keras
RUN pip3 install flask
RUN pip3 install azure
RUN pip3 install azure-storage-blob

RUN mkdir -p /mnt/blobfusetmp
RUN mkdir -p /var/blobfuse
RUN chmod 777 /var/blobfuse
WORKDIR /var/blobfuse

ADD connection.cfg .
ADD mount.sh .
RUN chmod +x mount.sh
# RUn blobfuse $1 --tmp-path=/mnt/blobfusetmp -o attr_timeout=240 -o entry_timeout=240 -o negative_timeout=120 --config-file=connection.cfg

# RUN ./mount.sh /var/blobfuse 





EXPOSE 5000
