try:
    num1=int(input("Enter The Value: "))
    print(num1)
except Exception as e:
    print("You just entered something bad")
    print(e)
print("HAHAHAH")

# num1=int(input("Enter The Value: "))
# print("HAHAH")
# print(num1)

'''
Create a Payroll Systems In which the user will enter basic salary

Case1:- if BS > 10000 then HRA will be 20% of basic salary , Fuel Reinbursement will be 10% of your BS , Entertainemnet will be 5% of your basic Salary , perks and privileges will be 10 % of your basic salary 

Case2:- if BS >= 5000 and <= 10000 the HRA will be 15% of BS , Fuel will be 10% of your BS , Entertainemnet will be 3% of your basic Salary , perks and privileges will be 8 % of your basic salary 


Case3:- if BS < 5000 the HRA will be 8% of BS , Fuel will be 2% of your BS , Entertainemnet will be 0 INR , perks and privileges will be 3 % of your basic salary 

Create the CTC of the employee.
deduct 20% for tax

'''