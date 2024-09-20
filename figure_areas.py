def rectArea():
      a = float(input("Width:"))
      b = float(input("Length:"))
      print("Area of your rectangle is: ", a * b)
      return

def sqrArea():
      a = float(input("Width:"))
      print("Area of your square is: ", a * a, "\n")
      return

def triArea():
      a = float(input("Base:"))
      h = float(input("Height:"))
      print("Area of your triangle is: ", (h * a)/2, "\n")
      return

def trapArea():
      a = float(input("Top:"))
      b = float(input("Base:"))
      h = float(input("Height:"))
      print("Area of your trapeze is: ", ((a + b)/2)*h, "\n")
      return


while True:
      print("Please choose your figure:\n"
            "1. Rectangle\n"
            "2. Square\n"
            "3. Triangle\n"
            "4. Trapeze\n"
            "5. Circle\n"
            "6. EXIT")
      choice = input()

      if (choice == "1"):
            rectArea()
      elif (choice =="2"):
            sqrArea()
      elif (choice =="3"):
            triArea()
      elif (choice =="4"):
            trapArea()
      else:
            exit()