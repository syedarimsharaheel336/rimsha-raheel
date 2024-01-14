print("mini calculator")
num1=int (input("enter your value 1:"))
num2=int (input("enter your value 2:"))
print ("press + for addition/npress - for substraction/npress * for multiplication/npress / for division")
choice=input ("enter the choice for +-*/:")
if choice =='+':
    print (num1 + num2)
elif choice =='-':
    print (num1 - num2)   
elif choice =='*':
    print (num1 * num2) 
elif choice =='/':
    print (num1 / num2)
else:
    print("invalid choice")
