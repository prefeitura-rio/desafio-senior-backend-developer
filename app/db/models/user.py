from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

#from app.db.database import Base
from app.db import Base
from app.routes.users.schemas.user_schema import UserCreate, UserLogin
from passlib.context import CryptContext


crypt_context = CryptContext(schemes=['sha256_crypt'])


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    document_number = Column(String, unique=True, index=True)
    name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    #credits = relationship("Credit", backref="user")

    @classmethod
    def get_user_by_document_number(cls, db: Session, user_document_number: str):
        return db.query(cls).filter(
            cls.document_number == user_document_number
        ).first()

    @classmethod  # talvez nao precise desse aqui
    def get_user_by_email(cls, db: Session, email: str):
        return db.query(cls).filter(cls.email == email).first()

    @classmethod
    def create_user(
        cls,
        db: Session, user: UserCreate
    ):  # essas manipulações nao sãopara estarem aqui
        db_user = cls(
            email=user.email,
            hashed_password=crypt_context.hash(user.password),
            name=user.name,
            document_number=user.document_number
        )
        #try: #melhorar essas aqui, talvez levar o try ecept pro controller

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        #except IntegrityError:
        """ raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User already exists'
        ) """
        return db_user
