from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1 Veritabanı adresi
# Şu anlık projenin olduğu klasörde 'clans.db' diye bir dosya oluşturacak.
# ilerde PostgreSQL bağlayacağız
SQLALCHEMY_DATABASE_URL = "sqlite:///./clans.db"

# 2 engine olşturma (veri tabanını çalıştırır bağlantıyı sağlar)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3 Session olşturma
# Veritabanı ile her işlem (ekleme, silme) için bir 'Session' açacağız.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4 Base sınıfı
# Veritabanı modellerimizi (tabloları) bu sınıftan türeteceğiz. 
Base = declarative_base()

# 5 Dependency
# Her API isteğinde veritabanı oturumu açıp, iş bitince kapatan fonksiyon.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

