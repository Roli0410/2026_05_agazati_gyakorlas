napi_dij = int(input("A napi kölcsönzési díj: "))
kolcs_hossz = int(input("A kölcsönzés hossza napokban:  "))

teljes_dij = napi_dij * kolcs_hossz

kedvezmeny =  (teljes_dij / 100) * 12

print(f"A teljes kölcsönzési díj: {teljes_dij} Ft")

if kolcs_hossz > 21:
    print(f"Az olvasónak járó kedvezmény: {int(kedvezmeny)} Ft.")
else: 
    print("Nem jár kedvezmény az olvasónak.")
