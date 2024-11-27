from cryptography.fernet import Fernet

def sifreleme_verisi(metin):
    key = Fernet.generate_key()  # Anahtar oluştur
    fernet = Fernet(key)

    encrypted = fernet.encrypt(metin.encode())  # Şifrele
    decrypted = fernet.decrypt(encrypted).decode()  # Şifreyi çöz

    return key.decode(), encrypted.decode(), decrypted
