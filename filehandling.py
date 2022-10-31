# file=open("awsmorning.txt","a")
# thedata="Sanskar is a good hecker!! "
# file.write(thedata)
# file.close()

with open("awsmasters.txt","w") as file:
    thedata="Im noob"
    file.write(thedata)

print("File has been closed")