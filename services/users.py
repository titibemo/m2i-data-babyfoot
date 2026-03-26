from sqlalchemy.orm import Session

from core.security import hash_password
from models.users import User, UserRole



def create_user(db: Session, username: str, password: str, role: str = UserRole.USER.value):
    """
    Crée un utilisateur en base.

    Le mot de passe est hashé avant l'insertion.
    Le rôle par défaut d'un utilisateur inscrit est 'user'.
    """
    password_hash = hash_password(password)

    user = User(
        username=username,
        password_hash=password_hash,
        role=role,
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_username(db: Session, username: str):
    """
    Recherche un utilisateur par son nom d'utilisateur.
    Retourne un objet User ou None.
    """
    return db.query(User).filter(User.username == username).first()

# supprimer un joueur
def delete_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
    
# modifier un joueur
def update_user_by_id(db: Session, user_id: int, username: str, password: str):
    user = db.query(User).filter(User.id == user_id).first()
    user.username = username
    user.password_hash = hash_password(password)
    db.commit()
