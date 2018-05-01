import sys
f = open(sys.argv[1])
hoge = [x.strip().split() for x in f]
f.close()
with open('col1.txt', 'w') as first, open('col2.txt', 'w') as second:
    for num, column in enumerate([x for x in zip(*hoge)]):
        if num == 0:
            first.write('\n'.join(column))
        elif num == 1:
            second.write('\n'.join(column))
        else:
            break

#print(numpy.transpose(hoge)) is same. (knock05でカッコつけちゃったので...)
#cut -f 1 file_name, cut -f 2 file_name are same.
