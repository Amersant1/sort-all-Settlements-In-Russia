from sqlalchemy import *

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging






# database = 'horoscope'
connection_string = "sqlite:///base.db"

Base = declarative_base()

###### LOGGING ######
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='app.log', filemode='a', format=LOG_FORMAT)
logger = logging.getLogger()


engine = create_engine(
    url=connection_string
)

Session = sessionmaker(engine)()
