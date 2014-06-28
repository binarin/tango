FROM debian:jessie
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y update
RUN apt-get install -y python-pip less apt-utils python-dev libpython-dev
RUN pip install -U Django==1.6.5
RUN pip install -U Pillow==2.4.0
RUN apt-get install -y libpq-dev
RUN pip install -U psycopg2==2.5.3
RUN pip install -U South==0.8.4
WORKDIR /code
