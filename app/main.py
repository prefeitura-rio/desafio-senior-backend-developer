from fastapi import FastAPI

from app.db import init_db
from app.db.models import user
from app.db.models import credit_user
from app.routes.credit import credit_viewer
from app.routes.users import users_viewer
from app.routes.files import files_viewer
from app.routes.users.controllers.user_controller import UserController
from app.routes.files.controllers.files_controller import FilesController
from app.routes.users.schemas.user_schema import UserSchema, UserCreate


app = FastAPI()
#app = FastAPI(dependencies=[Depends(get_query_token)])


#init_db()  #aparentemente isso aqui pode ser removido depois do almebic


@app.get('/health')
def health_check():
    return "ok, its health"


app.include_router(users_viewer.router)
app.include_router(files_viewer.router)
app.include_router(credit_viewer.router)
