import sys
import collections
f = open(sys.argv[1])
hoge = collections.defaultdict(int)
for line in f:
    hoge[line.split()[0]] += 1
f.close()
for k, v in sorted(hoge.items(), key=lambda x:x[1], reverse=True):
    print(k, v)
#cut -f 1 file_name | sort | uniq -c | sort -nr is same.
