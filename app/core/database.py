from typing import Annotated, Any, Generator
from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import Session
import os


sqlite_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.db")
engine = create_engine("sqlite:///" + sqlite_filepath, connect_args={"check_same_thread": False}, echo=True )

def get_session()-> Generator[Session, Any, None]:
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
