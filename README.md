# 📝 Python Görev Yönetim Uygulaması (To-Do List)

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white" alt="JSON" />
  <img src="https://img.shields.io/badge/CLI-4D4D4D?style=for-the-badge&logo=windows-terminal&logoColor=white" alt="CLI" />
</p>

## 📋 Proje Özeti
Bu proje, Python programlama dili kullanılarak geliştirilmiş konsol tabanlı bir Görev Yönetim Uygulamasıdır (To-Do List). Kullanıcıların günlük görevlerini dijital bir ortamda güvenli ve düzenli bir şekilde yönetmelerini (CRUD işlemleri) sağlar. Ayrıca önceliklendirme, tarih atama ve durum takibi gibi ileri seviye özelliklerle verimliliği artırmayı hedeflemektedir.

## ✨ Temel ve İleri Seviye Özellikler

* **Kalıcı Veri Saklama:** Tüm veriler veri kaybını önlemek amacıyla utf-8 formatında `gorevler.txt` dosyasına JSON yapısında kalıcı olarak kaydedilmektedir.
* **Kullanıcı Deneyimi (UX) ve Arayüz:** Uygulama, sonsuz bir döngü içerisinde çalışan ve kullanıcıya 6 farklı işlem seçeneği sunan basit, temiz ve anlaşılır bir konsol menüsüne sahiptir. Her işlem sonrası konsol ekranı temizlenerek (clear_screen) bilgi kirliliği önlenmiştir. Kullanıcının yanlış veya boş veri girmesi durumunda program çökmez; hata kontrol (try-except) mekanizmaları devreye girerek kullanıcıyı doğru formata yönlendirir.
* **Detaylı Görev Listeleme:** Kaydedilmiş tüm görevleri; sıra numarası, tamamlanma durumu, görev metni, öncelik seviyesi ve son tarih bilgileriyle birlikte formatlı bir şekilde ekrana yazdırır. Görevlere tamamlandı/tamamlanmadı durumu ekleme emoji destekli olarak görselleştirilmiştir.
* **Akıllı Görev Ekleme:** Kullanıcıdan görev metnini alır ve boş girişler reddedilir. Ek olarak kullanıcıdan "Öncelik Seviyesi" (Yüksek, Normal, Düşük) ve "Son Tarih" alınır. Son tarihler `datetime` modülü ile GG.AA.YYYY formatında doğrulanarak eklenir.
* **Esnek Düzenleme ve Silme (CRUD):** Seçilen görevin metni, son tarihi ve tamamlanma durumu değiştirilebilir. Mevcut veriyi korumak isteyen kullanıcılar için sadece Enter tuşuna basarak atlama kolaylığı sağlanmıştır. Numarası girilen görevi listeden ve kayıt dosyasından kalıcı olarak siler ve geçersiz numara girişleri engellenmiştir.
* **Algoritmik Sıralama:** Görevleri "Yüksek > Normal > Düşük" öncelik sırasına göre algoritmik olarak sıralama yeteneğine sahiptir.

## 🚀 Nasıl Çalıştırılır?

1. Dosyaları bilgisayarınıza indirin veya projeyi klonlayın.
2. Terminal veya komut satırını açarak dosyanın bulunduğu dizine gidin.
3. Aşağıdaki komut ile uygulamayı başlatın:
   ```bash
   python app.py
(Not: Uygulamayı isterseniz doğrudan Google Colab üzerinden de test edebilirsiniz: [TNC Group Colab Projesi](https://colab.research.google.com/drive/1tm-JPxMmWeY7bvwXKfgxNKWxAyrhPpYS?usp=sharing))
