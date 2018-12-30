y = int(input()) - 2018

if y == 0:
    print('yes')
else:
    startMonth = y * 12 + 1
    endMonth = startMonth + 11
    optimal = 4 

    while optimal < startMonth:
        optimal += 26

    if optimal <= endMonth:
        print('yes')
    else:
        print('no')
