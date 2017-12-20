# teacher-email-bot
Bu projenin amaci hocalarin tek tek mailleri bakip, pdf listesi cikarmayi otomatiklestirmek. Suanlik sadece gmail'e destek var. Bu proje tam olarak sunu yapar, otomatik odevleri gonderenlerin listesini olusturup Pdf haline getirir ve odevleri indirir.(Gmail Api)

Hocalara mail atilirken konu basligi olarak belli bir kural olmali. Suanlik alttaki gibi kural kullanilacak. 

[Universite-Yil-Donem-DersinKodu-Odev-OkulNumarasi-IsimSoyisim]

Ornek Mail basliklari:

[Ytu-2015-Guz-BLM1551-HW2-14400128-EmreGuler]

[Itu-2016-Bahar-BLM3841-HW1-100000112-RecepEr]

[Odtu-2015-Guz-BLM1552-Q1-14400128-EmreGuler]

[Iu-2016-Bahar-BLM3841-Q5-100000112-RecepEr]

[Mtu-2015-Guz-BLM1551-Project1-14400128-EmreGuler]

[Ktu-2016-Bahar-BLM3841-Assignment3-100000112-RecepEr]

Ileri versiyonunda sadece okul mail'iyle atilan mail'lere izin verilecek. Cunku herkes baska birinin yerine mail atarak, dosyalarin uzerine yazabilir.

# Kurulum

```bash
  $ git clone https://github.com/GnuYtuce/teacher-email-bot/
  $ cd teacher-email-bot/src
  $ virtualenv venv
  $ source venv/bin/active
  $ pip install -r requirements.txt
  $ # Sonraki adim olarak gmail api key'i almalisin. https://developers.google.com/gmail/api/quickstart/python
  $ # aldigin "client_secret.json" dosyasini "src" klasorun altina koymalisin.
  $ # Artik alttaki komutu calistirman yeterli olucak.
  $ python main.py
```
