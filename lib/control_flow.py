#!/usr/bin/env python3

def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    

def hows_the_weather(temperature):
    if (temperature == 33):
        return "It's brisk out there!"
    else:
        if (temperature == 99):
            return "It's too dang hot out there!"
        else:
            if (temperature == 75):
                return "It's perfect out there!"
            else:
                return "It's a little chilly out there!"
    

def fizzbuzz(num):
    if (num % 3 == 0 and num % 5 == 0) or num == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
        
       #def divide(num1, num2):
  #  try:
  #      quotient = num1 / num2
   #     print(quotient)
  #  except ZeroDivisionError:
  #      print("Error: num2 cannot be equal to 0")
  #  except TypeError:
  #      print("Error: input must be of type int or float")
  #  finally:
  #      print("Isn't division fun?")   

def calculator(operation, num1, num2):
    if (operation == "+"):
        return num1 + num2
    elif (operation == "-"):
        return num1 - num2 
    elif (operation == "*"):
        return num1 * num2 
    elif (operation == "/"):
        return num1 / num2 
    else:
        print("Invalid operation!")
        
    
