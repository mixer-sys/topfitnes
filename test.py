# выяснитть что число кратно 4 или 400 но не кратно 100
a = int(input())
if a % 4 == 0 or a % 400 == 0:
    if a % 100 != 0:
        print('да')
    else:
        print('нет')
else:
    print('нет')


docker container stop `docker container ls -aq`
docker container rm `docker container ls -aq`
docker image rm `docker image ls -aq`
docker volume rm `docker volume ls -q`
docker system prune -a

git clone 

docker build -t bot .

docker run --env-file .env

docker system prune -a

docker compose -f docker-compose.production.yml up

docker exec -it db psql -U django_user -d django
\l

docker network create django-network 
docker network connect django-network db 

docker compose exec backend python manage.py migrate

docker compose exec django_bot python manage.py makemigrations