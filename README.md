# Kapak İndirici

Bu uygulama, oyun ve film kapaklarını otomatik olarak indirmenizi sağlayan kapsamlı bir araçtır. Ayrıca, indirilen kapakları PDF formatında düzenleme ve metin dosyalarını yönetme özelliklerine sahiptir.

## Özellikler

### Oyun Kapakları
- Steam ve Twitch API'lerini kullanarak oyun kapaklarını otomatik indirme
- Türkçe oyun isimlerini otomatik tanıma ve eşleştirme
- Tekrar eden kapakları otomatik tespit etme
- İndirilemeyen oyunları raporlama

### Film Kapakları
- OMDb API kullanarak film kapaklarını otomatik indirme
- Türkçe film isimlerini İngilizce karşılıklarıyla değiştirme
- Tekrar eden kapakları otomatik tespit etme
- İndirilemeyen filmleri raporlama

### PDF Oluşturucu
- İndirilen kapakları PDF formatında düzenleme
- Otomatik sayfa düzeni ve boyutlandırma
- Çoklu sayfa desteği
- Görsel optimizasyonu

### Metin Düzenleyici
- Metin dosyalarını düzenleme
- Alfabetik sıralama
- Tekrar eden satırları temizleme
- UTF-8 kodlaması desteği

## Kurulum

1. Python 3.8 veya daha yüksek bir sürümü yükleyin
2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

## Kullanım

1. Uygulamayı başlatın:
```bash
python main.py
```

2. Oyun Kapakları İndirme:
   - "Oyun Listesi Seç" butonuna tıklayın
   - Oyun isimlerinin bulunduğu txt dosyasını seçin
   - "Oyun Kapaklarını İndir" butonuna tıklayın

3. Film Kapakları İndirme:
   - "Film Listesi Seç" butonuna tıklayın
   - Film isimlerinin bulunduğu txt dosyasını seçin
   - "Film Kapaklarını İndir" butonuna tıklayın
   - İsterseniz "İngilizce İsimlerle Değiştir" butonunu kullanın

4. PDF Oluşturma:
   - "Resim Seç" butonuna tıklayın
   - Kapakları seçin
   - "PDF Oluştur" butonuna tıklayın

5. Metin Düzenleme:
   - "Metin Dosyası Seç" butonuna tıklayın
   - Düzenlemek istediğiniz txt dosyasını seçin
   - Metni düzenleyin ve kaydedin

## API Anahtarları

Uygulama aşağıdaki API'leri kullanmaktadır:
- Steam API
- Twitch API
- OMDb API

API anahtarlarınızı `APIConfig` sınıfında güncelleyebilirsiniz.

## Dosya Yapısı

```
archive-editor/
├── main.py              # Ana uygulama dosyası
├── film_cevir.py        # Film çeviri yardımcı dosyası
├── requirements.txt     # Gerekli paketler
├── README.md           # Bu dosya
├── Oyunlar/            # İndirilen oyun kapakları
├── Filmler/            # İndirilen film kapakları
└── resimler.pdf        # Oluşturulan PDF dosyası
```

## Geliştirme

Projeyi geliştirmek için:
1. Bu repository'yi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik: X'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın. 