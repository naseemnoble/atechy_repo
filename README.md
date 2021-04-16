# Atechy_repo

Atechy_repo is REST API with Python django rest api framework.

## Steps for running

Install virtualenv, It is a tool to create isolated Python environments
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
* Users Sign Up with (First Name, Last Name, Email Address, Password, Role), 
If Role is admin use `is_superuser=True` and 
Role is user use `is_superuser=False`
```
curl --location --request POST 'http://127.0.0.1:8000/app1/register/' --form 'is_superuser=True' --form 'first_name="John"' --form 'last_name="smith"' --form 'email=john@gmail.com' --form 'password="smith@123"' --form 'password2="smith@123"'
```
* Generating JWT tokens with gmail address and password
```
curl --location --request POST 'http://127.0.0.1:8000/app1/token_request/' --form 'username=john@gmail.com' --form 'password=smith@123'
```
Response
```
{"refresh":**<REFRESH TOKEN>**, "access":**<ACCESS TOKEN>**}
```
* User sign in with JWT tokens
```
curl --location --request GET 'http://127.0.0.1:8000/app1/signin/' --header 'Authorization: Bearer **<ACCESS TOKEN>**
```
Example
```
curl --location --request GET 'http://127.0.0.1:8000/app1/signin/' --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NTcwMTY2LCJqdGkiOiJhNWVkNjJhODVmODg0Y2RmYTBmMzY2ZThmM2FlNzM2OSIsInVzZXJuYW1lIjoiam9obkBnbWFpbC5jb20ifQ.4bfmSePGmKZ3P_42R9XJ5Kb1v-AK811hFIGOtV91-jI'
```
* Request to change user first and last name with authentication and verification
```
curl --location --request PUT 'http://127.0.0.1:8000/app1/updateprofile/1/' --header 'Authorization: Bearer **<ACCESS TOKEN>** --form 'first_name="John john"' --form 'last_name="Smith smith"
```
* Store authenticated user customer support ticket by storing (User ID, Message)
```
curl --location --request POST 'http://127.0.0.1:8000/app1/ticket/' --header 'Authorization: Bearer **<ACCESS TOKEN>** --form 'message=tiket message'
```
* Admin user request to list customer support tickets
```
curl --location --request GET 'http://127.0.0.1:8000/app1/listticket/' --header 'Authorization: Bearer **<ACCESS TOKEN>**
```
Response if we use Admin ACCESS TOKEN
```
[
    {
        "Message": "ticket 2",
        "TicketId": 2,
        "User Id": "john@gmail.com"
    },
    {
        "Message": "\"ticket 3\"",
        "TicketId": 3,
        "User Id": "john@gmail.com"
    }
]
```
Response if we use normal user ACCESS TOKEN
```
{
    "message": "User chris@gmail.com has no permission to list customer support tickets"
}
```
