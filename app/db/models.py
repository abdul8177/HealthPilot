# app/db/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from app.db.session import Base

class GlucoseLog(Base):
    __tablename__ = "glucose_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    timestamp = Column(DateTime)
    glucose_level = Column(Float)
    meal_type = Column(String)
