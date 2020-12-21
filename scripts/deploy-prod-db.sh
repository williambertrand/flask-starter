# Before running, make sure env variable DEPLOY_DB_URL is set to our production DB url
export FLASK_APP=./app.py
export FLASK_ENV=deploy

flask db migrate
flask db upgrade

echo 'Flask db migration compelte.'