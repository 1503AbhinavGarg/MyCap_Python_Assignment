a=input("Please Enter a string: ")
def most_frequent(a):
    b=dict()
    for i in a:
        if i not in b:
            b[i]=1
        else:
            b[i]+=1
    return(b)
c=most_frequent(a)
print(c)
