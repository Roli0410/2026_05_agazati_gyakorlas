import random


# def kozte(szam, also, felso):
#     if also<= szam<=felso:
#         return True
#     else: 
#         return False 

# db = 0
# dobasok_szama = 150

# for i in range(dobasok_szama):
#     dobas = random.randint(1,  12)

#     if kozte(dobas, 4, 8):
#         db += 1 

# szazalek = (db / dobasok_szama) * 100

# print(f"Az {dobasok_szama} dobásból {db} esett 4 és 8 közé. ")
# print(f"Ez az összes dobás {szazalek: .2f}%-a.")


# havas megoldasa

def kozte(a, b, c):
    if a >= b and a <= c:
        return True
    else:
        return False


db = 0
for i in range(150):
    szam = random.randint(1, 12)
    if kozte(szam, 4, 8):
        db += 1

print(db)

szazalek = round(db / 150 * 100, 2) 

print(szazalek)