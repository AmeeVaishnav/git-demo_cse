
def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  if b == 0:
    return "cannot divide by zero"
  return a / b

if __name__ == "__main__":
  print("Calculator App")
  print(f"10 + 5 = {add(10, 5)}")
  print(f"10 - 5 = {subtract(10, 5)}")
  print(f"10 * 5 = {multiply(10, 5)}")
  print(f"10 / 5 = {divide(10, 5)}")
