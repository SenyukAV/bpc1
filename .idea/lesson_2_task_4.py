one=input("Input nuber 1: ")
two=input("Input nuber 2: ")
three=input("Input nuber 3: ")
number=[int(one),int(two),int(three)]
n=0
m=0
for i in number:
    if i < 0:
        n=n+1
    else:
        m=m+1

print("Numbers less than zero :",n,"Numbers greater than zero :",m)


