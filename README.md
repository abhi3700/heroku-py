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
6. Make sure IP (0.0.0.0) whitelisted in MongoDB Atlas.
   > Why allow all? Because heroku app is not static, it can change IP. Although there is a way to fix it i.e. by using M10 & above, which has private IP whitelisting where you can whitelist private IP ranges of the region where the heroku app is hosted.

Try to access the endpoint: `curl https://hello.herokuapp.com/health`.
