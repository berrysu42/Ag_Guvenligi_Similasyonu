from ag_taramasi import ag_taramasi
from port_taramasi import port_taramasi
from sifreleme import sifreleme_verisi
from PIL import Image, ImageTk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox

"""
if __name__ == "__main__":
    hedef_ip = input("Hedef IP adresini giriniz: ")

    #Ağ cihazlarını tarama 
    print("\n Ağ Cihazları: \n")
    ag_cihazlari = ag_taramasi(hedef_ip)

    for cihaz in ag_cihazlari:
        print(f"IP: {cihaz['ip']}, MAC: {cihaz['mac']}")

    #port taraması yapma
    print("\n Port taraması sonuçları ->  ")
    port_sonuclari = port_taramasi(hedef_ip)
    for host, data in port_sonuclari.items():
        print(f"Host: {host}, Durum: {data}")


    #Şifreleme İşlemi
    print("\n Şifreleme İşlemi: \n")
    metin = input("Şifrelemek istediğiniz metni giriniz. ->")
    key,encrypted,decrypted = sifreleme_verisi(metin)

    print(f"Anahtar: {key}")
    print("Şifrelenmiş Metin: {encrypted}")
    print(f"Şifresi Çözülmüş Metin: {decrypted }")
"""

# GUI fonksiyonu
def run_simulation():
    hedef_ip = ip_entry.get()  # IP adresini giriş kutusundan al

    if not hedef_ip:  # IP adresi girilmemişse hata ver
        messagebox.showerror("Hata", "Lütfen geçerli bir IP adresi girin!")
        return

    # Taranacak port aralığını al
    try:
        baslangic_port = int(port_start_entry.get())
        bitis_port = int(port_end_entry.get())
        if baslangic_port < 0 or bitis_port > 65535 or baslangic_port > bitis_port:
            raise ValueError
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir port aralığı girin! (0-65535)")
        return

    # Ağ cihazlarını tarama
    ag_cihazlari = ag_taramasi(hedef_ip)
    ag_output.delete(1.0, tk.END)  # Önceki çıktıyı temizle

    if ag_cihazlari:
        ag_output.insert(tk.END, "Ağ Cihazları:\n")
        for cihaz in ag_cihazlari:
            ag_output.insert(tk.END, f"IP: {cihaz['ip']}, MAC: {cihaz['mac']}\n")
    else:
        ag_output.insert(tk.END, "Ağ cihazları bulunamadı.\n")

    # Port taraması yapma
    port_sonuclari = port_taramasi(hedef_ip)
    port_output.delete(1.0, tk.END)

    if port_sonuclari:
        port_output.insert(tk.END, "\nPort Taraması Sonuçları:\n")
        for host, data in port_sonuclari.items():
            port_output.insert(tk.END, f"Host: {host}, Durum: {data}\n")
    else:
        port_output.insert(tk.END, "Port taraması sonuçları bulunamadı.\n")

    # Şifreleme işlemi
    metin = metin_entry.get()  # Şifrelenecek metni giriş kutusundan al
    if metin:
        key, encrypted, decrypted = sifreleme_verisi(metin)
        sifreleme_output.delete(1.0, tk.END)
        sifreleme_output.insert(tk.END, f"Anahtar: {key}\n")
        sifreleme_output.insert(tk.END, f"Şifrelenmiş Metin: {encrypted}\n")
        sifreleme_output.insert(tk.END, f"Şifresi Çözülmüş Metin: {decrypted}\n")
    else:
        sifreleme_output.insert(tk.END, "Şifrelenmek için bir metin girin.\n")

def close_app():
    # Pencereyi kapatmak için kullanılır
    root.destroy()

def update_background(event=None):
    """Pencere boyutuna göre arka planı günceller."""
    global bg_image, bg_resized_image
    new_width = root.winfo_width()
    new_height = root.winfo_height()

    # Görseli yeniden boyutlandır
    bg_resized_image = bg_original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(bg_resized_image)
    bg_label.config(image=bg_image)

# Ana GUI Penceresi
root = tk.Tk()
root.title("Ağ Güvenliği Simülasyonu")
root.geometry("800x600")  # Varsayılan boyut

# Arka plan resmi
bg_original_image = Image.open("arkaPlan2.jpeg")  # Orijinal resmi yükle
bg_resized_image = bg_original_image.resize((800, 600), Image.Resampling.LANCZOS)  # Başlangıç boyutunda ayarla
bg_image = ImageTk.PhotoImage(bg_resized_image)

bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Resmi tam olarak yay

# Pencere boyut değişikliklerini takip et
root.bind("<Configure>", update_background)


# IP adresi girişi
ip_label = tk.Label(root, text="Hedef IP Adresi:")
ip_label.pack(padx=5, pady=3)

ip_entry = tk.Entry(root, width=30)
ip_entry.pack(padx=10, pady=5)

# Ağ cihazları çıktısı
ag_output_label = tk.Label(root, text="Ağ Cihazları:")
ag_output_label.pack(padx=10, pady=5)

ag_output = tk.Text(root, width=50, height=5, wrap=tk.WORD)
ag_output.pack(padx=10, pady=5)

# Port aralığı girişi
port_start_label = tk.Label(root, text="Başlangıç Portu:", bg="#ffffff")
port_start_label.pack(padx=10, pady=5)

port_start_entry = tk.Entry(root, width=10)
port_start_entry.pack(padx=10, pady=5)

port_end_label = tk.Label(root, text="Bitiş Portu:", bg="#ffffff")
port_end_label.pack(padx=10, pady=5)

port_end_entry = tk.Entry(root, width=10)
port_end_entry.pack(padx=10, pady=5)

# Şifreleme için metin girişi
metin_label = tk.Label(root, text="Şifrelemek istediğiniz metni giriniz:", bg="#ffffff")
metin_label.pack(padx=10, pady=5)

metin_entry = tk.Entry(root, width=30)
metin_entry.pack(padx=10, pady=5)

# Port taraması sonuçları
port_output_label = tk.Label(root, text="Port Taraması Sonuçları:")
port_output_label.pack(padx=10, pady=5)

port_output = tk.Text(root, width=150, height=8, wrap=tk.WORD)
port_output.pack(padx=10, pady=5)

# Şifreleme sonuçları
sifreleme_output_label = tk.Label(root, text="Şifreleme Sonuçları:", bg="#ffffff")
sifreleme_output_label.pack(padx=10, pady=5)

sifreleme_output = tk.Text(root, width=150, height=8, wrap=tk.WORD)
sifreleme_output.pack(padx=10, pady=5)

# Simülasyonu başlatan buton
run_button = tk.Button(root, text="Simülasyonu Başlat", command=run_simulation)
run_button.pack(padx=10, pady=10)

# Kapat butonu
close_button = tk.Button(root, text="Kapat", command=close_app)
close_button.pack(pady=5)

# GUI'yi başlat
root.mainloop()


"""
# Port taraması çıktısı
port_output_label = tk.Label(root, text="Port Taraması Sonuçları:")
port_output_label.pack(padx=10, pady=5)

port_output = tk.Text(root, width=50, height=10, wrap=tk.WORD)
port_output.pack(padx=10, pady=5)
"""