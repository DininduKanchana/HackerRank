def slover(str):
    length = len(str);
    count = 0; 
    for i in range(0, length-1):
        if (str[i] == str[i+1]):
           count = count + 1
    print count;

slover("ABBABBB");


