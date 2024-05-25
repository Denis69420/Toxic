from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class ServerConfig(Base):
    __tablename__ = 'server_configs'

    guild_id = Column(String, primary_key=True)
    prefix = Column(String, default='!')
    welcome_message = Column(String, default='Welcome to the server!')
    welcome_channel_id = Column(String)  # Store channel ID for welcome messages
    verification_enabled = Column(Boolean, default=False)


class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True)
    channel_id = Column(Integer, unique=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    reason = Column(String, nullable=False)

DATABASE_URL = 'sqlite:///bot_config.db'
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
