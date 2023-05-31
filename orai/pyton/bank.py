for i in range(5):
    osszeg=int(input('Adja meg a betenni kívánt összeget: '))
    futamido=int(input('adja meg a betét futamidejét (hónapban) '))
    if futamido>=12:
        print(f'A betett összeg után {osszeg*0.12} kamat jár')
    elif futamido<12:
        print(f'A betett összeg után {osszeg*0.05} kamat jár')
