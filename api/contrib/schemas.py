from datetime import datetime
from typing import Annotated

from pydantic import UUID4, BaseModel, Field


class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributes = True


class OutMixin(BaseSchema):
    id: Annotated[UUID4, Field(description='identificador')]
    created_at: Annotated[datetime, Field(description='Data de criação')]
