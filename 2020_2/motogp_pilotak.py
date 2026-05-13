import statistics

class Pilota():
    def __init__(self , nev , csapat , orszag , rajtszam , pontszam):
        self.nev = nev
        self.csapat = csapat
        self.orszag = orszag
        self.rajtszam = rajtszam
        self.pontszam = pontszam

pilotak = []

with open('C:/Users/MullerGabor/Documents/GitHub/2026_05_agazati_gyakorlas/2020_2/pilotak.txt', 'r', encoding='utf-8') as forrasfajl:
        for sor in forrasfajl:
            adatok = sor.strip().split(';')
            pilota =  Pilota(adatok[0] , adatok[1] , adatok[2] , int(adatok[3]) , int(adatok[4]))
            pilotak.append(pilota)


print(f"3.2 feladat: Az állományban {len(pilotak)} adatai szerepelnek.")

legtobb_pontszamu = pilotak[0]

for i in pilotak:
    if i.pontszam > legtobb_pontszamu.pontszam:
        i = legtobb_pontszamu

print(f"3.3 feladat: a legtöbb pontot szerző pilóta:")
print(f"Név: {legtobb_pontszamu.nev}")
print(f"Csapat: {legtobb_pontszamu.csapat}")
print(f"Nemzetiség: {legtobb_pontszamu.orszag}")
print(f"Rajtszám: {legtobb_pontszamu.rajtszam}")
print(f"Pontszám: {legtobb_pontszamu.pontszam}")


valasztott =  input("3.4 feladat: Írjon be egy csapatnevet: ")
print(f"A {valasztott} pilótái")
for x in pilotak:
    if valasztott == x.csapat:
        print(x.nev)


spanyolok = 0
spanyol_pontszam = 0

for u in pilotak:
    if u.orszag == "spanyol":
        spanyolok += 1
        spanyol_pontszam += u.pontszam 

atlag = spanyol_pontszam / spanyolok

print(f"3.5 feladat: A spanyol pilóták átlagos pontszáma {round(atlag, 2)}")



