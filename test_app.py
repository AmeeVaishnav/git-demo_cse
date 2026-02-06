import pytest
from app import add, subtract, multiply, divide

def test_add():
  assert add(2, 3) == 5
  assert add(-1, 1) == 0
  print("Add Tests passed")

def test_subtract():
  assert subtract(5, 2) == 3
  assert subtract(10, 10) == 0
  print("Subtract Tests passed")
  
def test_multiply():
  assert multiply(3, 4) == 12
  assert multiply(0, 5) == 0
  print("Multiply Tests passed")

def test_divide():
  assert divide(10, 2) == 5
  assert divide(0, 5) == 0
  assert divide(5, 0) == "Cannot divide by zero"
  print("Divide Tests passed")

if __name__ == "__main__":
  test_add()
  test_subtract()
  test_multiply()
  test_divide()
  print("\n All tests passed!!")
