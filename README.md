# How to install
- Install mysql database
- create a user: root with password: PASSWORD  (Or change the credentials in tests/.env)
- create database test_main_db
- pip install -r requirements.txt
- pip install -r requirements_dev.txt

# How to run tests
- cd tests
- PYTHONPATH=../app pytest test_register.py  