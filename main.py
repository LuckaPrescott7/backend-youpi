from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, schemas, crud, auth
from database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mon API Backend", description="API pour contact, blog, newsletter, admin")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/token", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_admin_user_by_username(db, form_data.username)
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Identifiants incorrects")
    token = auth.create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/admin/create")
def register_admin(data: schemas.AdminCreate, db: Session = Depends(get_db)):
    return crud.create_admin_user(db, data.username, data.password)

@app.post("/contact")
def create_contact(data: schemas.ContactCreate, db: Session = Depends(get_db)):
    return crud.create_contact(db, data.name, data.email, data.message)

@app.post("/newsletter")
def subscribe(data: schemas.NewsletterCreate, db: Session = Depends(get_db)):
    return crud.subscribe_newsletter(db, data.email)

@app.post("/blog")
def add_blog(data: schemas.BlogPostCreate, db: Session = Depends(get_db)):
    return crud.create_blog_post(db, data.title, data.content)

@app.get("/blog", response_model=list[schemas.BlogPostRead])
def get_blogs(db: Session = Depends(get_db)):
    return crud.get_all_blog_posts(db)

@app.get("/")
def home():
    return {"message": "Bienvenue sur l’API Backend 🎉"}
