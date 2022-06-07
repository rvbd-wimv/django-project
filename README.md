# django-project
clone it and build it 
```
docker-compose build
docker-compose up
```

remove and rebuild it
```
docker-compose down
docker volume ls 
docker volume rm django.....
docker-compose build
docker-compose up --force-recreate
```

Request an infinity token
```
curl -X POST http://127.0.0.1:8000/api-token-auth/  \
-H "Content-Type: application/json"  \
-d '{"username":"someusername","password":"somepass"}'
```
