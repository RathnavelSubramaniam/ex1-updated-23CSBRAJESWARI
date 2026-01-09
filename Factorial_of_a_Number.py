num = int(input("Enter a Number: "))
factorial= 1
if num<0:
    print("facrorial does not exist for negative numbers")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("factorial of",num,"is",factorial)    

