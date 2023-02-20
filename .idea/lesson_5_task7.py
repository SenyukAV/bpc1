lst=[1,2,3,4,5,6,7,8,9]
def sum (lst1):
    for i in lst1:
        if i==0:
            print(lst1[len(lst1)-1] + lst1[i+1])
        elif i==len(lst1)-1:
            print(lst1[i-1] + lst1[0])
            break
        else:
            print(lst1[i-1] + lst1[i+1])



sum(lst)