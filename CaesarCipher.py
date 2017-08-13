def encryptCaesar(s, k):
    s = list(s)
    l = len(s)
    for i in range (0, l):
        charactor = s[i]
        ascii = ord(charactor)

        if charactor.islower():
            if (ascii + k > 122):
                m = (ascii + k) % 122
                s[i] = chr( 97 + m)
            else:
                s[i] = chr(ascii + k)
    print s;



if __name__ == '__main__':
   s = raw_input()
   k = input()
   print encryptCaesar(s, k)
