from typing import Optional
from datetime import date

from pydantic import BaseModel


class MailingListBase(BaseModel):
    email: str


# Properties to receive via API on creation
class MailingListCreate(MailingListBase):
    pass


# Properties to receive via API on update
class MailingListUpdate(MailingListBase):
    pass


class MailingListInDBBase(MailingListBase):
    id: Optional[int] = None
    enabled: Optional[bool] = True

    class Config:
        orm_mode = True


# Additional properties to return via API
class MailingList(MailingListInDBBase):
    pass


# Additional properties stored in DB
class MailingListInDB(MailingListInDBBase):
    pass
