from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

Base = declarative_base(metadata=MetaData(naming_convention=convention))

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    character_name = Column(String)
    
    def __repr__(self):
        return f"<Role(character_name='{self.character_name}')>"

class Audition(Base):
    __tablename__ = 'auditions'
    id = Column(Integer, primary_key=True)
    actor = Column(String)
    location = Column(String)
    phone = Column(Integer)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship("Role", backref=backref("auditions", cascade="all, delete-orphan"))
    
    def __repr__(self):
        return f"<Audition(actor='{self.actor}', location='{self.location}', hired='{self.hired}')>"
    
    def call_back(self):
        self.hired = True

    # Rest of the Role class methods remain unchanged

# Replace 'sqlite:///path/to/your/dbfile.db' with your database connection string
engine = create_engine('sqlite:///path/to/your/dbfile.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
