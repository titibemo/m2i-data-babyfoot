"""
Modèle SQLAlchemy représentant la table users.
"""

from enum import Enum

from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel, Field

from core.database import Base


class UserRole(str, Enum):
    """
    Liste simple des rôles disponibles dans la démo.
    """
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


class User(Base):
    """
    Modèle ORM utilisateur.

    Cette classe décrit la structure de la table users.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(20), default=UserRole.USER.value, nullable=False)

    

