import random
import string

length=int(input("Enter the Length of Password:"))

print('''Choose Complexity of password:
       1.Uppercase
       2.Lowercase
       3.Special Characters
       4.Digits
       5.Exit''')

characterList=" "
while(True):
    choice= int(input("Choose a Complexity Number:"))
    if (choice == 1):
         characterList += string.ascii_letters.upper()
       
    elif (choice == 2):
        characterList += string.ascii_letters.lower()
        
    elif (choice == 3):
         characterList += string.punctuation 
    elif (choice == 4): 
         characterList += string.digits
    elif (choice ==5):   
        break
    else:
        print("Please select valid number!! ")
         
password=[]
for i in range(length):
    randomchar = random.choice (characterList)
    password.append (randomchar)

print("Your Password is : " + "" .join(password))
  



