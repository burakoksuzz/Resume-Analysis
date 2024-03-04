# Resume-Analysis
Resume Analyzer
Resume Analyzer

Bu proje, iş açıklaması ve özgeçmiş metinlerini kullanarak eşleşme yüzdesini analiz eden bir araçtır. Kullanıcıdan alınan iş açıklaması ve özgeçmiş dosyaları üzerinde çalışır ve eşleşme yüzdesini, eşleşme sebebini, anahtar kelimeleri ve aday bilgilerini çıktı olarak sunar. Ayrıca, eşleşme yüzdesini görsel olarak sunar.

Nasıl Kullanılır?
Anahtar API Anahtarınızı Ayarlayın:
Kodun çalışması için bir OpenAI API anahtarı gereklidir. Anahtarınızı key değişkenine atayarak kodun başlangıcında belirtmelisiniz.

Gradio Arayüzünü Kullanarak Analiz Yapın:
Gradio arayüzünü başlatmak için kodu çalıştırın. Arayüz, iş açıklaması ve özgeçmiş dosyalarını yüklemenizi sağlayacak bir dosya yükleme alanı sunar. Analiz butonuna tıkladıktan sonra, eşleşme yüzdesi, sebep, anahtar kelimeler ve aday bilgileri görüntülenecektir.

Gereksinimler
Python 3.x
PyPDF2
OpenAI
Plotly
Gradio
Kurulum
Depoyu klonlayın:

bash
Copy code
git clone https://github.com/kullanıcı_adı/Resume-Analyzer.git
Proje dizinine gidin:

bash
Copy code
cd Resume-Analyzer
Gerekli kütüphaneleri yükleyin:

bash
Copy code
pip install -r requirements.txt
Anahtar API anahtarınızı ekleyin:

Kodun başlangıcındaki key değişkenine OpenAI API anahtarınızı ekleyin.

Kodu çalıştırın:

bash
Copy code
python main.py
