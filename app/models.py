from sqlalchemy import Column, String, Text, Date, Integer
from sqlalchemy.sql.sqltypes import Boolean

from .db import Base


class Newsletter(Base):
    __tablename__ = "newsletter"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    birth_date = Column(Date)
    user_type = Column(String)
    category = Column(String)
    message = Column(Text)
    enabled = Column(Boolean, default=True)


class MailingList(Base):
    __tablename__ = "mailing_list"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    enabled = Column(Boolean, default=True)
