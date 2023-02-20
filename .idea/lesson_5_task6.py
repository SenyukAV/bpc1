lst=[1,2,3,4,5,6,7,88,9]

print(list(filter(lambda z: z%2==0,lst))+list(filter(lambda z: z%2!=0,lst)))