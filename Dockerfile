# 1. Python'un resmi, hafif sürümünü baz alıyoruz
FROM python:3.9-slim

# 2. Konteyner içinde çalışma klasörünü ayarla
WORKDIR /code

# 3. Önce gereksinim dosyasını kopyala (Cache avantajı için)
COPY ./requirements.txt /code/requirements.txt

# 4. Kütüphaneleri kur
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 5. Tüm proje kodlarını konteyner içine kopyala
COPY ./app /code/app

# 6. Uygulamanın çalışacağı komutu belirle
# Cloud Run için port dinamik olabilir, o yüzden host 0.0.0.0 olmalı
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]