import sys
f = open(sys.argv[1])
for line in f:
    print(' '.join(line.strip().split('\t')))
f.close()

#元データ見たら全部タブ区切りだったんで...
# cat file_name | tr '\t' ' '  is same.
