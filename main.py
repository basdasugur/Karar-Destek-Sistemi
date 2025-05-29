#Uygulama: Yapay Zeka Model Karar Destek Sistemi
#Bir yapay zeka modelinin farklı durumlara göre karar vermesi gereken bir senaryo oluşturalım. Model, bir durumu analiz ediyor ve buna göre bir eylem öneriyor.

#Görev:
#Modelin güvenirlik skorunu temsil eden bir float değişkeni oluşturun: model_guvenirlik_skoru (örneğin: 0.78).
model_guvenirlik_skoru = 0.78

#Tespit edilen anomali (anormallik) şiddetini temsil eden bir integer değişkeni oluşturun: anomali_siddeti (0-100 arası bir değer, örneğin: 75).
anomali_siddeti = 75

#Cihazın online olup olmadığını temsil eden bir boolean değişkeni oluşturun: cihaz_online_mi (örneğin: True).
cihaz_online_mi = True


#if-elif-else Yapısı Kullanarak Karar Mekanizması Oluşturun:
#Eğer model_guvenirlik_skoru 0.90'dan büyük veya eşitse:
#Ekrana "Yüksek güvenli tespit: Otomatik düzeltme uygulanıyor." yazdırın.
if model_guvenirlik_skoru >= 0.90:
    print("Yüksek güvenli tespit: Otomatik düzeltme uygulanıyor")

#Değilse, eğer model_guvenirlik_skoru 0.70'den büyük veya eşitse:
#Eğer anomali_siddeti 60'ın üzerindeyse:
#Ekrana "Orta güvenli tespit: Anomali şiddeti yüksek. Manuel kontrol gerekli." yazdırın.

elif model_guvenirlik_skoru >= 0.70:
    if anomali_siddeti > 60:
        print("Orta güvenli tespit: Anomali şiddeti yüksek. Manuel kontrol gerekli")
    else:
        print("Orta güvenli tespit Anomli şiddeti düşük. İzlemeye devam ediliyor.")

#Değilse:

#Ekrana "Orta güvenli tespit: Anomali şiddeti düşük. İzlemeye devam ediliyor." yazdırın.

#Değilse (yani model_guvenirlik_skoru 0.70'in altındaysa):
elif model_guvenirlik_skoru < 0.70:
    if cihaz_online_mi == False:
        print("Düşük güvenli tespit: Cihaz offline. Bağlantı kontrolü gerekli")

#Eğer cihaz_online_mi False ise:
#Ekrana "Düşük güvenli tespit: Cihaz offline. Bağlantı kontrolü gerekli." yazdırın.


#Değilse (cihaz_online_mi True ise):
#Ekrana "Düşük güvenli tespit: Daha fazla veri bekleniyor veya uzman incelemesi." yazdırın.

    else:
        print("Düşük güvenli tespit: Daha fazla veri bekleniyor veya uzman incelemesi.")

#Kodunuzu farklı değişken değerleriyle (özellikle model_guvenirlik_skoru, anomali_siddeti ve cihaz_online_mi değerlerini değiştirerek) test edin ve çıktılarının beklediğiniz gibi olup olmadığını kontrol edin.

