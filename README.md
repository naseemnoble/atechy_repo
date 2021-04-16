# Atechy_repo

Atechy_repo is REST API with Python django rest api framework.

## Steps for running

Install virtualenv
```bash
pip install virtualenv
```
Create a virtual environment 'atechy_venv' for a project (Python 3.x interpreter used)
```
virtualenv -p /usr/bin/python3 atechy_venv
```
Activate virtualenv 'atechy_venv'
```
source atechy_venv/bin/activate
```
clone project from github
```
git clone https://github.com/naseemnoble/atechy_repo.git
```
Change to Project repository directory
```
cd atechy_repo
```
Install django and rest api dependencies
```
pip install -r requirements.txt
```
Change to Project root directory
```
cd atechy1
```
Migrate database
```
python manage.py migrate
```
Run server
```
python manage.py runserver
or
python manage.py runserver 8080 (Change port to 8080)
```
## APIs
