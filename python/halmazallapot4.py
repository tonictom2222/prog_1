while True:
    viz= float(input('Víz hőmérséklete: '))

    if viz>= 100:
        print('légnemű')
    elif viz< 0:
        print('szilárd')
    else:
        print('folyékony')
