#!/bin/bash
# https://docs.docker.com/config/containers/multi-service_container/
set -m

flask run -h 0.0.0.0 -p 5000 &

jupyter notebook --ip=0.0.0.0 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password='' &

rq worker -c rq_config &

fg %1