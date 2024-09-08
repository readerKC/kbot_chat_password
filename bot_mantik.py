import random

def sifre_olusturucu(parola_uzunlugu ):
    karakterler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    parola = ""
    for _ in range(parola_uzunlugu):
        rastgele_karakter = random.choice(karakterler)
        parola += rastgele_karakter

    return parola
