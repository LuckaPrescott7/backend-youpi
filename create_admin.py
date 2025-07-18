from database import SessionLocal
import crud

crud.create_admin_user(SessionLocal(), "admin", "motdepasse123")
