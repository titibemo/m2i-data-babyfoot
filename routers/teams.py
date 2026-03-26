
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from models.users import User, UserRole
from models.schemas import Teams, GetTeams
from db import user_db
from core.database import get_db
from services.teams import create_team, get_all_teams

from sqlalchemy.orm import Session

router = APIRouter(prefix="/teams", tags=["Teams"])

# créer une tema avec deux joueurs:
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_team(payload: Teams, db: Session = Depends(get_db)):
    team = create_team(db, payload.joueur1, payload.joueur2)
    return {"team créé": team}

@router.get("/", response_model=list[GetTeams])
async def get_teams(db: Session = Depends(get_db)):
    teams = get_all_teams(db)
    return teams