# Cassandra-django-boilerplate

## Installation

Requirements:

- Default requirements mentioned below.
Follow these steps:
  
Create Virtual Environment
```sh
pip install virtualenv
virtualenv cassBase
source cassBase/bin/activate
```

```sh
docker pull cassandra:latest
docker network create cass-cluster-network
docker run --name nodeA --network cass-cluster-network cassandra
docker stop nodeA
docker rm nodeA
```

Make env file
- Copy `.env.example` file to `.env`

Install Requirement
```sh
pip install -r requirements.txt
```

- Sync Cassandra db
```sh
python db_sync.py
```
 
- Run Project
```sh
python manage.py runserver
```

