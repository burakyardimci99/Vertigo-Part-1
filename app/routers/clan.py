from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas, database

# 1 Router Tanımı
router = APIRouter(
    prefix = "/clans",
    tags = ["clans"]
)

# 2 Dependency 
get_db = database.get_db

# ----------------------------------------------------------------
# ENDPOINT 1: KLAN OLUŞTUR (CREATE)
# ----------------------------------------------------------------
@router.post("/", response_model = schemas.ClanResponse)
def create_clan(clan: schemas.ClanCreate, db: Session = Depends(get_db)):
    """
    Yeni bir clan oluşturur.
    - **name** : Clan adı öin 3 karater
    - **region** : Bölge opsiyonel
    """
    
    
    # Aynı isimde clan var mı kontrol et
    existing_clan = db.query(models.Clan).filter(models.Clan.name == clan.name).first()
    if existing_clan:
        raise HTTPException(status_code=400, detail="Bu isimde bir clan mevcut")


    # Veritabanı modelini hazırla (Schema -> Model dönüşümü)
    # **clan.dict() ifadesi, gelen veriyi (name="X", region="Y") parçalayıp modele aktarır.APIRouter
    db_clan = models.Clan(**clan.dict())

    db.add(db_clan)
    db.commit()
    db.refresh(db_clan)
    
    return db_clan

# ----------------------------------------------------------------
# ENDPOINT 2: KLANLARI LİSTELE VE ARA (LIST & SEARCH)
# ----------------------------------------------------------------
@router.get("/", response_model = List[schemas.ClanResponse])
def read_clans(
    name : Optional[str] = Query(None, min_length = 3, description="Aranacak klan adı (en az 3 harf)"),
    skip : int = 0,
    limit : int = 100,
    db : Session = Depends(get_db)
):

    """
    Clanları listeler, eğer 'name' parametresi verilirse isme göre arama yapar.
    """

    # Temel sorguyu başlatma
    query = db.query(models.Clan)

    # name parametresi varsa, sorguya filtre ekle
    if name:
        # ilike : case-insensitive
        # %name% : contains
        query = query.filter(models.Clan.name.ilike(f"%{name}%"))

    # pagination ve retrieve
    clans = query.offset(skip).limit(limit).all()

    return clans

# ----------------------------------------------------------------
# ENDPOINT 3: KLAN SİL (DELETE)
# ----------------------------------------------------------------
@router.delete("/{clan_id}")
def delete_clan(clan_id : str, db : Session = Depends(get_db)):
    """
    Belirli bir clan'ı siler.
    """
    
    # clanı bulma
    clan = db.query(models.Clan).filter(models.Clan.id == clan_id).first()
    if clan is None:
        raise HTTPException(status_code=404, detail="Bu id'ye sahip bir clan bulunamadı")

    # clanı silme
    db.delete(clan)
    db.commit()
    
    return {"message": "Clan başarıyla silindi", "id": clan_id}
    