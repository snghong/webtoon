## Text to webtoon generator project
- Design document and milestones available here: https://docs.google.com/document/d/1MplfSnmNXhZZkV8tL8orX0uP6eUbevGm_luDP45rl4A/edit?usp=sharing

## Contributing:
- pick a milestone
- git pull / git clone
- git branch
- git merge

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