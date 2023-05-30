# File Encryptor

Bu Python programı, dosyaları şifrelemek ve şifresini çözmek için kullanılabilir. Şifreleme işlemi, Fernet şifreleme algoritması kullanılarak gerçekleştirilir.

## Gereksinimler

- Python 3.x
- `cryptography` kütüphanesi
- `tqdm` kütüphanesi

Gerekli kütüphaneleri yüklemek için aşağıdaki komutları kullanabilirsiniz:

    pip install cryptography
    pip install tqdm
    
## Kullanım

1. Anahtar üretme veya kullanıcıdan alma:
   - Program, `key.key` adında bir anahtar dosyası kullanır. Eğer `key.key` dosyası mevcut değilse, otomatik olarak yeni bir anahtar üretilir.
   - Eğer anahtar dosyası mevcutsa, anahtar dosyası yüklenir ve kullanılmaya başlanır.

2. Anahtarları yönetme:
   - "3. Yeni Anahtar Oluştur" seçeneği, mevcut anahtar dosyasını siler ve yeni bir anahtar oluşturur.
   - "4. Anahtarı Sil" seçeneği, mevcut anahtar dosyasını siler ve anahtar kullanılamaz hale gelir.

3. Dosya şifreleme ve çözme:
   - "1. Dosya Şifrele" seçeneği, şifrelemek istediğiniz dosyanın adını isteyecektir. Dosya, Fernet şifreleme algoritması kullanılarak şifrelenir.
   - "2. Dosya Şifresini Çöz" seçeneği, çözmek istediğiniz şifreli dosyanın adını isteyecektir. Dosya, Fernet şifreleme algoritması kullanılarak çözülür.

4. Programdan çıkış:
   - "5. Çıkış" seçeneği, programdan çıkmanızı sağlar.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyebilirsiniz.

