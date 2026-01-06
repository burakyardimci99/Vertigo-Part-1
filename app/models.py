from sqlalchemy import Column, String, DateTime
import uuid
from datetime import datetime, timezone
from .database import Base

class Clan(Base):
    # Veritabanındaki tablonun adı
    __tablename__ = "clans"

    # Sütun Tanımlamaları
    # id : Primary Key, UUID formatında. Heryeni kayıtta otomatik uuid4 üretir.
    id = Column(String, primary_key=True, default=lambda:str(uuid.uuid4()))

    # name : zorunlu alan, unique olmalı
    name = Column(String, nullable=False, index=True)

    # region : Bölge bilgisi
    region = Column(String, nullable=True)

    created_at = Column(DateTime, default=lambda:datetime.now(timezone.utc))

    