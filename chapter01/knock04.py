string = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
hoge=[1, 5, 6, 7, 8, 9, 15, 16, 19]
ans = dict()
for num, word in enumerate(string.strip().split()):
    if num+1 in hoge:
        ans[word[0]]=num+1
    else:
        ans[word[0:2]]=num+1
print(ans)
