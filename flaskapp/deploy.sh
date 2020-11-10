#!/bin/bash

if test $OSTYPE = darwin18; then
    export DOCKERHOST='host.docker.internal';
elif test $OSTYPE = linux-gnu; then
    export DOCKERHOST='89.223.120.79';
else
    export DOCKERHOST='89.223.120.79';
fi

echo ${DOCKERHOST}
docker stop mycontainer && docker rm mycontainer
docker build -t myimage .
docker run -d --name mycontainer -p 80:5000 -e DOCKERHOST=${DOCKERHOST} myimage
