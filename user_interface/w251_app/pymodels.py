from sqlalchemy import Boolean, Column, ForeignKey, Numeric, Integer, String
from sqlalchemy_utils import URLType
from sqlalchemy.orm import relationship

from database import Base

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    quantity = Column(Numeric(10, 2))

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    recipe_name = Column(String)
    used_ingredients = Column(String)
    missing_ingredients = Column(String)
    image = Column(URLType)
