f1 = open('col1.txt')
f2 = open('col2.txt')
with open('col12.txt', 'w') as o_f:
    for c1, c2 in zip(f1, f2):
        o_f.write('{}\t{}\n'.format(c1.strip(), c2.strip()))
f1.close()
f2.close()
#paste col1.txt col2.txt
