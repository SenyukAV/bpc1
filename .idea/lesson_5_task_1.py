def dec2bin (a):
    list=[]
    n = 0
    while a >= 1:
        if (a % 2 == 0):
            list.append('0')
        else:
            list.append('1')
        a = a / 2
    print(''.join(list[::-1]))



i=int(input("Imput i like dec: "))
dec2bin(i)

k=input("Imput k like bin: ")
def bin2dec (a):
    b=0
    lenght= len(a)
    for i in range(0,lenght):
        b = b + int(a[i]) * (2 ** (lenght - i - 1))
    print(b)

bin2dec(k)




