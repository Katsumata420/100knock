def cipher(string):
    return [chr(219-ord(x)) if 97 <= ord(x) <= 123 else x for x in string[::1]]
if __name__ == '__main__':
    string = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    print(''.join(cipher(string)))

