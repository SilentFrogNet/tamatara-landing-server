from uuid import uuid4
from sqlalchemy import Column, String, Text, Date
from sqlalchemy.dialects.postgresql import UUID

from .db import Base


class Newsletter(Base):
    __tablename__ = "lnd_newsletter"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    birth_date = Column(Date)
    user_type = Column(String)
    # other = Column(String)  # TODO: to change but don't know the field name
    message = Column(Text)
