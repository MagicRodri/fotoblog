# fotoblog
### This is a blog-type social network written in django  
## Stack used
### Django + JS + Bootstrap
## How to install 
### First clone or download this repository
### Navigate inside fotoblog/ folder 
```bash
cd fotoblog/
```
### Create virtual environment  and activate it
```bash
python -m venv venv
source venv/bin/activate
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Make migrations and migrate
```bash
python manage.py makemigrations
python manage.py migrate
```
### Run server
```bash
python manage.py runserver
```
### And app should be running on localhost:8080

## App features
### A user can register and login
### A user can make and edit post
### A user can add and edit profile picture
### Users can follow each other
### User sees only posts of thoses he is following
### Users can comment blog post in real time

## Features to be added
- [ ] Posts fetching from other sources