from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.core.security import get_current_user

from app.schemas.dashboard.dashboard_schema import (
    DashboardSummaryResponse,
    DashboardChartsResponse,
    ProfileSummaryResponse,
    AISuggestion,
)

from app.services.dashboard.dashboard_service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/summary",
    response_model=DashboardSummaryResponse
)
def get_dashboard_summary(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return DashboardService.get_dashboard_summary(
        db=db,
        user_id=current_user.user_id
    )


@router.get(
    "/ai-suggestions",
    response_model=List[AISuggestion]
)
def get_ai_suggestions(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return DashboardService.get_ai_suggestions(
        db=db,
        user_id=current_user.user_id
    )


@router.get(
    "/charts",
    response_model=DashboardChartsResponse
)
def get_dashboard_charts(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return DashboardService.get_chart_data(
        db=db,
        user_id=current_user.user_id
    )


@router.get(
    "/profile-summary",
    response_model=ProfileSummaryResponse
)
def get_profile_summary(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return DashboardService.get_profile_summary(
        db=db,
        user_id=current_user.user_id
    )