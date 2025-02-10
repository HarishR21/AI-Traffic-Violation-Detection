from fastapi import FastAPI
from database import database  # PostgreSQL
from mongo_database import mongo_db  # MongoDB

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    print("✅ PostgreSQL Connected")
    print("✅ MongoDB Connected")

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    print("❌ PostgreSQL Disconnected")
