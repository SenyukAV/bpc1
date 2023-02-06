text=input("Input : ").split(' ')
buffer1=text[0]
buffer2=text[-1]
text[0]=buffer2
text[-1]=buffer1
print(text)



