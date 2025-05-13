from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.dependencies import token_verifier
from app.routes.users.controllers.user_controller import UserController
from app.routes.files.controllers.files_controller import FilesController
from app.routes.files.schemas.files_schema import (
        FileResponse,
        FileUpload,
        GetFiles,
        GetFileResponse
)

router = APIRouter(
    prefix="/files",
    tags=["files"],
    dependencies=[Depends(token_verifier)]
)


@router.post("/upload") #response_model=FileResponse
def post_file(file: UploadFile = File(...)):
    return FilesController.post(file)

    #return UserController(db).post(file)
        #Add Response com content e status code

@router.get("/") #  response_model=GetFileResponse
def get_files():  # files: GetFiles
    return FilesController.get()
        #Add Response com content e status code
