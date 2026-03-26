from sqlalchemy.orm import Session

from core.security import hash_password
from models.users import User, UserRole
from services.users import get_user_by_username
from models.teams import Team


def create_team(db: Session, player_1: str, player_2: str):
    """
    Créé une équipe de deux joueurs
    """
    is_player_1 = get_user_by_username(db, player_1)
    is_player_2 = get_user_by_username(db, player_2)
    if is_player_1 is None or is_player_2 is None:
        return None
    team = Team(player_1=player_1, player_2=player_2)
    db.add(team)
    db.commit()
    db.refresh(team)
    return team

def get_all_teams(db: Session):
    return db.query(Team).all()

def get_team_by_id(db: Session, team_id: int):
    return db.query(Team).filter(Team.id == team_id).first()