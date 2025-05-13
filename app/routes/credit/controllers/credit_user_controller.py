from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.db.models.user import User
from app.db.models.credit_user import CreditUser


class CreditUserController():
    
    """Add docstring aqui e nas funções"""
    
    def __init__(self, db_session: Session, user: User):
        self.db_session = db_session
        self.user_id = user.id

    def get(self):
        credit = CreditUser.get_credit_by_user_id(
                self.db_session,
                self.user_id
            )
        if not credit:
            credit = 0.0
        return JSONResponse(
            status_code=200,
            content={"message": f"Credit value is R${credit}"}
        )

    def put(self, amount: float):
        """"""
        current_credit = CreditUser.get_credit_by_user_id(
            self.db_session,
            self.user_id
        )
        if not current_credit:
            credit = CreditUser.create_credit(
                self.db_session,
                self.user_id,
                amount
            )
            return JSONResponse(
                status_code=200,
                content={"message": f"Credit valueeeee is R${credit}"}
            )

        print("current_credit", current_credit.credit_value)
        new_credit = current_credit.credit_value + amount

        credit = CreditUser.update_credit(
            self.db_session,
            self.user_id,
            new_credit
        )
        return JSONResponse(
            status_code=200,
            content={"message": f"Credit value is R${credit.credit_value}"}
        )
    
    
