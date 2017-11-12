docker-compose up -d --build
docker-compose run model-server python manage.py recreate_db
docker-compose run model-server python manage.py seed_db
docker-compose run model-server python manage.py test
