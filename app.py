# from flask import Flask, jsonify
# from flask_pymongo import PyMongo
# import os
# from dotenv import load_dotenv
# import logging

# # Configure logging
# logging.basicConfig(level=logging.INFO)

# # Load environment variables from .env file
# load_dotenv()

# app = Flask(__name__)
# mongo_uri = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/myDatabase')
# port = os.environ.get('PORT', 5000)

# app.config["MONGO_URI"] = mongo_uri
# logging.info(f"Connecting to MongoDB at {mongo_uri}")
# mongo = PyMongo(app)

# @app.route('/')
# def index():
#     user = mongo.db.users.find_one({"name": "John Doe"})
#     return jsonify(user)

# @app.route('/health')
# def health_check():
#     return jsonify({"status": "healthy"})

# @app.route('/users')
# def get_users():
#     users = list(mongo.db.users.find({}, {"_id": 0}))
#     return jsonify(users)

# if __name__ == '__main__':
#     with app.app_context():
#         try:
#             # Check if the connection to MongoDB is established
#             if mongo.db is None:
#                 raise Exception("Failed to connect to MongoDB. Please check your MONGO_URI configuration.")
            
#             # Check if the collection is empty before inserting dummy users
#             if mongo.db.users.count_documents({}) == 0:
#                 mongo.db.users.insert_many([
#                     {"name": "John Doe", "email": "john@example.com"},
#                     {"name": "Jane Doe", "email": "jane@example.com"},
#                     {"name": "Alice", "email": "alice@example.com"},
#                     {"name": "Bob", "email": "bob@example.com"}
#                 ])
#         except Exception as e:
#             logging.error(f"Error connecting to MongoDB: {e}")
#             raise
#     port = int(os.environ.get('PORT', 5000))
#     app.run(debug=True, port=port)

from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
import os

app = FastAPI()

class HealthCheckResponse(BaseModel):
    status: str
    data: str

async def get_db_client():
    client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
    return client

@app.get("/health", response_model=HealthCheckResponse)
async def health_check(db_client: AsyncIOMotorClient = Depends(get_db_client)):
    try:
        await db_client.admin.command("ping")
        response = {
            "status": "200 OK",
            "data": "Health check passed"
        }
        return JSONResponse(status_code=200, content=response)
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))