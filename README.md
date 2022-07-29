# Inventory Management System( IMS ):
1. Manager: The person who manage the website content.
2. Employee:The person who manage products detail.
3. User: The person who viste on website.


## Steps to Execute the project
## 1. Clone repository -
Run the following command to clone the repository:
```bash
git clone https://gitlab.com/mountblue/cohort-16-python/anuragm/django-toy-project.git
```
After succesfully cloning the repository, move the current directory to django-toy-project by running the following command:
```bash
cd django-toy-project
``` 

## 2. Set up the virtual environment -

Make sure that virtualenv package is already installed. If not, install it using the following command:
```bash
$ pip3 install virtualenv
```
Now, create the virtual environment:
```bash
$ virtualenv venv -p python3
```
Activate the virtual environment:
```bash
$ source ./venv/bin/activate
```
## 3. Install dependencies - 
Install the requirements for the project using the **requirements.txt** file:
```bash
$ pip3 install -r requirements.txt 
```
## 4. Setup postgresql -

If postgress not in install in virtual environment, install it first. 

    $ pip3 install postgres
    $ pip3 install psycopg2-binary
    $ sudo -i -u postgres psql

**Note:** Run all command of **create_db.sql** in psql shell for generate user and database.

## 5. Run the project - 

1. Run mange.py 
    * $ python3 manage.py makemigrations
    * $ python3 manage.py migrate 
2. Create superuser account by
    * $ python3 manage.py createsuperuser
    * $ python3 manage.py migrate 
3. Run server
    * $ python3 manage.py runserver

Open given server link on brower :

    http://127.0.0.1:8000/   

## 6. For stoping runable project

In terminal press: **ctrl + C**

**Note:** Run all command of **drop.sql** in psql shell for remove user and database.
 
Deactivate virtual environment.
```bash
$ deactivate
```

