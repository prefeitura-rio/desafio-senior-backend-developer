from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.dependencies import get_db, get_current_user, token_verifier
from app.db.models.user import User
from app.routes.credit.controllers.credit_user_controller import (
        CreditUserController
)
from app.routes.credit.schemas.credit_schema import CreditRecharge, CreditResponse

router = APIRouter(
    prefix="/credit",
    tags=["credit"],
    dependencies=[Depends(token_verifier)]
)


@router.get("/", response_model=CreditResponse)
def get_credit(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return CreditUserController(db, user).get()


@router.put("/recharge") #, response_model=UserSchema
def put_credit(
    credit_user: CreditRecharge,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return CreditUserController(db, user).put(credit_user.amount)
        #Add Response com content e status code