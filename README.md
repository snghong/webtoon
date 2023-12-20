## Text to webtoon generator project
- Design document and milestones available here: https://docs.google.com/document/d/1MplfSnmNXhZZkV8tL8orX0uP6eUbevGm_luDP45rl4A/edit?usp=sharing

## Contributing:
- pick a milestone
- git pull / git clone
- git branch
- build your milestone
- make a Pull Request :>

## Authors: 
- Sng Hong
- Neo Jing Xuan

## Stack
- Django web framework
- SQLite for DB
- LLM APIs for queries

## Dependencies
- Django
- SQLite
- Python
- openAI

## Set-Up
1. Run `python3 -m venv env` to create a virtual environment called "env"
2. Run `source env/bin/activate` to change your environment
3. Run `pip install -r requirements.txt` to install dependencies
4. Change .env.example file to .env and fill in the variables in the file

## Running the server
- From the root directory, run python3 manage.py runserver
- Create a user / Login as needed
- Enter your desired story settings at /gen/input
- View webtoon

## Setting up the server
- Sign up with a new user account from the root page
- create a superuser (admin) account for yourself with `python3 manage.py createsuperuser`
- Access the admin dashboard by clicking on 'Admin Login' from the root page

## Database Migrations
- Delete any existing db.sqlite3 files or __pycache__ folders
- Create or update the model
- Create a DB migration: `python manage.py makemigrations`
- Apply the migration: `python manage.py migrate --run-syncdb`
