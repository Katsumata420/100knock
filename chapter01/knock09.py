import random
string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
new_string = list()
for word in string.strip().split():
    if len(word) <= 4:
        new_string.append(word)
    else:
        temp = word[0]
        hoge = random.sample(word[1:-1], len(word)-2)
        temp += ''.join(hoge)
        temp += word[-1]
        new_string.append(temp)
print(' '.join(new_string))
