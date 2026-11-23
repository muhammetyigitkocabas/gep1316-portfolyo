# merhaba.py
# Kullanıcının adını ve doğum yılını alıp yaşını hesaplayan,
# kişiye özel bir karşılama mesajı yazan program.

# datetime modülünü içe aktarıyoruz; bu yılı bilgisayarın saatinden almak için gerekli.
from datetime import date

# Bu yılı alıp "bu_yil" değişkenine kaydediyoruz (ör. 2026).
bu_yil = date.today().year

# Ekrana bir başlık yazdırıyoruz.
print("=== Merhaba Programı ===")

# input() kullanıcıdan klavyeyle bilgi ister; yazılanı metin (str) olarak döndürür.
# strip() baştaki ve sondaki gereksiz boşlukları siler.
ad = input("Adınız nedir? ").strip()

# Doğum yılını da input() ile alıyoruz; gelen değer metin olduğu için
# int() ile tam sayıya çeviriyoruz, böylece onunla hesap yapabiliyoruz.
dogum_yili = int(input("Doğum yılınız nedir? "))

# --- KENDİ EKLEDİĞİM DEĞİŞİKLİK ---
# Doğum yılı bu yıldan büyükse kişi henüz doğmamış demektir; bu durumda uyarı veriyoruz.
if dogum_yili > bu_yil:
    print(f"Uyarı: {dogum_yili} yılı henüz gelmedi! Lütfen doğum yılınızı kontrol edin.")
# Doğum yılı geçerliyse yaşı hesaplayıp karşılama mesajını yazıyoruz.
else:
    # Yaşı, bu yıldan doğum yılını çıkararak hesaplıyoruz.
    yas = bu_yil - dogum_yili

    # f-string ile değişkenleri cümlenin içine yerleştirip mesajı yazdırıyoruz.
    print(f"Merhaba {ad}! GEP1316 dersine hoş geldin.")
    print(f"{dogum_yili} yılında doğduğuna göre bu yıl {yas} yaşına giriyorsun.")
# --- DEĞİŞİKLİĞİN SONU ---
