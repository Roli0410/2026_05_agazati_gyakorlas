import random


def kozte(szam, also, felso):
    if also<= szam<=felso:
        return True
    else: 
        return False 

db = 0
dobasok_szama = 150

for i in range(dobasok_szama):
    dobas = random.randint(1,  12)

    if kozte(dobas, 4, 8):
        db += 1 

szazalek = (db / dobasok_szama) * 100

print(f"Az {dobasok_szama} dobásból {db} esett 4 és 8 közé. ")
print(f"Ez az összes dobás {szazalek: .2f}%-a.")


