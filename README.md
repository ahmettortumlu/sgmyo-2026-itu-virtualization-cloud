# sgmyo-2026-itu-virtualization-cloud

Dockerfile içerisinde;
* python:3.12-slim docker image'inden image oluşturulmaya başlanmalı,
* /app dizininde çalışmaya başla,
* requirements.txt dosyası, /app/requirements.txt dosyası içine kopyalanmalı,
* pip ile requirements.txt dosyasında tanımlanan kütüphaneleri yükle,
* app.py dosyasını /app/app.py altına kopyala,
* 5000 portunu expose et,
* "python app.py" komutu ile docker image'ini ayağa kaldır.

Docker container'ının 
* imajı biraz önce oluşturduğun docker image'i olsun,
* container'ın 5000 portunu lokal bilgisayarınızın 5000 portuna bağla,
* okul-net networkünde kaldır container'ını
* aşağıdaki ortam değişkenlerinden bir environment variable dosyası oluştur ve buradan al ortam değişkenlerini:
      DB_HOST: db
      DB_NAME: ogrenci_db
      DB_USER: user
      DB_PASSWORD: password
