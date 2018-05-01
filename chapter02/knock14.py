import sys
f = open(sys.argv[1])
for num, line in enumerate(f):
    print(line.strip())
    if num+1 == int(sys.argv[2]):
        break
f.close()
#head -n N file_name is same.
