exercises = 0
  
while exercises < 99:
  
  Exercises=int(input("Enter the number of the exercise you want to run or enter the number 99 for end: "))
  if exercises == 1:
    #Calculate the area of a triangle
    Base=int(input("Enter the base of the triangle: "))
    height=int(input("Enter the height of the triangle: "))
    Area=Base*height/2
    print("The area of the triangle is: ",Area)
  elif exercises == 2:
    #Addition of two numbers
    first=int(input("Enter a number: "))
    second=int(input("Enter another number: "))
    addition=first+second
    print("The sum of the 2 numbers is: ",addition)
  elif exercises == 3:
    #The square of a number
    Number=int(input("Enter a number: "))
    Square=Number*Number
    print("The square of the number is: ",Square)
  elif exercises == 4:
    #Sum of 1234 y 532
    number1= 1234
    number2= 532
    Sum=number1+number2
    print("The sum of 1234 + 532 is: ",Sum)
  elif exercises == 5:
    #subtract between 1234 and 532
    number1=1234
    number2=532
    subtract=number1-number2
    print("the result of the subtraction: 1234 - 532 is: ",subtract)
  elif exercises == 6:
      #Multiplication between 1234 and 532
    number1=1234
    number2=532
    multiplication=number1*number2
    print("the result of the multiplication: 1234 x 532 is: ",multiplication)
  elif exercises == 7:
    #Division between 1234 y 532
    number1=1234
    number2=532
    Division=number1/number2
    print("The result of the division: 1234 / 532 is: ",Division)
  elif exercises == 8:
    #Module of 1234 between by 532
    Number1=1234
    Number2=532
    Module=Number1%Number2
    print("The Module of 1234 between by 532 is: ",Module)
  elif exercises == 9:
    #Conversion from euros to dollars
    Euro=float(input("Enter the euro: "))
    Conversion=Euro*1.10
    print("in dollars that equals: ",Conversion)
  elif exercises == 10:
    #Area of a rectangle
    Broad=float(input("Enter the width of the rectangle: "))
    Height=float(input("Enter the height of the rectangle: "))
    Area=Broad*Height
    print("The area of the rectangle is: ",Area)
  elif exercises == 11:
    #area and perimeter of a square
    Lado=int(input("Enter the side of the square: "))
    #Area
    Area=Lado*Lado
    print("The area of the square is: ",Area)
    #Perimeter
    Perimeter=Lado*4
    print("The perimeter of the square is: ",Perimeter)
  elif exercises == 12:
    #Area and volume of a cylinder
    Radio=int(input("Enter the radius: "))
    Height=int(input("Enter the height: "))
    #Area
    Area=2*3.1416*Radio*(Radio+Height)
    print("the area of the cylinder is: ",Area)
    #Volume
    Volume=3.1416*Radio*Radio*Height
    print("The volume of the cylinder is: ",Volume)
  elif exercises == 13:
    #Area and length of a circle
    Radio=int(input("Enter the radius of the circle: "))
    #Lenght
    Lenght=2*3.1415926536*Radio
    print("The length of the circle is: ",Lenght)
    #Area
    Area=3.1415926536*Radio*Radio
    print("The area of the circle is: ",Area)
  elif exercises == 14:
    #average of three numbers
    numero1=int(input("Enter the first number: "))
    numero2=int(input("Enter the second number: "))
    numero3=int(input("Enter the third number: "))
    Promedio=(numero1+numero2+numero3)/3
    print("The average of the three numbers is: ",Promedio)
    exercises=int(input("Enter the number of the exercise you want to run: "))

  elif exercises==17:
    #A number is positive or negative
    number = float(input("Enter a number: "))
    if (number > 0): 
      print("The number" + str(number) + " Is positive")
    else:
      print("The number " + str(number) + " Is positive")
  
  elif exercises==18:
    #The greatest and least number
    number1 = float(input("Enter a number: "))
    number2 = float(input("Enter another number: "))
    if (number1>number2):
      print("The number", number1, "Is the eldest: ")
    elif (number2>number1):
      print("The number", number1, "Is the eldest:")
  
  elif exercises==19:
    #The largest number and the smallest among three numbers
    number1 = float(input("Enter a number: "))
    number2 = float(input("Enter another number: "))
    number3 = float(input("Enter another number: "))
    if (number1 > number2 > number3):
      print("The number", number1, "It is the largest and the number ", number3, "It is the smallest t")
    elif (number1 > number3 > number2):
      print("The number", number1, "It is the largest and the number ", number2, "It is the smallest ")
    elif (number2 > number1 > number3):
      print("The number", number2, "It is the largest and the number", number3, "It is the smallest ")
    elif (number3 > number1 > number2):
      print("The number", number3, "It is the largest and the number ", number2, "It is the smallest ")
    elif (number2 > number3 > number1):
      print("The number", number2, "It is the largest and the number ", number1, "It is the smallest ")
    else:
      print("The number", number3, "It is the largest and the number ", number1, "It is the smallest ")
  
  elif exercises==20:
    #Employee salary
    name = input("Please enter your name: ")
    hours = float(input("Please Enter normal hours worked: "))
    additional = float(input("Please enter the number of overtime hours worked: "))
    if (additional==0):
      print(name, "his salary is", hours*4)
    elif (additional >0):
      print(name, "his salary is",(hours*4)+(additional*8))
  
  elif exercises==21:
    #Addition or subtraction of two numbers
    number1 = float(input("Please enter a  (A): "))
    number2 = float(input("Please enter another number (B): "))
    if (number1 > number2):
      print("The subtraction of the numbers is: ", number1-number2)
    elif (number2 > number1):
      print("The addition of the numbers is: ", number1+number2)
  
  elif exercises==22:
    #Quotient of two numbers
    number1 = float(input("Please enter a number (A): "))
    number2 = float(input("Please enter another number (B): "))
    if (number2 > 0):
      print("The quotient between these two numbers is:", number1/number2)
    elif (number2 == 0):
      print("The division is not valid since whatever value our answer is, we will have to admit that this value multiplied by 0 is equal to 1, and that cannot be true, because anything multiplied by 0 is 0.")
  elif exercises ==23:
    #Day of the week
    numberD = int(input("Enter the number of the day of the week (1-7): "))
    if numberD == 1:
      print("Monday")
    elif numberD == 2:
      print("Tuesday")
    elif numberD == 3:
      print("Wednesday")
    elif numberD == 4:
      print("Thursday")
    elif numberD == 5:
      print("Friday")
    elif numberD == 6:
      print("Saturday")
    elif numberD == 7:
      print("Sunday")
    
  elif exercises==24:
    #Equilateral triangle
    number1 = float(input("Please enter the measurement of the first length: "))
    number2 = float(input("Please enter the measurement of the second length: "))
    number3 = float(input("Please enter the measurement of the third length: "))
    if number1 == number2 and number1 == number3:
      print("The triangle is equilateral ")
    elif (number1 != number2 or number1 != number3 or number2 != number3):
      print("The triangle is not equilateral ")
  
  elif exercises==25:
    #Addition or multiplication of two numbers
    number1 = float(input("Please enter a number (A): "))
    number2 = float(input("Please enter another number (B): "))
    if (number1 <0 or number2 <0):
      addition = number1 + number2
      print ("The addition of the two numbers is: ",addition)
    elif (number1 >0 or number2 >0):
      multiplication= number1 * number2
      print ("The multiplication of the two numbers is: ",multiplication)
  
  elif exercises==26:
    #Zodiac signs
    day = int(input("enter your day of birth: "))
    month = int(input("enter the number of the month of your birth: "))
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
      print("Acuario")
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
      print("Piscis")
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
      print("Aries")
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
      print("Tauro")
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
      print("Geminis")
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
      print("Cancer")
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
      print("Leo")
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
      print("Virgo")
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
      print("Libra")
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
      print("Escorpio")
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
      print("Sagitario")
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
      print("Capricornio")
  
  elif exercises==27:
    #Area and perimeter of a quadrilateral
    base = float(input("Please enter the base of the quadrilateral: "))
    height = float(input("Please enter the height of the quadrilateral: "))
    #Squaare
    if (base == height):
      perimeter = base*4
      area = base*height
      print("This figure is a square, its perimeter is ",perimeter, "and its area is ",area)
    #Rectangle
    elif (base != height):
      perimeter1 = (base*2)+(height*2)
      area1 = (base*height)
      print("This figure is a rectangle, its perimeter is ",perimeter1, "and its area is",area1)
      
  elif exercises==28:
    #Discounts
      sale = float(input("Please enter the sale price: "))
    #Discount 5%
      if (sale < 100.0):
        discount = sale*5/100
        price = sale - discount
        print("Your discount is 5% which is equivalent to ",discount, "and your purchase remains in ",price)
      #Discount 10%
      elif (sale>100 or sale==100) and (sale<200):
        discount1  = sale*10/100
        price1 = sale - discount1
        print("Your discount is 10% which is equivalent to ",discount1, "and your purchase remains in ",price1)
      elif (sale > 200 or sale == 200):
        discounT = sale*15/100
        pricE = sale - discounT
        print("Your discount is 15% which is equivalent to ",discounT, "and your purchase remains in ",pricE)
  
  elif exercises == 29:
    #Know if a year is a leap year
    year = int(input("Please enter the year: "))
    if not year % 4 and (year % 100 or not year % 400):
      print("The year is leap")

  elif exercises == 30:
    #Multiples of 3 up to 100
    for i in range (3, 100, 3):
      print (i)
  elif exercises == 31:
    #Odd numbers between 1 and 100
    for i in range (1, 100, 2):
      print (i)
  elif exercises == 32:
    #even numbers between 0 and 100
    for i in range (2, 102, 2):  
      print (i)
  elif exercises == 33:
    for i in [1]: 
      print ("1\n2\n3\n")
  elif exercises == 34:
    #Numbers from 10 to 1
    for i in range (10, 0, -1):  
      print (i)
  elif exercises == 35:
    #squares of numbers from 1 to 30
      for i in range (1,31):
        print(i*i)
  elif exercises == 36:
    #addition of the squares of the first hundred numbers natural
    addition = 0
    for i in range (1,100):
      print(i*i)
      addition += i*i
    print("The sum of the squares of these numbers is " + str(addition))
  elif exercises == 37:
    #addition of the following hundred numbers
    number=int(input("Enter a number: "))
    addition = 0
    for i in range (number, (number + 101) ):
      print(i)
      addition += i
    print("The sum of the squares of these numbers is " + str(addition))
  elif exercises == 38:
    #factorial number of a number
    def factorialNoRecursivo(n):
      fac  = int(1)
      for i in range (1,n+1):
         fac = fac * i
      return fac
    for i in range (1,11):
      number=int(input("Enter a number: "))
      print ("The factorial of the number is: " + str(factorialNoRecursivo(number)))