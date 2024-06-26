#Ask user for their name
# name = input("What is your name? ")

#Printing message and name on single line
# print("Hello ",end="")
# print(name)
# print(f"Hello {name}")

#adding quoataions within others
# print("Hello 'friend'")
# print("Hello \"friend\"")

#removing white spaces & capitalizing first character for multiple words
# name = input("What is your name? ").strip().title()

#splitting the user's name into first and last names
# first,last = name.split(" ")

# print(f"Hello {first}")


#simple calculator
# x = int(input("What's x? "))
# y = int(input("What's y? "))
# print(x + y)

#rounding off 
# float_number = float(input("Float_Number: "))
# number = round(float_number, 2)
# print(number)

#floats
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x + y)

# print(f"{z:,}") #adding a , separator #1,000

# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = (x / y)

# print(f"{z:.2f}") #rounding off 

##Defining a function
# def intro(name):
#   print(f"Hi there, I'm {name}")

# intro("Gary")

# def hello(to):
#   print("Hello,",to)
  
# name = input("What is your name? ")
# hello(name)

##Default argument
# def hello(to="World"):
#   print("Hello,",to)
  
# name = input("What is your name? ")
# hello()

# def main():
#   name = input("What is your name? ")
#   hello(name) #passes the entered name value to the hello function
  
# def hello(to="World"):
#   print("Hello,", to)

# main()

##Return values
# def main():
#   x = int(input("What is x? "))
#   print("x squared is",square(x)) #calls the square fn and passes it the entered value of x
  
# def square(n):
#   return pow(n, 2) #or n*n or n**2

# main()

##Next 
