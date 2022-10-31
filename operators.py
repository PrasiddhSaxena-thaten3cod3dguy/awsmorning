'''
1. Arithmetic  (+,-,*,/,//,**)  #BODMAS(Brackets of Division , Multiplication, Addition and Subraction)
2. Comparision
3. Logical
4. Assignment
5.Membership
6. Identity 
'''

# result=(2+3)/2
# print(result)

#Comparision Operator
'''
>
<
==
!=
>=
<=

Generally when we write conditions for if else and loops 
'''

#Logical Operators ==> Logic Gates 

'''
OR GATE TRUTH TABLE

Input A     Input B     Result

1           0           1
0           1           1
1           1           1
0           0           0

AND GATE TRUTH TABLE

Input A     Input B     Result

1           0           0
0           1           0
1           1           1
0           0           0


NOT GATE TRUTH TABLE

INPUT     OUTPUT

1           0
0           1

'''

# a=3
# b=5 

# if not(a>2 and b>6):
#     print("AND GATES WORK even if second case is false")
# else:
#     print("They Dont Work")

# a=True
# if not(a):
#     print("Works")
# else:
#     print("Dont Work")

# rupali=5

# rupali +=1
# rupali -= 3
# # rupali *= 4
# rupali //=5

# print(rupali)

# a=[1,2,3,4,5,6,7,8,9,"blah"]

# print(2 not in a)  #True

# if 2 not in a:
#     print("Works")
# else:
#     print("Dont Works")

#Identity Operator 

# print( 2 is not int)   #TASK
# 

myvalue="Doubt"

print(str(myvalue) + "is of the type"  + str(type(myvalue)))