from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path
from typing import Any

from sqlalchemy.orm import Session

from backend.app.core.config import config
from backend.app.models.auditoria_log import AuditoriaLog


class BackupService:
    BACKUP_DIR = Path(__file__).resolve().parents[2] / "data" / "backups"
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    @classmethod
    def _get_database_path(cls) -> Path:
        database_url = config.DATABASE_URL
        if not database_url.startswith("sqlite:///"):
            raise ValueError("Backup suporta apenas bancos SQLite")
        return Path(database_url.replace("sqlite:///", "", 1)).resolve()

    @classmethod
    def create_backup(cls, db: Session, created_by: int | None = None) -> dict[str, Any]:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = cls.BACKUP_DIR / f"backup_{timestamp}.sqlite"
        source_db = cls._get_database_path()
        if not source_db.exists():
            raise FileNotFoundError(f"Banco de dados não encontrado em {source_db}")

        shutil.copy2(source_db, backup_path)
        success = backup_path.exists()
        cls._log_event(db, created_by, "backup_criado" if success else "backup_falhou", success)
        return {
            "success": success,
            "backup_id": backup_path.stem,
            "file_name": backup_path.name,
            "path": str(backup_path),
        }

    @classmethod
    def restore_backup(cls, db: Session, backup_id: str, restored_by: int | None = None) -> dict[str, Any]:
        backup_path = cls.BACKUP_DIR / f"{backup_id}.sqlite"
        if not backup_path.exists():
            raise ValueError("Backup não encontrado")

        target_db_path = cls._get_database_path()
        target_db_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(backup_path, target_db_path)

        cls._log_event(db, restored_by, "backup_restaurado", True)
        return {
            "success": True,
            "backup_id": backup_id,
            "restored_file": backup_path.name,
        }

    @classmethod
    def _log_event(cls, db: Session, user_id: int | None, action: str, success: bool) -> None:
        db.add(
            AuditoriaLog(
                funcionario_id=user_id,
                acao=action,
                entidade="backup",
            )
        )
        db.commit()

    @classmethod
    def list_backups(cls) -> list[dict[str, Any]]:
        return [
            {
                "backup_id": path.stem,
                "file_name": path.name,
                "created_at": datetime.fromtimestamp(path.stat().st_mtime),
                "path": str(path),
            }
            for path in sorted(cls.BACKUP_DIR.glob("backup_*.sqlite"), key=lambda item: item.stat().st_mtime, reverse=True)
        ]        