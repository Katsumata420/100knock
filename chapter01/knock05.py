def get_ngram(str_list, num):
    return list(zip(*[str_list[i:] for i in range(num)]))
if __name__ == '__main__':
    print('word bigram', get_ngram('I am an NLPer.'.strip().split(), 2))
    print('character bigram', get_ngram('I am an NLPer.'[::1], 2))
