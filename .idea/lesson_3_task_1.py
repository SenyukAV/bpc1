m=input("Input :")
n=0
number=[]
while(n<int(m)):
    number.append(2**n)
    n=n+1

print(number)

number2=[2**i for i in range(int(m))]
print(number2)


