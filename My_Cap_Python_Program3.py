a=int(input("Enter the number of terms :"))
n1=0
n2=1

if (a<=0):
    print("Please enter positive number.")

else:
    print("Fibonacci Numbers:")
    for i in range(0,a):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        i=i+1
