import sys
f = open(sys.argv[1])
hoge = set()
for line in f:
    hoge.add(line.split()[0])
f.close()
print(hoge)
#sort col1.txt | sort is same.
