from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

ENGINE = create_engine("sqlite:///hp_qs.db", echo=False)
sqla_session = scoped_session(sessionmaker(bind=ENGINE, autocommit=False, autoflush=False))

Base = declarative_base()
Base.query = sqla_session.query_property()


# Classes

class Question(Base):

    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    content = Column(String(140))
    category = Column(Integer, ForeignKey("categories.id"))


class Category(Base):

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    description = Column(String(256))
    parent = Column(Integer, ForeignKey("categories.id"), nullable=True)


class Answer(Base):

    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)
    solution = Column(Integer, ForeignKey("solutions.id"))
    question = Column(Integer, ForeignKey("questions.id"))
    answer = Column(Boolean)


class Solution(Base):

    __tablename__ = "solutions"

    id = Column(Integer, primary_key=True)
    content = Column(String(140))
    category = Column(Integer, ForeignKey="categories.id")
    color_coding = Column(Integer)


# Functions

def create_db():
    """Recreates the database."""

    Base.metadata.create_all(ENGINE)






