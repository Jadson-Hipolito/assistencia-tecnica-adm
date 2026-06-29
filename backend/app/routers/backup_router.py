from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.core.dependencies import get_db
from backend.app.core.dependencies_auth import get_current_user, require_roles
from backend.app.services.backup_service import BackupService

router = APIRouter(prefix="/backup", tags=["Backup"])


@router.post("/manual")
def manual_backup(
    db: Session = Depends(get_db),
    payload: dict = Depends(require_roles("admin")),
):
    try:
        result = BackupService.create_backup(db, created_by=int(payload.get("sub", 0)))
        return result
    except Exception as exc:  # pragma: no cover - defensive path
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc)) from exc


@router.post("/restore/{backup_id}")
def restore_backup(
    backup_id: str,
    db: Session = Depends(get_db),
    payload: dict = Depends(require_roles("admin")),
):
    try:
        return BackupService.restore_backup(db, backup_id, restored_by=int(payload.get("sub", 0)))
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc)) from exc


@router.get("/")
def list_backups():
    return BackupService.list_backups()