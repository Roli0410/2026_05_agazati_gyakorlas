print("3. feladat: ")

class Urhajos():
    def __init__(self , nev_, orszag_ , nem_ , szulev_ , urido_ ):
        self.nev = nev_
        self.orszag = orszag_
        self.nem = nem_
        self.szulev = szulev_
        self.urido = urido_


urhajosok = []
with open('urhajos.txt' , "r" ,  encoding="utf-8" ) as forrasfajl:
        next(forrasfajl)
        for sor in forrasfajl:
            adatok = sor.strip().split(";")
            urhajos = Urhajos(adatok[0], adatok[1], adatok[2], int(adatok[3]), int(adatok[4]) )
            urhajosok.append(urhajos)



print(f"3.4. feladat: Az állományban {len(urhajosok)} űrhajós adatai találhatók.")

van_olasz = False
for i in urhajosok: 
    if i.orszag  == "ITA": 
        van_olasz = True
        break

if van_olasz == True:
    print("3.5. feladat: Az űrhajósok között van olasz származású.")

else: 
    print("3.5. feladat: Az űrhajósok között nincs olasz származású.")

osszeg = 0
db = 0

for i in urhajosok:
    if i.nem == "N":
        osszeg += i.urido
        db += 1

atlag = osszeg / db

print(f"3.6. feladat: A női űrhajósok átlagosan {atlag } napot töltöttek az űrben.")

legfiatalabb = urhajosok[0]

for i in urhajosok: 
    if i.szulev > legfiatalabb.szulev:
        legfiatalabb = i

print(f"3. 7. feladat: A legfiatalabb űrhajós: \n Neve: {legfiatalabb.nev} \n Országa: {legfiatalabb.orszag} \n Neme: {legfiatalabb.nem}\n Születési éve: {legfiatalabb.szulev}\n Űrben töltött ideje: {legfiatalabb.urido} nap")