
lst=[1,2,3,4,5,6,7]
n=int(input("Input n: "))
def displacement (a,args):
    args=args[-a:] + args[:-a]
    print(args)

displacement(n,lst)