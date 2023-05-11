szo=input('szo: ')
for i in range(len(szo)):
    print(szo[:i+1])

for i in range(len(szo)):
    for j in range(i):
        print(' ',end='')
    print(szo[i])