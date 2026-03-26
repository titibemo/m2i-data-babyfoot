"""
Schémas Pydantic utilisés pour valider les entrées/sorties de l'API.
"""

from pydantic import BaseModel, Field

################################################### USERS
class UserRegister(BaseModel):
    """
    Données attendues pour l'inscription d'un nouvel utilisateur.
    """
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6, max_length=128)


class UserLogin(BaseModel):
    """
    Données attendues pour la connexion.
    """
    username: str
    password: str


class UserPublic(BaseModel):
    """
    Représentation publique d'un utilisateur.
    Aucun mot de passe ni hash ne doit sortir ici.
    """
    id: int
    username: str
    role: str

    model_config = {"from_attributes": True}
    
class GetUser(BaseModel):
    """
    Représentation publique d'un utilisateur.
    Aucun mot de passe ni hash ne doit sortir ici.
    """
    username: str

    model_config = {"from_attributes": True}

################################################### TOKEN

class TokenResponse(BaseModel):
    """
    Réponse renvoyée après un login ou un refresh.
    """
    access_token: str
    token_type: str = "bearer"


class MessageResponse(BaseModel):
    """
    Petit schéma utilitaire pour les réponses simples.
    """
    message: str


class LoginResponse(TokenResponse):
    """
    Variante un peu plus riche de la réponse de login, pour que l'utilisateur
    sache immédiatement quel compte il vient d'authentifier.
    """
    user: UserPublic
    expires_in: int


################################################### teams

# une team est composé de minimum deux joueurs
class Teams(BaseModel):
    joueur1: str
    joueur2: str
    name: str
    
class GetTeams(BaseModel):
    player_1: str
    player_2: str
    name: str
    
    model_config = {"from_attributes": True}