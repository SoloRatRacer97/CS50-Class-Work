#import cs50
#No cs50 library availbie...?

# to use the 'make' function that we have been using in C, we can now just use something like:
      #> python InClassNotes.py

# Cool way to try differnt things when getting input.. use > try: (then your code)
      # this is helpful when trying to handle different outcomes. See below:

try: 
      x = int(input("x: "))
except ValueError:
      print("That is not an int!")
      exit()
try:
      y = int(input("y: "))
except ValueError:
      print("That is not an int!")
      exit()
print(x+y)

# recall that to using a for loop for X number of itterations, we can use for i in range(x): SOME CODE TO DO SOMETHING

# dont forget about floating point inprecision where certain values of variables can ony be so procise. I forget why... but after a ceratin point 1 / 10 becomes 0.10000000000000004234324. 

# ==============================================
# Lets not forget about module of numbers. It is basically the same thing in C. See below:

n = input("n: ")

if n % 2 == 0:
      print("Even!")
else:
      print("Odd!")


# recall that we do not have anything to define a caracter. All we need to do here now is use a string to get a single chacter. 

s = input("Do you agree? ")

if s =="Y" or s == "y":
      print("Agreed")
      
if s =="N" or s == "n":
      print("Not agreed")
# This isnt super good though, maybe the user types in "Yes" or something


s = input("Do you agree? ")

if s.lower in ["y", "Yes"]:
      print("Agreed")
      
if s.lower =="N" or s == "n":
      print("Not agreed")

# Even better:

s = input("Do you agree? ").lower().somehtingelse.etc...

if s in ["y", "Yes"]:
      print("Agreed")
      
if s.lower =="N" or s == "n":
      print("Not agreed")

# ==============================================
# Function review in python

def main():
      for i in range(3):
            meow()
def meow():
      print("meow")

# Recall that you need to call this function for it to work!
# Alos, this need to be definied at the bottom of the file, not the top. * Still good to name your main file "main"
main()

# ==============================================
def main():
      meow(3)
def meow(n):
      for i in range(n):
            print("meow")
main()

# ==============================================
# There is no do while loop in python... Instead we do this:
while True:
      n = input("How tall? ")
      if n > 0:
            break
for i in range(n):
      print("#")

# ==============================================
# This is really interesting... notice how n is defied inside of the while loop in the second function, but then we can access it after the while loop is finished. This is beacause Python defines a variable for a function and then it is accessable throughout that ENTIRE function. Interesting... No need to definie the variable outside of the loop in the function like saying int n; in C
def main():
      for i in range(n):
            print("#")
def get_height():
      while True:
            n = input("Height: ")
            if n > 0:
                  break
      return n

# ==============================================
# Here we are kind of getting out do while loop from C where we can require that the use inputs a ceratin type of value. If they do not put in an int in this case, we re-promt them for the input becasue of the while loop 
def main():
      height = get_height()
      for i in range(height):
            print("#")


def get_height():
      while True:
            try: 
                  n = input("How tall? ")
                  if n > 0:
                        break
            except ValueError:
                  print("That is not an integer!")
      return n

# ==============================================
# We want to print them out in a row now and not a collumn. 
# print can take a few differnt arguments..... 
# named argument...? called end?
# print usually just makes a \n at the end of the line by default. 
for i in range(4):
      print("?", end = "")

# ==============================================
# this is the same as:
print("?" * 4)


# ==============================================
# quick way to do a for loop:

before = input("Before: ")
print(f"After: {before.upper()}")
# ==============================================
# getting arguments from the user in the command line. 

from sys import argv

if len(argv) == 2:
      print(f"hello, {argv[1]}")
else:
      print("hello, word")

# ==============================================
# here you can make the for loop start at different places depending on the location. Here, we are starting at -1
from sys import argv

for arg in argv[:-1]:
      print(arg)

# ==============================================
# this lets us write other programs and tag the lines with error messages. Here, if the line fails, we get an error code of 1 that we can go back and see where it messed up. If all runs well, we get a 0
from sys import argv, exit

if len(argv) != 2:
      print("Missing command-line argument")
      exit(1)

print(f"hello, {argv[1]}")
exit(0)

# ==============================================
# super fast binary search
# binary search now:

import sys
number = [4, 6, 8, 2, 7, 5, 0]

if 0 in number:
      print("found")
      sys.exit(0)
print("Not found")
sys.ecit(1)

# ==============================================
# fast search for strings

import sys
names = ["Bill", "Chalie", "Joe", "Ron"]

if "Ron" in names:
      print("Found")
      sys.ecit(0)
print("Not found :(")
sys.exit(1)

# ==============================================
# Phone book idea now:
#open {} gives you an empty dictionary. bascially, key value pairs in python. super easy though with the indexing of [] in an array. 
people = {
      "Carter": "1-617-495-3939",
      "David": "+6-234-554-2346"
}

name = input("Name: ")
if name in people:
      number = people[number]
      print(f"Number: {name}")

# ==============================================
# csv file handeling (Comma seperated values)
# we can add data to a csv file here with this code. It will prompt the user for an input and then that input will be added to the file

import csv

file = open("phonebook.csv", "a")

name  = input("Name: ")
number  = input("Number: ")

writer = csv.writer(file)
writer.writerow([name, number)

file.close()
# ==============================================
# the with keyword is useful when doing these types of interactions with files since it helps to keep files open and closed. This will just close the file when the with function is done running. No memory leak!
name  = input("Name: ")
number  = input("Number: ")

with open("phonebook.csv", "a") as file:

      writer = csv.writer(file)
      writer.writerow([name, number)


# ==============================================
# importing data from a google form:
# you can export the data from google forms as a cas file basically. you can do this in the responses tab of the form, take it to google slides, then download it as a csv file, then inport it into 

import csv
houses = {
      "Gryffindor": 0,
      "Hufflepuff": 0,
      "Ravenclaw": 0,
      "Lytherin": 0
} 
#using with to make sure it cloeses when we finish
with open("hogwarts.csv", "r") as file:
      # using the reader function to read the file
      reader = csv.reader(file)
      # Skipping the first variable 
      next(reader)
      # for loop for each row in the file
      for row in reader:
            # giving the row[1] a name
            house = row[1]
            # adding 1 to the dictionary's name for that house
            houses[house] += 1
for house in houses:
      count = houses[house]
      print(f"{house}: {count}")

# ==========================================================
# this one is different since we are using the DictReader function which automatically skips the first entry in the dictionary for us since this is such a common practice. 
import csv
houses = {
      "Gryffindor": 0,
      "Hufflepuff": 0,
      "Ravenclaw": 0,
      "Lytherin": 0
} 
#using with to make sure it cloeses when we finish
with open("hogwarts.csv", "r") as file:
      # using the reader function to read the file
      reader = csv.DictReader(file)
      # for loop for each row in the file
      for row in reader:
            # giving the row[1] a name
            house = row["House"]
            # adding 1 to the dictionary's name for that house
            houses[house] += 1
for house in houses:
      count = houses[house]
      print(f"{house}: {count}")

# =========================================================

