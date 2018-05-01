import sys

f = open(sys.argv[1])

for num, _ in enumerate(f):
    a = 1
f.close()
print(num+1)
# wc command is same.
