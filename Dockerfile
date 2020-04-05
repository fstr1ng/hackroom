FROM python:3.8
RUN apt-get update
RUN apt-get install sqlite3
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
CMD uwsgi uwsgi.ini
