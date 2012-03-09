#!/bin/bash
set -e
LOGFILE=/home/bezrukov/Envs/house_shop/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# user/group to run as
USER=bezrukov
GROUP=bezrukov
ADDRESS=127.0.0.1:8001
PID=/home/bezrukov/Envs/house_shop/gunicorn.pid
cd /home/bezrukov/Envs/house_shop/source
source /home/bezrukov/Envs/house_shop/bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn_django -w $NUM_WORKERS --bind=$ADDRESS \
  --user=$USER --group=$GROUP --log-level=debug -p $PID \
  --log-file=$LOGFILE 2>>$LOGFILE
