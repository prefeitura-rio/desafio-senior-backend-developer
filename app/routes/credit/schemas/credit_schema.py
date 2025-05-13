from pydantic import BaseModel


class CreditRecharge(BaseModel):
    amount: float


class CreditResponse(BaseModel):
    amount: float
    message: str
