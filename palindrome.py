def reverseofnumber(number):
    # print(number)
    reverse=0
    while (number>0):
        rem=number % 10
        # print(rem)
        reverse = reverse * 10 + rem
        number=number//10
    return reverse

valuetobechecked=121
x=reverseofnumber(valuetobechecked)
print(valuetobechecked)
print(x)


if valuetobechecked == x:
    print("Palindrome")
else:
    print("Not Palindrome")