from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.db import SessionLocal
from app.routes.users.controllers.user_auth_controller import (
        UserAuthController
)

oauth_scheme = OAuth2PasswordBearer(tokenUrl='/user/login')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def token_verifier(
    db_session: Session = Depends(get_db),
    token=Depends(oauth_scheme)
):
    return (
        UserAuthController(
            db_session=db_session
        ).verify_token(access_token=token)
    )


def get_current_user(
        db_session: Session = Depends(get_db),
        token=Depends(oauth_scheme)
):
    return (
        UserAuthController(
            db_session=db_session
        ).get_user_token(access_token=token)
    )
