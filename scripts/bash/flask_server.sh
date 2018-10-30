#!/bin/bash

cd flaskapp
pwd
export FLASK_APP=flaskapp.py
export FLASK_DEBUG=1
printenv FLASK_APP
printenv FLASK_DEBUG
#flask run --host=0.0.0.0
gunicorn -b 0.0.0.0:4000 flaskapp:app --daemon

echo "web server (gunicorn) started on port 4000"
