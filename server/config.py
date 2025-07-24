import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-fallback-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', "postgresql://bus_fidel:fidel123@localhost:5432/bus_booking_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-dev-key')