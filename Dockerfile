FROM python:2.7
MAINTAINER Bruno Martins <bscmartins@gmail.com>

RUN apt-get update && apt-get install -y freetds-dev

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD uwsgi.ini /app/uwsgi.ini
ADD webhook_server.py /app/webhook_server.py

WORKDIR /app
CMD ["uwsgi", "--ini", "uwsgi.ini"]
