rekesz=int(input('Adja meg a rendelt rekeszek darabszámát (5-20): '))
alma=int(input('adja meg a mai napon leszüretelt almák darabszámát (1000-2000): '))
teljes=int(alma/120)
if rekesz*120<=alma:
    print('A rendelt mennyiség teljesíthető.')
elif rekesz*120>alma:
    print(f'A rendelt mennyiség nem teljesithető, max {teljes} rekeszt lehet értékesíteni.')
