from typing import Generic, TypeVar

from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    def __init__(self, model_cls: type[ModelType], db: Session):
        self.model_cls = model_cls
        self.db = db

    def get_all(self) -> list[ModelType]:
        return self.db.query(self.model_cls).all()

    def get_by_id(self, item_id: int) -> ModelType | None:
        return self.db.get(self.model_cls, item_id)

    def add(self, item: ModelType) -> ModelType:
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def update(self, item: ModelType) -> ModelType:
        self.db.commit()
        self.db.refresh(item)
        return item

    def delete(self, item: ModelType) -> ModelType:
        self.db.delete(item)
        self.db.commit()
        return item