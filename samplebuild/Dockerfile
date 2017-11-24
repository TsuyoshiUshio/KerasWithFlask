FROM ubuntu:16.04
RUN apt-get update && apt upgrade -y 
RUN apt-get install wget -y
RUN wget https://packages.microsoft.com/config/ubuntu/16.04/packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb
RUN apt-get install apt-transport-https -y
RUN apt-get update
RUN apt-get install git -y
RUN git clone https://github.com/Azure/azure-storage-fuse/
RUN apt-get install pkg-config libfuse-dev cmake libcurl4-gnutls-dev libgnutls28-dev -y
RUN cd azure-storage-fuse && ./build.sh


RUN mkdir -p /mnt/blobfusetmp
RUN mkdir -p /var/blobfuse/build
RUN chmod 777 /var/blobfuse
WORKDIR /var/blobfuse

ADD connection.cfg .
ADD mount.sh .
RUN chmod +x mount.sh
# RUN ./mount.sh /var/blobfuse