import knock05
str1='paraparaparadise'
str2='paragraph'
X = set(knock05.get_ngram(str1[::1], 2))
Y = set(knock05.get_ngram(str2[::1], 2))
print('X:', X)
print('Y:', Y)
print('X or Y:', X|Y)
print('X and Y:', X&Y)
print('X - Y:', X-Y)
if ('s', 'e') in X:
    print('X include "se"')
if ('s', 'e') in Y:
    print('Y include "se"')
