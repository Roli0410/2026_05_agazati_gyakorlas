
print("3. feladat: ")

#3.1
class Konyv():
    def __init__(self , szerzo , cim , kiadas , oldalszam , ekonyv):
        self.szerzo = szerzo
        self.cim = cim
        self.kiadas = kiadas
        self.oldalszam = oldalszam
        self.ekonyv = ekonyv



konyvek = []
with open('2020_1\konyvek.txt', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        konyv = Konyv(adatok[0] , adatok[1] , int(adatok[2]) , int(adatok[3]) , int(adatok[4]))
        konyvek.append(konyv)

#3.2
print(f"3.2 feladat: Az állományban {len(konyvek)} db könyv adatai szerepelnek.")

#3.3
legtobb_oldal = konyvek[0]

for konyv in konyvek:
    if konyv.oldalszam > legtobb_oldal.oldalszam:
        legtobb_oldal = konyv

print(f"3.3 feladat:  A legtöbb oldalas könyv: ")
print(f"\tSzerző: {legtobb_oldal.szerzo}")
print(f"\tCím: {legtobb_oldal.cim}")
print(f"\tKiadás éve: {legtobb_oldal.kiadas}")
print(f"\tOldalszám: {legtobb_oldal.oldalszam}")

#3.4
valasztott = input("3.4 feladat: Írjon be egy szerzőnevet: ")
print(f"{valasztott} könyvei: ")
for konyv in konyvek:
    if valasztott == konyv.szerzo:
        print(f"\t{konyv.cim}")

#3.5
nyomtatott_konyvek = 0
nyomtatott_oldalak = 0
for konyv in konyvek:
    if konyv.ekonyv == 0:
        nyomtatott_konyvek += 1
        nyomtatott_oldalak += konyv.oldalszam

atlag = nyomtatott_oldalak / nyomtatott_konyvek

print(f"3.5 feladat: A nyomtatott kötetek átlagos oldalszáma {round(atlag, 2)} lap.")
