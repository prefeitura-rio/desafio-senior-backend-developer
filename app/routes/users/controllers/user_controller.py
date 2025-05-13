from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException

from app.db.models.user import User
#from app.users.schemas.user_schema import UserCreate


class UserController():
    """Add docstring aqui e nas funções"""
    
    def __init__(self, email, db_session: Session):  # acho que aqui deveria ser o cpf
        self.email = email
        self.db_session = db_session

    def post(self, user):
        """"""
        user_exist = User.get_user_by_email(self.db_session, self.email)
        if user_exist:
            raise HTTPException(
                status_code=400,
                detail="User email already registered"
            )
        return User.create_user(self.db_session, user=user) #melhorar resposta de sucesso

