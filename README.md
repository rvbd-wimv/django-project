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

