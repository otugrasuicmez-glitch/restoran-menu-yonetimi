# 🍽️ Restoran Menü Yönetimi Sistemi

**Streamlit ile geliştirilmiş modern ve sade bir dijital menü yönetim uygulaması**
Bu proje, restoranların ürünlerini görselleriyle birlikte dijital ortamda yönetebilmesi için geliştirilmiştir.

---

## 📋 Proje Açıklaması

Bu uygulama; restoran sahiplerinin menülerini **kolayca oluşturmasını, güncellemesini ve yönetmesini** sağlayan web tabanlı bir sistemdir.
Ürünler görselleriyle birlikte listelenir, yeni ürün eklenebilir ve mevcut ürünler silinebilir.

Uygulama özellikle:

* **Basit kurulum**
* **Hızlı kullanım**
* **Platform bağımsız dosya yolu yönetimi (Windows / macOS / Linux)**

gibi konular gözetilerek geliştirilmiştir.

---

## ✨ Özellikler

### 👨‍💼 Restoran Yönetimi

* ➕ Yeni ürün ekleme (isim, kategori, fiyat, açıklama, görsel)
* 🗑️ Ürün silme
* 🖼️ Ürün görsellerini yükleme ve yönetme
* 📋 Menüdeki ürünleri kart yapısıyla listeleme
* 💾 SQLite veritabanı ile kalıcı veri saklama

### 👥 Menü Görünümü

* 📱 Responsive tasarım (mobil uyumlu)
* 🖼️ Görsel odaklı ürün kartları
* 💰 Net fiyat gösterimi
* 🧠 Görsel bulunamazsa otomatik placeholder kullanımı

---

## 🚀 Kurulum ve Çalıştırma

### Gereksinimler

* Python 3.9+
* Streamlit
* Pandas

```bash
pip install -r requirements.txt
```

### Uygulamayı Başlatma

Proje ana dizinindeyken:

```bash
streamlit run app.py
```

Uygulama varsayılan olarak aşağıdaki adreste çalışır:

```
http://localhost:8501
```

---

## 📁 Proje Yapısı

```
RestoranMenusu/
│
├── app.py                 # Streamlit uygulama giriş noktası
├── restoran.db            # SQLite veritabanı
├── requirements.txt       # Python bağımlılıkları
├── README.md              # Proje dokümantasyonu
│
├── src/
│   ├── __init__.py
│   ├── views.py           # Arayüz ve sayfa fonksiyonları
│   ├── database.py        # Veritabanı işlemleri
│   └── img/               # Ürün görselleri
│
└── .venv/                 # (Opsiyonel) Sanal ortam
```

---

## 🛠️ Kullanılan Teknolojiler

* **Frontend / Backend:** Streamlit
* **Veri Yönetimi:** SQLite + Pandas
* **Görsel Yönetimi:** Pillow (Streamlit image handling)
* **Dosya Yolu Yönetimi:** pathlib (cross-platform uyumlu)

---

## 🧠 Teknik Detaylar

### 📁 Görsel Yönetimi

* Yüklenen görseller `src/img/` klasörüne kaydedilir
* Veritabanında **relative path** saklanır (`src/img/urun.webp`)
* Windows (`\\`) ve Unix (`/`) path farkları otomatik düzeltilir

### 🗄️ Veritabanı Yapısı

Temel alanlar:

* `id`
* `isim`
* `kategori`
* `fiyat`
* `aciklama`
* `gorsel_yolu`

---

## 📱 Kullanım Senaryoları

* 🏪 Küçük ve orta ölçekli restoranlar
* 📚 Eğitim amaçlı Streamlit CRUD projeleri
* 🧪 Veritabanı ve dosya yönetimi pratiği

---

## 🔮 Gelecekte Eklenebilecek Özellikler

* ✏️ Ürün düzenleme (edit)
* 🔍 Arama ve kategori filtreleme
* 📦 Docker desteği
* ☁️ Streamlit Cloud deploy
* 📊 Basit menü istatistikleri

---

## 👤 Geliştirici Notu

Bu proje eğitim ve kişisel gelişim amaçlı hazırlanmıştır.
Streamlit kullanarak **gerçek hayata yakın bir CRUD uygulaması** geliştirmek isteyenler için iyi bir örnektir.

---

## 📜 Lisans

Bu proje **MIT Lisansı** ile sunulmaktadır.

---

✨ Her türlü geliştirme fikri ve katkıya açıktır.
