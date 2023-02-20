dct={'France':'Paris','UK':'London','Belarus':'Minsk','Latvia':'Riga'}

def gt (a,**kwargs):
    return kwargs.get(a)

result=print(gt('Belarus',**dct))