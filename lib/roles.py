from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    character_name = Column(String)
    
    def __repr__(self):
        return f"<Role(character_name='{self.character_name}')>"
    
    # Rest of the methods for the Role class (actors, locations, lead, understudy)
