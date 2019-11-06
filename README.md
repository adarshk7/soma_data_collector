SoMA Data Collector
===================

Script to pull data from reddit API.


Instructions
------------

1. Get your reddit App (Reddit > Preferences > Apps > Create App)
2. Get the client ID and client secret.
3. `export CLIENT_ID=<client id that you retrieved>`.
4. `export CLIENT_SECRET=<client secret that you retrieved>`
5. Optionally, `export DATABASE_HOST=<database host>`. Otherwise localhost is used.
6. Optionally, `export DATABASE_PORT=<database port>`. Otherwise 27017 is used.
7. Optionally, `export DATABASE_NAME=<database name>`. Otherwise soma is used.
8. `pip install -r requirements.txt`
9. `python main.py --subreddit <some subreddit>`


Prerequisites
-------------

- Python 3
- MongoDB
- virtualenv (optional, makes developing with python easier)
