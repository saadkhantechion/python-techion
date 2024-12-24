# python-techion

# Prerequisite
```shell
pip3 install falcon
pip3 install gunicorn
```

# Running
```shell
gunicorn -b 127.0.0.1:8000 appserver:app 
```

# Postgres Setup
```shell
docker run --name postgres -d -p 5432:5432 -e POSTGRES_PASSWORD=test -e POSTGRES_USER=test postgres:latest
docker rm postgres
```