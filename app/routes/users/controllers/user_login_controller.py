from datetime import datetime, timedelta, timezone
from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from app.db.models.user import User
from app.routes.users.schemas.user_schema import UserLogin
from passlib.context import CryptContext


crypt_context = CryptContext(schemes=['sha256_crypt'])
#SECRET_KEY = config('SECRET_KEY')
#ALGORITHM = config('ALGORITHM')
SECRET_KEY = 'f7fdf23eb3b76d1789e0cc94331cfca849e97960dc08c5236bef3e1113ff38f0'
ALGORITHM = 'HS256' # ad o config do decouple


class UserLoginController():
    """Add docstring aqui e nas funções"""

    def __init__(self, db_session: Session, user_login: UserLogin):
        self.db_session = db_session
        self.user_login_email = user_login.email
        self.user_login_password = user_login.password

    def verify_user_password(self, user_password):
        return crypt_context.verify(self.user_login_password, user_password)

    def post(self, expires_in: int = 30):
        """"""
        print("email", self.user_login_email) 
        user_exist = User.get_user_by_email(
            self.db_session,
            self.user_login_email
        )
        print("user exist", user_exist)
        if not user_exist:
            raise HTTPException(
                status_code=400,
                detail="Invalid email or password1"
            )

        match_password = self.verify_user_password(
            user_exist.hashed_password,
        )
        if not match_password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid username or password'
            )

        exp = datetime.now(timezone.utc) + timedelta(minutes=expires_in)

        payload = {
            'sub': self.user_login_email,
            'exp': exp
        }

        access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

        return { #Fazer um response model pra isso
            'access_token': access_token,
            'expires': exp.isoformat()
        }

