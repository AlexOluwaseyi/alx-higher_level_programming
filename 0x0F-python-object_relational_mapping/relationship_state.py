#!/usr/bin/python3
"""
python file that contains the class definition of a
State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import City

Base = declarative_base()


class State(Base):
    """State class"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state",
                          cascade="all, delete-orphan")

    # Establish a relationship between City and State
    cities = relationship("City", back_populates="state",
                          cascade="all, delete-orphan")
