i=int(input("Input i :"))
p=1
for n  in range(2,i+1):
    if(n%2==0):
        print(n,end='')
        p=p+1
        if p>5:
            p=1
            print(" ")





