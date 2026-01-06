from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# 1 Base Schema (Ortak Özellikler)
class ClanBase(BaseModel):
    name: str = Field(..., min_length=3, description="Klan adı en az 3 harf olmalı")
    region : Optional[str] = None

# 2 Create Schema (Kullanıcıdan veri alınırken), kullanıcı sadece name ve region gönderir
class ClanCreate(ClanBase):
    pass

# 3 Response Schema (Kullanıcıya veri gönderirken), kullanıcıya id ve created_at da gönderir
class ClanResponse(ClanBase):
    id: str
    created_at: datetime
    
    # Bu ayar, Pydantic'in SQLAlchemy modellerini (ORM) okumasını sağlar.
    class Config:
        orm_mode = True
        