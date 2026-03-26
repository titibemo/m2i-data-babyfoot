"""
Modèle SQLAlchemy représentant la table users.
"""

from enum import Enum

from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel, Field

from core.database import Base


# class UserRole(str, Enum):
#     """
#     Liste simple des rôles disponibles dans la démo.
#     """
#     ADMIN = "admin"
#     USER = "user"
#     GUEST = "guest"


class Team(Base):
    """
    Modèle ORM utilisateur.

    Cette classe décrit la structure de la table users.
    """

    __tablename__ = "team"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    player_1: Mapped[str] = mapped_column(String(50), nullable=False)
    player_2: Mapped[str] = mapped_column(String(255), nullable=False)


    

