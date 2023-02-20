dct={'001':{'name':'Ivan','surname':'Ivanov','tel':'+3751722211133','email':'info@com'},'002':{'name':'Petr','surname':'Petrov','tel':'+3751722211144','email':' '},'003':{'name':'Pavel','surname':'Pavlov','tel':'+3751722211199'}}

def get_empty_email(**kwargs):
    for n in kwargs:
       if kwargs.get(n, {}).get('email') == ' ' or kwargs.get(n, {}).get('email') == None:
           print(kwargs.get(n, {}).get('name'))

get_empty_email(**dct)