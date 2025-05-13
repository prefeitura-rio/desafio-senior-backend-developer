from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.db import Base


class CreditUser(Base):
    __tablename__ = "credit_user"

    id = Column(Integer, primary_key=True, index=True)
    credit_value = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", backref="credit_user")

    @classmethod
    def get_credit_by_user_id(cls, db: Session, user_id: int):
        return db.query(cls).filter(
            cls.user_id == user_id
        ).first()
    
    @classmethod
    def create_credit(cls, db: Session, user_id: int, credit: float):
        print("CCCCCCCCCCC", credit)
        db_credit = cls(
            credit_value=credit,
            user_id=user_id,
        )
        #try: #melhorar essas aqui, talvez levar o try ecept pro controller

        db.add(db_credit)
        db.commit()
        db.refresh(db_credit)
        return db_credit
    
    @classmethod
    def update_credit(cls, db: Session, user_id: int, new_credit: float):
        db.query(cls).filter(cls.id == user_id).update(
            {"credit_value": new_credit}
        )
        db.commit()
        return db.query(cls).filter(cls.id == user_id).first()
