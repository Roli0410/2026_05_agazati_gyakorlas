import random


def gyors_kor(masodperc):
    if masodperc < 105:
        return True
    else:
        return False
    

db = 0

for i in range(120):
    idok = random.randint(95, 120)
    if gyors_kor(idok):
        db += 1

szazalek = (db / 120) * 100

print(f"A 120 körből {db} volt 105 másodpercnél gyorsabb.\n Ez a körök {round(szazalek, 2)}%-a.")