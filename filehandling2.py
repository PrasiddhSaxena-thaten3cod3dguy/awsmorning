# sanksar=open("awsmorning2.txt","r")
data='''
Hi ,
My name is Shrikant Shinde!! 
'''
# sanksar.write(data)
# sanksar.close()

with open("awsmorning2.txt","w") as sanskar:
    sanskar.write(data)

print("File Has Been Closed")