# PineAppleMusic

## Author

_El boudiri Anasse - He-Arc - 2022-2023_

## Context
This project is part of the course "Web development" during my 3rd yeard of Bachelor at the HE-ARC engineering school. The goal is to develop a web application using the Django and Vue.js frameworks. We will also use Docker to facilitate the deployment of the application.

## Description of the project

This project aims to set up a platform allowing the sharing of music between users. Users can add / listen to music. As with a social network, we can also put like / comment  on the music.

## Prerequisites

- Docker
- Docker-compose
- python 3.10
- pip

## Get started

This project is divided into two parts, the backend and the frontend. The backend is developed with Django and the frontend with Vue.js.

### Backend

- Installing Python dependencies using pipenv :

```bash
cd backend/
pip install pipenv
pipenv shell
pipenv install
```

- Migrate the database :

```bash
cd pineAppleMusic/
python manage.py migrate
```

- Load the fixtures :

```bash
python manage.py loaddata backend/fixtures/db.json
```

- Start the server :

```bash
python manage.py runserver
```

You can now access the backend at the following address: http://localhost:8000/

To access the django admin interface : http://localhost:8000/admin/
To access the swagger documentation : http://localhost:8000/swagger/

### Frontend

- Create the docker container (at the root of the frontend project):

```bash
cd frontend/
docker-compose up
```

- Connect to the docker container:

```bash
docker exec -it vuejs-pineAppleMusic /bin/bash
```

- Once in the container, you need to install the dependencies with npm :

```bash
npm install
```

- Start the server :

```bash
npm run dev
```

You can now access the website at the following address: http://localhost:8080/


## Useful Information

### Credentials with data

- Login : Anasse
- Password : anasse

**NB : Don't forget the capital letter at the beginning of the login**

I have put some data directly in the repository to facilitate the use of the application. This is not a good practice, but it is necessary to try the application.
