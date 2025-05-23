FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y build-essential gcc make python3 python3-pip \
    manpages-posix-dev libpthread-stubs0-dev util-linux

WORKDIR /lab09/06_sendmq

CMD ["bash"]