FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY ./app /app
COPY ./requirements.txt /requirements.txt

RUN python3 -m pip install -r /requirements.txt
RUN (cd .. && export FLASK_APP=app:app && flask db init && flask db migrate -m "users table" && flask db upgrade)
