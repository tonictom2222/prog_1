rekesz=int(input('hány rekesz-t rendeltél csöcs?? '))
alma=int(input('mennyi alma van gec?? '))
if alma//(rekesz*120):
    print('a rendelés teljesíthető')
else:
    print(f'nem teljesíthető, max {alma//120} teljesíthető')