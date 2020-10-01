#Python Program to find Sum and Average of N Natural Numbers
 
n=int(input("Please Enter any Number: "))
total = 0

for i in range(1, n+1):
    total = total + i

avg = total / n

print("The Sum of first ",n," Natural Numbers is : ",total);
print("The Average of first ",n," Natural Numbers is : ",avg);
