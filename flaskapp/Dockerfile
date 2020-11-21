FROM python:3.6-buster

WORKDIR /home/flaskapp

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY app app
COPY migrations migrations
COPY flaskapp.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP flaskapp.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
