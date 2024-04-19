#!/usr/bin/python3
"""
This script defines City Class and an instance Base
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Represents a City Class"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
