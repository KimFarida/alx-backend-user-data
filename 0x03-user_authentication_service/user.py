#!/usr/bin/env python3
"""User Module"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Coloumn, Integer, String
Base = declarative_base()

class User(Base):
    """The model for user data"""
    __tablename__ = 'users'

    id = Coloumn(Integer, primary_key=True)
    email = Coloumn(String(250), nullable=False)
    hashed_password = Coloumn(String(250), nullable=False)
    session_id = Coloumn(String(250), nullable=True)
