from databases import Database
import os

DATABASE_URL = "postgresql://admin:admin@localhost/traffic_violation_db"

database = Database(DATABASE_URL)
