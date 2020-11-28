#!/bin/bash

if test $OSTYPE = darwin18; then
    export DOCKERHOST='host.docker.internal';
elif test $OSTYPE = linux-gnu; then
    export DOCKERHOST='89.223.120.79';
else
    export DOCKERHOST='89.223.120.79';
fi

echo ${DOCKERHOST}
docker stop flaskapp && docker rm flaskapp
docker build -t flaskapp-image .
docker run -d --name flaskapp -p 80:5000 -e DOCKERHOST=${DOCKERHOST} -e PSQL_PASSWORD=${PSQL_PASSWORD} flaskapp-image
