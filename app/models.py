from uuid import uuid4
from sqlalchemy import Column, String, Text, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import Boolean

from .db import Base


class Newsletter(Base):
    __tablename__ = "lnd_newsletter"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    birth_date = Column(Date)
    user_type = Column(String)
    category = Column(String)
    message = Column(Text)
    enabled = Column(Boolean, default=True)


class MailingList(Base):
    __tablename__ = "lnd_mailing_list"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    email = Column(String)
    enabled = Column(Boolean, default=True)
