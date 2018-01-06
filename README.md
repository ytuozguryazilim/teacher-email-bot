# teacher-email-bot
Bu projenin amaci hocalarin tek tek mailleri bakip, pdf listesi cikarmasini otomatiklestirmek. Suanlik sadece gmail'e destek var. Bu proje tam olarak sunu yapar, otomatik odevleri gonderenlerin listesini olusturup Pdf haline getirir ve odevleri indirir.(Gmail Api)

Hocalara mail atilirken konu basligi olarak belli bir kural olmali. Suanlik alttaki gibi kural kullanilacak. 

<code>[Universite-Yil-Donem-DersinKodu-Odev-OkulNumarasi-IsimSoyisim]</code>

Ileri versiyonunda sadece okul mail'iyle atilan mail'lere izin verilecek. Cunku herkes baska birinin yerine mail atarak, dosyalarin uzerine yazabilir.

# Kurulum

```bash
                          $ git clone https://github.com/GnuYtuce/teacher-email-bot/
                          $ cd teacher-email-bot/src
  (teacher-email-bot/src) $ virtualenv venv
  (teacher-email-bot/src) $ source venv/bin/active
                   (venv) $ pip install -r requirements.txt
                   (venv) $ # Sonraki adim olarak gmail api key'i almalisin. https://developers.google.com/gmail/api/quickstart/python
                   (venv) $ # aldigin "client_secret.json" dosyasini "src" klasorun altina koymalisin.
                   (venv) $ # Artik alttaki komutu calistirman yeterli olucak.
                   (venv) $ python main.py
```

# Demo
3 tane ornek mail atildi.

![alt text](https://github.com/GnuYtuce/teacher-email-bot/blob/master/pics/email_messages.png)

Sonrasinda uygulama calistirildi. Ve olusan dizinin icerigi goruntulendi.

![alt text](https://github.com/GnuYtuce/teacher-email-bot/blob/master/pics/tree.png)

Daha sonrasinda List.pdf dosyasinin icerigine bakildi.

![alt text](https://github.com/GnuYtuce/teacher-email-bot/blob/master/pics/pdf.png)


# Ornek Mail Basliklari

Ornek Mail basliklari:

<code>[Ytu-2015-Guz-BLM1551-HW2-14400128-TuncaySanli]</code>

<code>[Itu-2016-Bahar-BLM3841-HW1-100000112-Ersanİlyasova]</code>

<code>[Odtu-2015-Guz-BLM1552-Q1-14400128-CediOsman]</code>

<code>[Iu-2016-Bahar-BLM3841-Q5-100000112-EmreGuler]</code>

<code>[Mtu-2015-Guz-BLM1551-Project1-14400128-IsilAlben]</code>

<code>[Ktu-2016-Bahar-BLM3841-Assignment3-100000112-CenkTosun]</code>
