loop = 0
while loop <= 5:
    print('loop count is: ' + str(loop))
    if loop == 3:
        print('Control in if.')
        loop = loop + 1
        continue
    else:
        print('Control in else.')
        loop = loop + 1
print('loop ended')
