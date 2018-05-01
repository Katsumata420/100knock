import sys
f = open(sys.argv[1])
hoge = list()
lines = list()
for line in f:
    lines.append(line.strip())
    if len(lines) == int(sys.argv[2]):
        hoge.append(lines)
        lines = list()
if lines:
    hoge.append(lines)
f.close()
for num, lines in enumerate(hoge):
    with open('split_{}.txt'.format(num), 'w') as o_F:
        o_F.write('\n'.join(lines))
#split -l N tile_name split_is same.        
