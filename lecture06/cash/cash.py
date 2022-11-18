






import math

while True:
      n = float(input("Dollars paid: "))
      if n > 0:
            break
n = n * 100
counter = 0
if n > 24:
      counter = math.floor(n / 25)
      n = n % 25
      print(f"Quarter count: {counter}")
if n > 9:
      tempCounter = math.floor(n / 10)
      print(f"Dime count: {tempCounter}")
      n = n % 10
      counter += tempCounter
if n > 4:
      tempCounter = math.floor(n / 5)
      print(f"Nickle count: {tempCounter}")
      n = n % 5
      counter += tempCounter
if n > 1:
      tempCounter = math.floor(n / 1)
      print(f"Penny count: {tempCounter}")
      n = n % 5
      counter += tempCounter
print (f"{counter}")