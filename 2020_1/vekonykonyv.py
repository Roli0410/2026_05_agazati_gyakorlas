import random

def vekony(szam):
    if szam < 220:
        return True
    else:
        return False
    
db = 0
for szam in range(200):
    szam = random.randint(100, 500)
    if vekony(szam):
        db += 1

szazalek = (db / 200) * 100

print(f"A 200 könyvből {db} vékonyabb 220 oldalnál.")
print(f"Ez az összes könyv {round(szazalek, 2)} százaléka")