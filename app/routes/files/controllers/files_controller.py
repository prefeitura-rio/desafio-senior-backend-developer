import os

from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException

from app.db.models.user import User
#from app.users.schemas.user_schema import UserCreate


class FilesController():
    """Add docstring aqui e nas funções"""
    
    """ def __init__():
        pass """

    def post(file):
        """"""
        with open(f'uploads/{file.filename}', "wb") as f:
            f.write(file.file.read())
        return ({"message": f"File '{file.filename} saved successfully"})
    
    def get():
        print("FILES", os.listdir("uploads"))
        files = [  # melhorar isso aqui, deixar mais legivel
            file for file in os.listdir("uploads")
            if os.path.isfile(os.path.join("uploads", file))]
        return files
