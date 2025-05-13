from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.routes.users.controllers.user_controller import UserController
from app.routes.users.controllers.user_login_controller import UserLoginController
from app.routes.users.schemas.user_schema import UserCreate, UserLogin, UserSchema

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.post("/register", response_model=UserSchema)
def post_user(user: UserCreate, db: Session = Depends(get_db)):
    #setar o schema aqui
    return UserController(user.email, db).post(user)
        #Add Response com content e status code


@router.post("/login") #add response model
def user_login(
        request_form_user: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
        ):
    user_login = UserLogin(
        email=request_form_user.username,
        password=request_form_user.password
    )

    #setar o schema aqui
    return UserLoginController(db, user_login).post()
        #Add Response com content e status code

""" 

@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
 """
""" 
@app.post("/users/", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserController().get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@app.get("/users/", response_model=list[UserSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = UserController.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = UserController.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user """
