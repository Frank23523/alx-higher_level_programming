#!/usr/bin/python3
for ones in range(0, 10):
    for tens in range(ones + 1, 10):
        if ones == 8 and tens == 9:
            print('89')
        else:
            print('{}{}, '.format(ones, tens), end='')
