from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost/postgres")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)

Base.metadata.create_all(bind=engine)

class MessageCreate(BaseModel):
    text: str

@app.put("/message")
def save_message(message: MessageCreate):
    db = SessionLocal()
    db_message = Message(text=message.text)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    db.close()
    return {"id": db_message.id, "text": db_message.text}
