# django-project
### keeping django-secret for test environment - replace it if needed

clone it (git clone) and build it 
```
git clone -b oauth2 --single-branch https://github.com/rvbd-wimv/django-project.git
```

Change the .env variables
```
vi .env
```
Build the dockercompose
```
docker-compose up --build
```

remove and rebuild it usefull commmands
```
docker-compose down
docker volume ls 
docker volume rm django-project_vol_db
docker-compose up --build --force-recreate
```

step 1 - change the .env file with the correct values
step 2 - create application via the admin interface

step 3 - request a access_token with scope
```
curl -X POST \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "grant_type=client_credentials" \
-d "client_id=someclientid" \
-d "client_secret=someclientsecret" \
-d "scope=customers" \
http://127.0.0.1/oauth2/token/
```

Scopes: users, customers
