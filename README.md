# 📄 Resume Analyzer 📊

![Resume Analyzer](https://r.resimlink.com/aJuC4Vs75k.jpg)
![Resume Analyzer](https://r.resimlink.com/5osbrIS0mu.jpg)

Bu proje, iş açıklaması ve özgeçmiş metinlerini kullanarak eşleşme yüzdesini analiz eden bir araçtır. Kullanıcıdan alınan iş açıklaması ve özgeçmiş dosyaları üzerinde çalışır ve eşleşme yüzdesini, eşleşme sebebini, anahtar kelimeleri ve aday bilgilerini çıktı olarak sunar. Ayrıca, eşleşme yüzdesini görsel olarak sunar.

## Nasıl Kullanılır? 🚀

1. **Anahtar API Anahtarınızı Ayarlayın:**
   Kodun çalışması için bir OpenAI API anahtarı gereklidir. Anahtarınızı `key` değişkenine atayarak kodun başlangıcında belirtmelisiniz.

2. **Gradio Arayüzünü Kullanarak Analiz Yapın:**
   Gradio arayüzünü başlatmak için kodu çalıştırın. Arayüz, iş açıklaması ve özgeçmiş dosyalarını yüklemenizi sağlayacak bir dosya yükleme alanı sunar. Analiz butonuna tıkladıktan sonra, eşleşme yüzdesi, sebep, anahtar kelimeler ve aday bilgileri görüntülenecektir.

## Gereksinimler 🛠️

- Python 3.x
- PyPDF2
- OpenAI
- Plotly
- Gradio

## Kurulum 📦

1. Depoyu klonlayın:

   ```bash
   git clone https://github.com/burakoksuzz/Resume-Analyzer.git

  2.Proje dizinine gidin:
  ```bash
    cd Resume-Analyzer
       
  3.Gerekli kütüphaneleri yükleyin:

   ```bash
      pip install -r requirements.txt


