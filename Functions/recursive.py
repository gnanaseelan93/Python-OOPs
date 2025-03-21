def sum_of_n(n): #5
    if n==1:
        #base case
        return 1
    else:
        #recursive case
        return n+sum_of_n(n-1) #5+sum_of_n(4) #5+4+sum_of_n(3) #5+4+3+sum_of_n(2) #5+4+3+2+sum_of_n(1) #5+4+3+2+1=15

result=sum_of_n(3) #3+2+1=6
print(result)             


#exampl 2

def factorial(n): #5
    if n==0:
        #base case
        return 1
    else:
        #recursive case
        return n*factorial(n-1) #5*factorial(4) #5*4*factorial(3) #5*4*3*factorial(2) #5*4*3*2*factorial(1) #5*4*3*2*1=120


result=factorial(5) #5*4*3*2*1=120
print(result)
    