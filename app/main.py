from typing import Any, List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from . import actions, models, schemas
from .db import SessionLocal, engine

from .mailer import Mailer

# Create all tables in the database.
# Comment this out if you using migrations.
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST'],
    allow_headers=["*"],
)

mailer = Mailer()

# Dependency to get DB session.
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    return {"message": "Tamatara Landing Backend"}


# --------------------------------- #
#       NEWSLETTER                  #
# --------------------------------- #

@app.get("/newsletters", response_model=List[schemas.Newsletter], tags=["newsletters"])
def list_newsletters(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 100
) -> Any:
    newsletters = actions.newsletter.get_all(db=db, skip=skip, limit=limit)
    return newsletters


@app.post(
    "/newsletters",
    response_model=schemas.Newsletter,
    status_code=HTTP_201_CREATED,
    tags=["newsletters"],
)
def create_newsletter(
    *, db: Session = Depends(get_db), newsletter_in: schemas.NewsletterCreate
) -> Any:
    newsletter = actions.newsletter.create(db=db, obj_in=newsletter_in)
    mailer.send(newsletter.email)
    return newsletter


# @app.put(
#     "/newsletter/{id}",
#     response_model=schemas.Newsletter,
#     responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
#     tags=["newsletters"],
# )
# def update_newsletter(
#     *, db: Session = Depends(get_db), id: int, newsletter_in: schemas.NewsletterUpdate,
# ) -> Any:
#     newsletter = actions.newsletter.get(db=db, id=id)
#     if not newsletter:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Newsletter not found")
#     newsletter = actions.newsletter.update(db=db, db_obj=newsletter, obj_in=newsletter_in)
#     return newsletter


@app.get(
    "/newsletters/{id}",
    response_model=schemas.Newsletter,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["newsletters"],
)
def get_newsletter(*, db: Session = Depends(get_db), id: int) -> Any:
    newsletter = actions.newsletter.get(db=db, id=id)
    if not newsletter:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="Newsletter not found"
        )
    return newsletter


# @app.delete(
#     "/newsletter/{id}",
#     response_model=schemas.Newsletter,
#     responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
#     tags=["newsletters"],
# )
# def delete_newsletter(*, db: Session = Depends(get_db), id: int) -> Any:
#     newsletter = actions.newsletter.get(db=db, id=id)
#     if not newsletter:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Newsletter not found")
#     newsletter = actions.newsletter.remove(db=db, id=id)
#     return newsletter


@app.put(
    "/newsletters/{id}/optoup",
    response_model=schemas.Newsletter,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["newsletters"],
)
def optout_newsletter(*, db: Session = Depends(get_db), id: int) -> Any:
    return actions.newsletter.optout(db=db, id=id)


# --------------------------------- #
#       MAILING LIST                #
# --------------------------------- #

@app.get("/mailing_list", response_model=List[schemas.MailingList], tags=["mailing_list"])
def list_mailing_lists(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 100
) -> Any:
    mailing_lists = actions.mailing_list.get_all(db=db, skip=skip, limit=limit)
    return mailing_lists


@app.post(
    "/mailing_list",
    response_model=schemas.MailingList,
    status_code=HTTP_201_CREATED,
    tags=["mailing_list"],
)
def create_mailing_list(
    *, db: Session = Depends(get_db), mailing_list_in: schemas.MailingListCreate
) -> Any:
    mailing_list = actions.mailing_list.create(db=db, obj_in=mailing_list_in)
    mailer.send(mailing_list.email)
    return mailing_list


# @app.put(
#     "/mailing_list/{id}",
#     response_model=schemas.MailingList,
#     responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
#     tags=["mailing_list"],
# )
# def update_mailing_list(
#     *, db: Session = Depends(get_db), id: int, mailing_list_in: schemas.MailingListUpdate,
# ) -> Any:
#     mailing_list = actions.mailing_list.get(db=db, id=id)
#     if not mailing_list:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="MailingList not found")
#     mailing_list = actions.mailing_list.update(db=db, db_obj=mailing_list, obj_in=mailing_list_in)
#     return mailing_list


@app.get(
    "/mailing_list/{id}",
    response_model=schemas.MailingList,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["mailing_list"],
)
def get_mailing_list(*, db: Session = Depends(get_db), id: int) -> Any:
    mailing_list = actions.mailing_list.get(db=db, id=id)
    if not mailing_list:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="MailingList not found"
        )
    return mailing_list


# @app.delete(
#     "/mailing_list/{id}",
#     response_model=schemas.MailingList,
#     responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
#     tags=["mailing_list"],
# )
# def delete_mailing_list(*, db: Session = Depends(get_db), id: int) -> Any:
#     mailing_list = actions.mailing_list.get(db=db, id=id)
#     if not mailing_list:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="MailingList not found")
#     mailing_list = actions.mailing_list.remove(db=db, id=id)
#     return mailing_list


@app.put(
    "/mailing_list/{id}/optoup",
    response_model=schemas.MailingList,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["mailing_list"],
)
def optout_mailing_list(*, db: Session = Depends(get_db), id: int) -> Any:
    return actions.mailing_list.optout(db=db, id=id)
