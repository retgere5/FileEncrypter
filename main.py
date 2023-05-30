from cryptography.fernet import Fernet
from tqdm import tqdm
import os


class FileEncryptor:
    def __init__(self, key_file):
        self.key_file = key_file
        self.key = None
        self.fernet = None

    def generate_key(self):
        key = Fernet.generate_key()
        with open(self.key_file, "wb") as key_file:
            key_file.write(key)

    def load_key(self):
        with open(self.key_file, "rb") as key_file:
            self.key = key_file.read()
        self.fernet = Fernet(self.key)

    def process_file(self, filename, mode):
        if self.fernet is None:
            print("Anahtar yüklenemedi. Lütfen önce anahtarı yükleyin.")
            return
        progress_bar = tqdm(total=os.path.getsize(filename),
                            unit="B", unit_scale=True, desc=mode.capitalize() + "ing")
        try:
            with open(filename, "rb") as file:
                data = file.read()
            processed_data = getattr(self.fernet, mode)(data)
            with open(filename, "wb") as processed_file:
                processed_file.write(processed_data)
            progress_bar.update(len(data))
            progress_bar.close()
            print("Dosya başarıyla", mode + "lendi.")
        except KeyboardInterrupt:
            progress_bar.close()
            print("\n", mode.capitalize(), "iptal edildi.")

    def delete_key(self):
        if os.path.exists(self.key_file):
            os.remove(self.key_file)
            print("Anahtar başarıyla silindi.")
        self.key = None
        self.fernet = None


key_file = "key.key"
file_encryptor = FileEncryptor(key_file)

# Anahtar üretme veya kullanıcıdan alınması
if not os.path.exists(key_file):
    file_encryptor.generate_key()

# Anahtarı yükleme
file_encryptor.load_key()

while True:
    print("1. Dosya Şifrele")
    print("2. Dosya Şifresini Çöz")
    print("3. Yeni Anahtar Oluştur")
    print("4. Anahtarı Sil")
    print("5. Çıkış")
    choice = input("Yapmak istediğiniz işlemi seçin (1/2/3/4/5): ")
    if choice == "1":
        dosya_adi = input(
            "Lütfen şifrelemek istediğiniz dosyanın adını girin: ")
        file_encryptor.process_file(dosya_adi, "encrypt")
    elif choice == "2":
        dosya_adi = input(
            "Lütfen şifresini çözmek istediğiniz dosyanın adını girin: ")
        file_encryptor.process_file(dosya_adi, "decrypt")
    elif choice == "3":
        file_encryptor.delete_key()
        file_encryptor.generate_key()
        file_encryptor.load_key()
        print("Yeni anahtar oluşturuldu ve yüklendi.")
    elif choice == "4":
        file_encryptor.delete_key()
    elif choice == "5":
        break
    print()
