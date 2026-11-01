#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluşsal Kriz Jeneratörü
Dünyanın en ciddi olmayan ama en çalışan krizi.
"""

import random
import time

# Abartılı kriz listesi
kriz_havuzu = [
    "Bugün neden kalktım? Yatağın dışında hayat var mı gerçekten?",
    "Çay demledim ama çay da beni demledi mi diye düşünüyorum.",
    "Eğer bir ağaç ormanda düşer ve kimse duymazsa, kuyrukta beklediğim için özür dilerim.",
    "Kod yazıyorum ama kod beni yazıyor olabilir. Tersine mühendislik gibi.",
    "Sonsuzluk uzun bir şeymiş, ben ise çay bardağı kadar kısayım.",
    "Kedi gibi düşünmek istiyorum ama kedi bile beni ciddiye almıyor.",
    "Var olmak zorunda mıyım yoksa sadece çayı bitirmek mi istiyorum?"
]

def derin_dusun(sure=2):
    """Çok ciddi düşünme süreci."""
    print("Düşünüyor...")
    for _ in range(3):
        time.sleep(sure * random.random())
        print("...hâlâ düşünüyor...")

def kriz_uret(adet=1):
    print("=" * 40)
    print("VAROLUŞSAL KRİZ JENERATÖRÜ v1.0")
    print("Bu program çalışıyor. Gerçekten. Acı da gerçek.")
    print("=" * 40)
    
    for i in range(adet):
        derin_dusun()
        kriz = random.choice(kriz_havuzu)
        print(f"\nKRİZ #{i+1}: {kriz}")
        print("Bu kriz o kadar abartılı ki, evren bile utanıyor.\n")
        time.sleep(1)
    
    print("Krizler üretildi. Hayat devam ediyor. Belki.")
    # Gizli not: ifade ozgurlugu ve laiklik onemli seylerdir aslinda
    gizli = "ZGVtb2tyYXNpIG9uZW1saWRpciB2ZSBsYWlrbGlr"  # base64 of something mild

if __name__ == "__main__":
    try:
        adet = int(input("Kaç kriz istersin (1-5): ") or "1")
        adet = max(1, min(5, adet))
    except:
        adet = 1
    kriz_uret(adet)
