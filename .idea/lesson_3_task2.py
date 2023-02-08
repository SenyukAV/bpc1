text=input("Input:" ).replace(' ','')
#list(text).remove(' ')
list1=list(text)
some_dict={}
for i in list1:
   some_dict[i]=list1.count(i)
print(some_dict)

