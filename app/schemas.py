from typing import Optional
from datetime import date

from pydantic import BaseModel, UUID4


class HTTPError(BaseModel):
    message: str


class NewsletterBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    birth_date: date
    user_type: str
    category: str
    message: str


# Properties to receive via API on creation
class NewsletterCreate(NewsletterBase):
    pass


# Properties to receive via API on update
class NewsletterUpdate(NewsletterBase):
    pass


class NewsletterInDBBase(NewsletterBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Newsletter(NewsletterInDBBase):
    pass


# Additional properties stored in DB
class NewsletterInDB(NewsletterInDBBase):
    pass
