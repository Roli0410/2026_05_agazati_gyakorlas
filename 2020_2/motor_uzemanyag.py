körök = int(input("Add meg a teljesítendő körök számát. "))

fogyasztás = float(input("Add meg az egy körre eső átlagos fogyasztást (l). "))

tartály = int(input("Add meg a motor üzemanyag--tartályának méretét (l). "))

szukseges_uzemanyag = fogyasztás * körök

print(f"Körök száma: {körök}")
print(f"Átlagos fogyasztás körönként (liter): {round(fogyasztás, 2)}")
print(f"A tartály mérete (liter): {tartály}")
print(f"A versenyhez szükséges üzemanyag: {round(szukseges_uzemanyag, 2)}")




if szukseges_uzemanyag <= tartály:
    print("A tartály elegendő a versenyhez!")

else:
    print(f"A tartály NEM elegendő! még {szukseges_uzemanyag - tartály} liter üzemanyag szükséges.")