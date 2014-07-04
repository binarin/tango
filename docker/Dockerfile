FROM debian:jessie
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y update
RUN apt-get install -y python-pip less apt-utils python-dev libpython-dev
RUN pip install https://www.djangoproject.com/download/1.7c1/tarball/
RUN pip install -U Pillow==2.4.0
RUN apt-get install -y libpq-dev
RUN pip install -U psycopg2==2.5.3
RUN pip install -U ipython pylint pep8
RUN apt-get install -y strace
WORKDIR /code
