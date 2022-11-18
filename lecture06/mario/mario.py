

while True:
      n = int(input("Height: "))
      if n > 0 and n < 9:
            break

for j in range(1, n + 1):
      print(" " * (n - j), end = "")
      print("#" * j, end = "")
      print(" ", end = "")
      print("#" * j)