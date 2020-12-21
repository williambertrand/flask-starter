# Starter API
Starter Flask API

## Getting Started

#### Create a virtualenv

1. run `python -m venv ./venv`
 
2. Activate your virtualenv: `source ./venv/bin/activate`

#### Install dependencies

run `sh scripts/install-dependencies.sh`

#### Configure DB

1. Make sure you have postgres running locally

2. replace `my_db_name` with your databse name in `.env`

#### Run the application

1. run `scripts/run.sh` to run Flask app locally on port 5000

2. To run with gunicorn: `gunicorn -b localhost:5000 -w 4 app:app` 

## Endpoints

/users
-> example setup of a basic route

## ADDING MODELS: NOTE

When adding models, you must import the models to the main factory.py file or else the migration script 
won't pick up the changes for the next generated migration


## CI /CD 
[ ] TODO

## Deploying
- This section depending on your deployment... 



## DB Starting from Scratch
Using Flask-Migrate

`flask db init` > This will create the migrations directory

## Making changes to the database

> To generate a migration automatically, Alembic compares the database schema as defined by the database models, against the actual database schema currently used in the database. It then populates the migration script with the changes necessary to make the database schema match the application models.

After editing the model files, run:

`flask db migrate` (with -m message parameter) to generate the migration script.

Then run the migration script with `flask db upgrade`