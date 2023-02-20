lst1=[1,2,3,'qwe',222,'asdff']
result=list(filter(lambda x: isinstance(x,str),lst1))
print(result)