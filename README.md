# Heroku Python App

This is a simple FastAPI application that runs on Heroku. It uses the FastAPI framework and the Motor library to interact with a MongoDB database.

## Prerequisites

- Python 3.10 or later
- FastAPI
- Motor
- FastAPI
- Uvicorn

## Procedure

1. Create app on heroku: `heroku create hello`. Automatically added buildpack for python.
2. Set config vars: `heroku config:set MONGODB_URI="mongodb+srv://username:password@cluster0.blrc4.mongodb.net/"`.
3. Push to heroku: `git push heroku main`.
4. Open the app: `heroku open`.
5. Check health: `heroku logs --tail`.

Try to access the endpoint: `curl https://hello.herokuapp.com/health`.
