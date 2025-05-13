from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from app.db.models.user import User

from passlib.context import CryptContext


crypt_context = CryptContext(schemes=['sha256_crypt'])

#SECRET_KEY = config('SECRET_KEY')
#ALGORITHM = config('ALGORITHM')
SECRET_KEY = 'f7fdf23eb3b76d1789e0cc94331cfca849e97960dc08c5236bef3e1113ff38f0'
ALGORITHM = 'HS256' # ad o config do decouple


class UserAuthController():
    """Add docstring aqui e nas funções"""
 
    def __init__(self, db_session: Session):  # acho que aqui deveria ser o cpf
        self.db_session = db_session

    def get_user_token(self, access_token):
        try:
            data = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
            user = User.get_user_by_email(
                self.db_session,
                email=data['sub']
            )
 
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='User not found'
            )

        return user

    def verify_token(self, access_token):
        try:
            self.get_user_token(access_token)
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid token")
