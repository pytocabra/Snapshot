# Snapshot

[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

Snapshot is a web platform for sharing your daily journeys with snaps (pictures). The website allows you to create your account, uploads snaps, describe them and explore other users' snaps.

## Technology Stack

- Django - core framework.
- Html & CSS - templates and static files.
- Bootstrap 5.0 - CSS styling.

## Setup

Create a virtual environment to install dependencies in and activate it:
```
py -m venv venv
cd venv\Scripts\activate
(venv) pip install -r requirements.txt
```
Once `pip` has finished downloading the dependencies, create database models:
```
(venv) cd snapshot
(venv) py manage.py migrate
```
Finally, run the website:
```
(venv) python manage.py runserver
```
And navigate to http://127.0.0.1:8000/
