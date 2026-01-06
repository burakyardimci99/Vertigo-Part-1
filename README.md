# Vertigo Games - Data Engineering Case Study

Bu repo, Vertigo Games Data Engineer pozisyonu için hazırlanan teknik vaka çalışmasının (Case Study) çözümünü içermektedir. Proje, ölçeklenebilir bir Backend API servisi ve kapsamlı veri mühendisliği süreçlerini kapsar.

## 🚀 Proje Özellikleri

Proje, **Clean Code** prensiplerine sadık kalınarak, modüler ve konteynerize edilmiş bir yapıda geliştirilmiştir.

### Tech Stack

* **Dil:** Python 3.9
* **Framework:** FastAPI (Yüksek performanslı, async API)
* **Veritabanı:** PostgreSQL (Cloud SQL uyumlu) / SQLite (Local geliştirme için)
* **ORM:** SQLAlchemy
* **Data Validation:** Pydantic
* **Containerization:** Docker
* **Data Processing:** Pandas (Veri temizliği ve seed işlemleri için)

---

## 🛠️ Kurulum ve Çalıştırma

Projeyi lokalinizde çalıştırmak için aşağıdaki adımları izleyebilirsiniz.

### 1. Docker ile Çalıştırma (Önerilen)

En temiz ve hızlı kurulum yöntemidir.

```bash
# 1. İmajı build edin
docker build -t vertigo-clan-api .

# 2. Konteyneri başlatın
docker run -p 8080:8080 vertigo-clan-api
```

Tarayıcınızda `http://localhost:8080/docs` adresine giderek Swagger UI üzerinden API'yi test edebilirsiniz.

### 2. Manuel Kurulum (Python venv)

```
# Sanal ortamı oluşturun ve aktif edin
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Uygulamayı başlatın
uvicorn app.main:app --reload
```

---

## 🌱 Veri Tohumlama (Data Seeding)

Proje, `clan_sample_data.csv` dosyasındaki örnek verileri veritabanına otomatik olarak yükleyen bir **ETL scripti** içerir.

Scriptin Özellikleri:

* **Veri Temizliği:** İsmi (`name`) boş olan hatalı kayıtları filtreler.
* **Zenginleştirme:** Eksik `id` (UUID) değerlerini üretir.
* **Formatlama:** Tarih formatlarını UTC standardına dönüştürür.

Verileri yüklemek için:

```
python seed.py
```

---

## 📂 Proje Yapısı

Kod tabanı, "Separation of Concerns" ilkesine göre modüler parçalara ayrılmıştır:

```
├── app/
│   ├── routers/      # API Endpoint tanımları (Clan işlemleri)
│   ├── models.py     # SQLAlchemy veritabanı modelleri
│   ├── schemas.py    # Pydantic veri şemaları ve validasyon
│   ├── database.py   # Veritabanı bağlantı ayarları
│   └── main.py       # Uygulama giriş noktası
├── Dockerfile        # Konteyner konfigürasyonu
├── seed.py           # Veri yükleme ve temizleme scripti
└── requirements.txt  # Proje bağımlılıkları
```

---

## 📊 API Endpointleri

* **POST /clans:** Yeni klan oluşturur (Min. 3 karakter isim kontrolü).
* **GET /clans:** Klanları listeler. `?name=...` parametresi ile "contains" araması yapılabilir.
* **DELETE /clans/{id}:** ID'ye göre klan siler.

---

**Author:** Ayberk Burak Yardımcı
**Version:** v1.0
