from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URL = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_URL)
mongo_db = client.traffic_violation_logs
