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
Users Sign Up with (First Name, Last Name, Email Address, Password, Role)
If Role is admin use is_superuser=True
Role is user use is_superuser=False
```
curl --location --request POST 'http://127.0.0.1:8000/app1/register/' --form 'is_superuser=True' --form 'first_name="John"' --form 'last_name="smith"' --form 'email=john@gmail.com' --form 'password="smith@123"' --form 'password2="smith@123"'
```