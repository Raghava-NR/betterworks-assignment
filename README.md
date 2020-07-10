**PYTHON 3.6**


**Tasks Completed:**

Rest-ful APIs for the data required as per the FE.


**Tasks TBD:**

1. Need to write test cases.
2. Error handling mechanism. (creating a custom exception handler)
3. Proper structured response data. (creating a custom renderer)
4. Setting-up Authentication


**Deployment Steps:**

Firstly create a DB and dump the data from .sql file.

1. Clone the repo:      
   git clone https://github.com/Raghava-NR/betterworks-assignment.git
2. Navigate to the _betterworks_ folder present in the project.
3. Create a virtualenv using python 3.6:
   _python3 -m venv env_name_
4. Activate the virtualenv:
   _source env_name/bin/activate_
5. Install requirements:
   _pip install -r requirements.txt_
6. Create a config file with name config.ini:
   _touch config.ini_
7. Edit the config.ini with the required values. Sample is shown below.
   
   _[main]
   secret_key = 3@=g%1dxcdbp*^#tlmt!jtj_ef(cli@nw7!*8c8ghi9+cnckb8
   
   [database_default]
   host = 127.0.0.1
   name = db_name
   user = user_name
   password = user_password_
   
   
   
8. Run server:
   _./manage.py runserver_