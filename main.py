"""
Application principale FastAPI.
"""

from fastapi import FastAPI

from core.database import Base, engine, SessionLocal
from core.security import hash_password
from models.users import User, UserRole
from routers import auth, users, teams

app = FastAPI(
    title="FastAPI JWT Demo V5",
    description="Démo FastAPI avec inscription, login JWT, rôles et persistance SQLite via SQLAlchemy.",
    version="5.0.0",
)


def seed_demo_users() -> None:
    """
    Insère des utilisateurs de démonstration s'ils n'existent pas encore.

    Cela permet de tester immédiatement :
    - un administrateur
    - un utilisateur classique
    - un invité
    """
    demo_users = [
        ("alice", "azerty123", UserRole.ADMIN.value),
        ("bob", "azerty123", UserRole.USER.value),
        ("guest", "azerty123", UserRole.GUEST.value),
    ]

    db = SessionLocal()
    try:
        for username, raw_password, role in demo_users:
            existing = db.query(User).filter(User.username == username).first()
            if existing is None:
                db.add(
                    User(
                        username=username,
                        password_hash=hash_password(raw_password),
                        role=role,
                    )
                )
        db.commit()
    finally:
        db.close()


@app.on_event("startup")
def on_startup():
    """
    Au démarrage :
    - créer les tables définies par les modèles SQLAlchemy
    - insérer les comptes de démonstration si nécessaire
    """
    Base.metadata.create_all(bind=engine)
    seed_demo_users()


@app.get("/")
def root():
    return {
        "message": "Bienvenue sur la démo FastAPI JWT V5.",
        "docs": "/docs",
        "features": ["jwt", "sqlite", "sqlalchemy", "rbac"],
    }

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(teams.router)

