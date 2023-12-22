def addition(a,b):
  return a+b

def subtraction(a,b):
  return a-b

def multiply(a,b):
  return a*b

def divide(a,b):
  return a/b

print("Select the operation for calculate value:\n" 
         "1.Addition (a+b)\n"
         "2.Subtraction (a-b)\n"
         "3.Multiplication (a*b)\n"
         "4.Division s(a/b)\n")

select = int (input("Enter your Choice:"))   
a= int (input("Enter the First Digit:")) 
b= int (input("Enter the Second Digit:")) 

if select == 1:
    print(a,"+",b,"=",addition(a,b))

elif select == 2:
    print(a,"-",b,"=",subtraction(a,b))

elif select == 3:
    print(a,"*",b,"=",multiply(a,b))

elif select == 4:
    print(a,"/",b,"=",divide(a,b))

else:
    print("Please Insert correct Input")              
