import sys
f = open(sys.argv[1])
hoge = {line.strip(): float(line.split()[2]) for line in f}
f.close()
for k, v in sorted(hoge.items(), key=lambda x:x[1]):
    print(k)
#sort -k 3,3 -n file_name is same.
