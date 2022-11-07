print ("hello")


# add
def add( x,y):
  return  x +y
#subtract
def subtract (x,y):
  return  x-y
#multiplication
def multiply (x,y):
  return  x*y        
#division 
def divide (x,y):
   return x/y

print ("select operation.")
print ("select 1 = add")
print ("select 2 = subtract")
print ("select 3 = multiply")
print ("select 4 = Divide")

while True:
    A = input ("Enter a select option of 1,2,3,4 ")
    if A in ('1','2','3','4'):
        number1 =int(input("Enter first number = "))
        number2 =int(input("Enter second number = "))
    if A == '1':
        print (number1, " + ", number2, " = ", add(number1,number2) )
    
    elif A == '2':
        print (number1, " - ", number2, " = ", subtract(number1,number2) )    

    elif A == '3':
        print (number1, " * ", number2, " = ", multiply(number1,number2) )

    elif A == '4':
        print (number1, " / ", number2, " = ", divide(number1,number2) )
        
