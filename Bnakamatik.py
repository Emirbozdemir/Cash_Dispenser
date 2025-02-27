import requests
import os


KULLANICI_DOSYASI = 'kullanici_verileri.txt'

def dosya_var_mi():
    return os.path.exists(KULLANICI_DOSYASI)


def kullanici_kaydi(kullanici_adı, sifre):
    with open(KULLANICI_DOSYASI, 'a') as f:
        f.write(f"{kullanici_adı},{sifre}\n")


def kullanici_giris(kullanici_adı, sifre):
    if not dosya_var_mi():
        print("Henüz kayıtlı kullanıcı yok.")
        return False

    with open(KULLANICI_DOSYASI, 'r') as f:
        for satir in f:
            kayit_kullanici_adı, kayit_sifre = satir.strip().split(',')
            if kullanici_adı == kayit_kullanici_adı and sifre == kayit_sifre:
                return True
    return False


def uygulama():
    print("1. Giriş Yap")
    print("2. Kayıt Ol")
    secim = input("Bir seçenek girin (1/2): ")

    if secim == '2':
        kullanici_adı = input("Kullanıcı Adı: ")
        sifre = input("Şifre: ")
        if kullanici_giris(kullanici_adı, sifre):
            print("Kullanıcı zaten mevcut!")
        else:
            kullanici_kaydi(kullanici_adı, sifre)
            print("Kayıt başarılı!")

    elif secim == '1':
        kullanici_adı = input("Kullanıcı Adı: ")
        sifre = input("Şifre: ")
        if kullanici_giris(kullanici_adı, sifre):
            print("Giriş başarılı!")
        else:
            print("Hatalı kullanıcı adı veya şifre!")
    else:
        print("Geçersiz seçenek!")


if __name__ == '__main__':
    uygulama()


