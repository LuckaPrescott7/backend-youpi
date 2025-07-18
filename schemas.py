from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class AdminCreate(BaseModel):
    username: str
    password: str

class ContactCreate(BaseModel):
    name: str
    email: str
    message: str

class NewsletterCreate(BaseModel):
    email: str

class BlogPostCreate(BaseModel):
    title: str
    content: str

class BlogPostRead(BlogPostCreate):
    id: int
    created_at: str

    class Config:
        orm_mode = True
