#!/bin/bash

# activate venv (pip installed packages)
source env/bin/activate
# start service with globally installed packages
gunicorn app:app -b $HOST:$PORT --worker-class gevent -w 4 --pythonpath "/site/site-packages"