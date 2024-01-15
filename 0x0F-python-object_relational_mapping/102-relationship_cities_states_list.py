#!/usr/bin/python3
'''Prints all City objects and their State in a database.
'''
import sys
from sqlalchemy import create_engine, and_, text, tuple_
from sqlalchemy.orm import sessionmaker, relationship

from relationship_state import Base, State
from relationship_city import City

