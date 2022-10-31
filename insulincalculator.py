insulinweight={
    "Insulin1": 5,
    "Insulin2":6,
    "Insulin3":2
}

#WAP to calculate net weight of all the insulins 

theykeys=list(insulinweight.keys())

print(theykeys)
print(type(theykeys))

resultantweight=0
for i in theykeys:
    resultantweight = resultantweight + insulinweight[i]

print(resultantweight)