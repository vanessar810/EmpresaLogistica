from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.configuration.database import Base
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(20), default="user")
    
    cliente = relationship("Cliente", back_populates="user", uselist=False)