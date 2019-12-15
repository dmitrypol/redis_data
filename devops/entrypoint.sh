#!/bin/bash
# https://docs.docker.com/config/containers/multi-service_container/
set -m

# https://ryanstutorials.net/bash-scripting-tutorial/bash-if-statements.php
if [ $CONTAINER_TYPE = 'web' ]
then
    flask run -h 0.0.0.0 -p 5000 &
    jupyter notebook --ip=0.0.0.0 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password='' &
elif [ $CONTAINER_TYPE = 'worker' ]
then
    rq worker -c rq_config &
fi

fg %1