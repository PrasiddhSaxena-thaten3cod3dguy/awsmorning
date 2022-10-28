def armstrong(number):
    sumofnum=0
    while(number>0):
        rem=number % 10
        sumofnum = sumofnum + (rem ** 3)
        number = number // 10
    
    return sumofnum


valuetobechecked=int(input("Enter a number: "))
x=armstrong(valuetobechecked)

if valuetobechecked == x:
    print("Armstrong")
else:
    print("Blah")


y=armstrong(780)
print(y)
