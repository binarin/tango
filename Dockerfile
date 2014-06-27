FROM debian:jessie
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y update
RUN apt-get install -y python-pip less apt-utils python-dev libpython-dev
RUN pip install -U Django==1.6.5
RUN pip install -U Pillow==2.4.0
