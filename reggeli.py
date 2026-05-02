vendegek = int(input("Add meg a vendégek számát! "))
tojasok_raktarban = int(input("Add meg a raktárban lévő tojások  számát! "))

toretlen_tojasok = vendegek * 3
plusztizsszazalek = vendegek / 10 
szukseges_tojasok = toretlen_tojasok + plusztizsszazalek
tojasok_kulonbsege = int(szukseges_tojasok - tojasok_raktarban)

print(f"Vendégek száma: {vendegek} ")
print(f"Raktáron lévő tojások: {tojasok_raktarban}")
print(f"Ennyi vendéghez {int(szukseges_tojasok)} tojásra van szükség")

if szukseges_tojasok < tojasok_raktarban: 
    print("Nem kell több tojást vásárolni.")
else: 
    print(f"Kell még {tojasok_kulonbsege} tojást vásárolni")

