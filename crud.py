from sqlalchemy.orm import Session
import models, auth

def get_admin_user_by_username(db: Session, username: str):
    return db.query(models.AdminUser).filter(models.AdminUser.username == username).first()

def create_admin_user(db: Session, username: str, password: str):
    hashed_pw = auth.hash_password(password)
    user = models.AdminUser(username=username, hashed_password=hashed_pw)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_contact(db: Session, name: str, email: str, message: str):
    obj = models.Contact(name=name, email=email, message=message)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def subscribe_newsletter(db: Session, email: str):
    entry = models.Newsletter(email=email)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

def create_blog_post(db: Session, title: str, content: str):
    post = models.BlogPost(title=title, content=content)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_all_blog_posts(db: Session):
    return db.query(models.BlogPost).order_by(models.BlogPost.created_at.desc()).all()
