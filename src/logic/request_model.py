from typing import Literal, Optional
from langserve import CustomUserType


class RequestLogic(CustomUserType):
    filter: Optional[Literal["genere", "actor", "title", "desc", "all"]]
    search: str
