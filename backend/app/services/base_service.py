from datetime import datetime, timezone
from typing import Any, TypeVar

from sqlalchemy.orm import Session

T = TypeVar("T")


class BaseService:
    def __init__(self, db: Session):
        self.db = db

    @staticmethod
    def _to_dict(data: Any) -> dict[str, Any]:
        if hasattr(data, "model_dump"):
            return data.model_dump()
        if hasattr(data, "dict"):
            return data.dict()
        if isinstance(data, dict):
            return dict(data)
        return {}

    @staticmethod
    def _utcnow() -> datetime:
        return datetime.now(timezone.utc)

    def _commit_and_refresh(self, instance: T) -> T:
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def _flush_and_refresh(self, instance: T) -> T:
        self.db.add(instance)
        self.db.flush()
        self.db.refresh(instance)
        return instance

    def _get_or_raise(self, model_cls: type[T], item_id: int, message: str) -> T:
        item = self.db.get(model_cls, item_id)
        if not item:
            raise ValueError(message)
        return item