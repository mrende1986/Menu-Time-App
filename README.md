# Menu Time App

## Running locally - Use python 3.10

1. Use a virtual environment by running: `python3 -m venv .venv` (leave the virtual environment name as `env` if you want .gitignore to pick it up )
2. Activate virtual env: `source .venv/bin/activate`
3. Install requirements: `pip3 install -r requirements.txt`
4. Update gunicorn_config comment line 8 and uncomment line 11 (to run locally)
4. Run app: `gunicorn --config gunicorn_config.py main:app`
