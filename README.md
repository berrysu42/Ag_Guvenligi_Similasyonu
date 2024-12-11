# 📍 Ağ Güvenliği Simülasyonu
Bu proje, ağ güvenliği simülasyonu gerçekleştirmek için Python ve Tkinter kullanarak geliştirilmiş bir GUI uygulamasıdır. Kullanıcılar, hedef IP adresi üzerinden ağ cihazlarını tarayabilir, port taraması yapabilir ve metin şifreleme işlemleri gerçekleştirebilirler.
Özellikler

    Ağ Tarama: Belirtilen IP adresine bağlı ağ cihazlarının IP ve MAC adreslerini tarar.
    Port Tarama: Belirli bir IP adresindeki 1-1024 arası portları tarar ve sonuçları gösterir.
    Şifreleme: Kullanıcı tarafından girilen metni şifreler ve çözme işlemini gerçekleştirir.

Kullanım

    Ağ Tarama: Kullanıcı, bir IP adresi girerek ağdaki cihazları tarayabilir.
    Port Tarama: Başlangıç ve bitiş portlarını girerek, belirli bir port aralığını tarayabilirsiniz.
    Şifreleme: Şifrelenmesini istediğiniz metni girerek, simetrik şifreleme işlemi gerçekleştirebilirsiniz.

Gereksinimler

    Python 3.x
    Tkinter
    Nmap
    Scapy
    Pillow (PIL)


##Kullanıcı Arayüzü

GUI üzerinden:

    Hedef IP adresi, port aralığı ve şifreleme metni girilir.
    Tarama ve şifreleme sonuçları GUI üzerinden görüntülenir.

## 🔐 Şifreleme ve Şifre Çözme

Bu fonksiyon, verilen bir metni şifreler ve ardından şifreyi çözer. İlk olarak bir güvenli anahtar oluşturulur. Ardından, metin şifrelenir ve bu şifreli metin çözülerek orijinal metin geri elde edilir. Sonuç olarak, fonksiyon şifreleme anahtarını, şifreli veriyi ve şifresi çözülmüş metni döndürür.

### 📌 İşlevler

#### Anahtar Oluşturma
`Fernet.generate_key()` fonksiyonu ile şifreleme için benzersiz bir anahtar oluşturulur.

#### Şifreleme
`fernet.encrypt(metin.encode())` fonksiyonu, verilen metni şifreler.

#### Şifre Çözme
`fernet.decrypt(encrypted)` fonksiyonu, şifreli metni çözer ve orijinal metni geri döndürür.

### 🔑 Çıktılar

- **Anahtar**: Şifreleme için kullanılan oluşturulmuş güvenli anahtar.
- **Şifrelenmiş Veri**: Şifrelenmiş metin.
- **Çözülmüş Veri**: Şifresi çözülmüş, orijinal metin.

## 🌐 Port Tarama

Bu fonksiyon, belirli bir hedef IP adresi üzerinde port taraması yapar ve 1 ile 1024 arasındaki portları tarar. Nmap kütüphanesini kullanarak port taraması gerçekleştirilir ve tarama sonuçları döndürülür.

### 📌 İşlevler

#### Port Taraması
`nmap.PortScanner()` kullanılarak hedef IP adresindeki 1 ile 1024 arasındaki portlar taranır.

### 🔑 Çıktılar

- **Tarama Sonuçları**: Hedef IP adresindeki açık portlar hakkında detaylı bilgiler içerir.

## 💻 Kurulum ve Kullanım

1. **Gerekli Kütüphaneyi Yükleyin**:
   ```bash
   pip install cryptography nmap

![image alt](https://github.com/berrysu42/Ag_Guvenligi_Similasyonu/blob/562886578b683ea55d26ca6a897e1dc887003304/AgSimilasyonu.png)

