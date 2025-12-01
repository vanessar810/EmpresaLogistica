from sqlalchemy.orm import Session
from app.entity.user import User

class UserRepository:
    @staticmethod
    def find_by_username(db: Session, username: str):
        return db.query(User).filter(User.username == username).first()

    @staticmethod
    def find_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def save(db: Session, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user