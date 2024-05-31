#Create a simple calculator using Python
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    return"Error: Cannot divide by zero."
  else:
    return x / y

def main():
  while True:
    print("Select operation:\n"
          "1. Add\n" \
		      "2. Subtract\n" \
	        "3. Multiply\n" \
		      "4. Divide\n")
    

    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    
    if choice == '1':
      result = add(num1, num2)
      print(num1, "+", num2, "=", result)
    elif choice == '2':
      result = subtract(num1, num2)
      print(num1, "-", num2, "=", result)
    elif choice == '3':
      result = multiply(num1, num2)
      print(num1, "*", num2, "=", result)
    elif choice == '4':
      result = divide(num1, num2)
      print(num1, "/", num2, "=", result)
    else:
      print("Invalid Input")

if __name__ == "__main__":
  main()
