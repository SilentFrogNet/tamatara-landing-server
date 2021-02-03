from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.sqltypes import Boolean

from .db import Base


class Newsletter(Base):
    __tablename__ = "lnd_newsletter"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    number = Column(String)
    user_type = Column(String)
    category = Column(String)
    enabled = Column(Boolean, default=True)


class MailingList(Base):
    __tablename__ = "lnd_mailing_list"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    enabled = Column(Boolean, default=True)
