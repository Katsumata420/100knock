import sys
f = open(sys.argv[1])
hoge = [x.strip() for x in f]
f.close()
for line in hoge[len(hoge)-int(sys.argv[2]):]:
    print(line)
#tail -n N file_name is same.
