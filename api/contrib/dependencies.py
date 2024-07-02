from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.configs.database import get_session

data_base_dependecy = Annotated[AsyncSession, Depends(get_session)]
