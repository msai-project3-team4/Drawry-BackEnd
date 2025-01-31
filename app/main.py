from fastapi import FastAPI
from pymongo import MongoClient
import redis
import os

app = FastAPI()

# MongoDB 연결 설정
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/mydatabase")  # 컨테이너 내부 주소 사용
mongo_client = MongoClient(MONGO_URI)
db = mongo_client.get_database("mydatabase")
collection = db.get_collection("test_collection")

# Redis 연결 설정
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.get("/")
def read_root():
    return {"message": "안녕하세요 1월 31일 테스트입니다., FastAPI Backend with MongoDB & Redis!"}

@app.get("/mongo-test")
def mongo_test():
    doc = {"name": "Test User", "age": 25}
    collection.insert_one(doc)
    return {"message": "Inserted into MongoDB!", "data": doc}

@app.get("/redis-test")
def redis_test():
    redis_client.set("test_key", "Hello Redis!")
    value = redis_client.get("test_key")
    return {"message": "Value from Redis", "data": value}
