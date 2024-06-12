import os

workers = int(os.environ.get('GUNICORN_PROCESSES', '2'))
threads = int(os.environ.get('GUNICORN_THREADS', '4'))
# timeout = int(os.environ.get('GUNICORN_TIMEOUT', '120'))

## Production
# bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:8080')

## Local testing
bind = os.environ.get('GUNICORN_BIND', '127.0.0.1:5051')

forwarded_allow_ips = '*'

secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }

## To run locally without docker image: 
#gunicorn --config gunicorn_config.py main:app