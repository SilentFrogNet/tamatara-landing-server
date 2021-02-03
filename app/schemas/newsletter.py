from typing import Optional
from datetime import date

from pydantic import BaseModel


class NewsletterBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    number: str
    user_type: str
    category: str


# Properties to receive via API on creation
class NewsletterCreate(NewsletterBase):
    pass


# Properties to receive via API on update
class NewsletterUpdate(NewsletterBase):
    pass


class NewsletterInDBBase(NewsletterBase):
    id: Optional[int] = None
    enabled: Optional[bool] = True

    class Config:
        orm_mode = True


# Additional properties to return via API
class Newsletter(NewsletterInDBBase):
    pass


# Additional properties stored in DB
class NewsletterInDB(NewsletterInDBBase):
    pass
