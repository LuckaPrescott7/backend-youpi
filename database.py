from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Crée un dossier 'db' si non existant
if not os.path.exists("./db"):
    os.makedirs("./db")

# Chemin absolu vers le fichier .db
SQLALCHEMY_DATABASE_URL = "sqlite:///./db/youpi.db"

# Configuration SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
