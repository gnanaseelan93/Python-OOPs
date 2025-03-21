arr = [1,2,3,4,5,6,7,8,9,10]
odd = []
even = []

#method 1

for i in arr:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print('odd:',odd)
print('even:',even)

#method 2
odd = [i for i in arr if i%2!=0]
even = [i for i in arr if i%2==0]
print('odd:',odd)
print('even:',even)
