
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from models.users import User, UserRole
from models.schemas import Teams, GetTeams
from db import user_db
from core.database import get_db
from services.teams import create_team, get_all_teams, get_team_by_id

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

# get team by id
@router.get("/{team_id}", response_model=GetTeams)
async def get_team(team_id: int, db: Session = Depends(get_db)):
    team = get_team_by_id(db, team_id)
    if team is None:
        raise HTTPException(status_code=404, detail=f"Équipe {team_id} non trouvée")
    return team

# update team by id
@router.put("/{team_id}", response_model=GetTeams)
async def update_team(team_id: int, payload: Teams, db: Session = Depends(get_db)):
    team = get_team_by_id(db, team_id)
    if team is None:
        raise HTTPException(status_code=404, detail=f"Équipe {team_id} non trouvée")
    team.player_1 = payload.joueur1
    team.player_2 = payload.joueur2
    db.commit()
    return team

# delete team by id
@router.delete("/{team_id}", response_model=GetTeams)
async def delete_team(team_id: int, db: Session = Depends(get_db)):
    team = get_team_by_id(db, team_id)
    if team is None:
        raise HTTPException(status_code=404, detail=f"Équipe {team_id} non trouvée")
    db.delete(team)
    db.commit()
    return team