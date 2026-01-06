import pandas as pd 
import uuid
from datetime import datetime, timezone
from app.database import SessionLocal
from app.models import Clan

def seed_data():
    print("🌱 Veri tohumlama işlemi başlıyor...")

    # 1 CSV dosyasını oku
    try:
        df = pd.read_csv("clan_sample_data.csv")
    except FileNotFoundError:
        print("CSV dosyası bulunamadı")
        return

    print(f"📄 Toplam satır sayısı: {len(df)}")
    
    # 2 Veri temizliği
    df = df.dropna(subset=["name"])

    # 3 Veri tabanı oturumu aç
    db = SessionLocal()
    
    success_count = 0

    # 4 Satır satır işe ve kaydet
    for _, row in df.iterrows():
        try:
            # ID üret, CSV'de yok
            clan_id = str(uuid.uuid4())

            # tarih düzenleme tarih yoksa şu anı al
            if pd.isna(row["created_at"]):
                created_at = datetime.now(timezone.utc)
            else:
                # stringi datetime çevir ve utc verisini ekle
                created_at = pd.to_datetime(row["created_at"]).replace(tzinfo=timezone.utc)
            

            # veritabanı modeline çevir
            clan = Clan(
                id=clan_id,
                name=row["name"],
                region=row["region"],
                created_at=created_at
            )

            # veritabanına kaydet
            db.add(clan)
            success_count +=1
        
        except Exception as e:
            print("Veri kaydetme hatası:", str(e))
            
    
    try:
        db.commit()
        print(f"{success_count} veri başarıyla kaydedildi.")
    except Exception as e:
        db.rollback()
        print("Veritabanı kaydetme hatası:", str(e))
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()