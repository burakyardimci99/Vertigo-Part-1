from fastapi import FastAPI
from . import models, database
from .routers import clan

# 1. Tabloları Oluştur
# Uygulama başlarken veritabanına bakar, tablolar yoksa oluşturur.
models.Base.metadata.create_all(bind=database.engine)

# 2. Uygulamayı Başlat
app = FastAPI(
    title="Vertigo Games Clan API",
    description="Klan yönetimi için basit bir REST API",
    version="1.0.0"
)

# 3. Router'ları Ekle
# Yazdığımız clan.py dosyasını ana uygulamaya bağlıyoruz.
app.include_router(clan.router)

# Basit bir hoşgeldin mesajı (Opsiyonel)
@app.get("/")
def read_root():
    return {"message": "Vertigo Games Clan API'ye Hoşgeldiniz! Dokümantasyon için /docs adresine gidin."}