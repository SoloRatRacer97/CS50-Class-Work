















# We are working with a csv file like this:

# time stamp, title, genere
# 1/3/4 10:00:00AM, The Office, Comedy
# .   .     .     .     .

# ===================== FILTERING =========================
import csv 
titles = []

# Opening a csv file of file_name, and calling it file so we can refference it:
with open("file_name.csv", "r") as file:
      # Still unsure of what the reader is here... We can itterate over it with a for loop for each row, so is it just the list of dictionaries that the file reads for us? Looks like it?
      reader = csv.reader(file)
      # This ignores the first row of the file since it continas titles and what not. 
      next(reader)
      # For printing out each show in the file:
      for row in reader:
            print(row[1])
      
      # ==================================================
      # This is problematic though... row[1] doenst really tell us anything. A name would be a lot better. DictReader will actually let us name that column from the csv file so we can access that with it's name. 
      reader = csv.DictReader(file)
      for row in reader:
            print(row["title"])

      # ==================================================
      # How can we filter out duplicates?
      # We could filter through an array to check if the title is already there and append it to that list IF the title is not found
      
      reader = csv.DictReader(file)
      for row in reader:
            if not row["title"] in titles:
                  titles.append(row["titles"])
      # ==================================================
      # Common problem though, what is there are spaces or weird capital letters in the code? We need to filter these out so we have consistent data from users. 

      # use strip() for white space subtraction
      # user .upper() for uppercase 

      reader = csv.DictReader(file)
      for row in reader:
            title = row["title"].strip().upper()
            if not title in titles:
                  titles.append(title)
      # =====================================================
      # Even better yet, we can make titles a set so that it only takes in values that will not produce duplicates. 

      titles = set()
      # this negates the following code so all we need now is:
      for row in reader:
            title = row["title"].strip().upper()
            titles.add(title)
      # ====================================================
# Now we can sort them alphabetically like this when we print the rows out:

for title in sorted(titles):
      print("title")
# ================= COUNTING EACH INPUT ==================
# We can use a dictionary in python to store key value pairs. Bascially, just think of a chart with two collumns 
import csv

titles = {}

with open("favotires.csv", "r") as file:
      reader = csv.DictReader(file)
      for row in reader:
            title = row["title"].strip().upper()
            # Need to initialize the dictionaries now. The value for each key "title" will be printed in value stored for each "title". These are key value pairs. 
            if not title in titles:
                  titles[title] = 0
            titles[title] += 1

for title in titles:
      print(title, titles[title])

# ============================================================
# This sorts the titles in reverse alphabetical order
for title in sorted(titles, reverse = True):
      print(title, titles[title])

# ================ SORTING THE TALBE ======================
# This will sort the dictionary by the get_value function which returns the value of each title that we have logged. Little weird....
# So we can actually sort by functions in python. I dont know why we cannot just say titles[title] down below and instead, we need write it through a function, but we can do it. 
# Maybe becasue it looks cleaner?
# See below!!!!
def get_value(title):
      return titles[title]

for title in sorted(titles, key = get_value, reverse=True):
      print(title, titles[title])

# ======================== LAMBDA ============================
# Functions that dont have any name. Good for single use functions, like a quick copy and paste.

# Interesting.... the code: lambda title: titles[title] is the same as writing this: def get_value(title):
                  # return titles[title]
# Cool way to tighten up your code. 

for title in sorted(titles, key=lambda title: titles[title], reverse=True):
      print(title, titles[title])

# =================== CLEANING DATA ========================
# cheking if a ceratin input is IN something: 
# Dont count whether or not data == The Office, instead you should cheak whether or not the variable has OFFICE in it. 
# but what if somehting is mispelled? Create a drop down selector of movies like a search bar where it would make you select movies that are already in a repositiory of known movies. 
# May not be good for large projects.... but maybe there would be a clever way of usuing google to filter out the problems? Has this been done before..?

counter = 0

with open("file_name.csv", "r") as file:

      reader = csv.DictReader(file)
      for row in reader:
            print(row["title"].strip().upper())
            if "OFFICE" in title:
                  counter += 1

print(f"Number of people who like the office: {counter}")

# =================== REGULAR EXPRESSIONS ========================
# Good for cleaning up or validating data. Useful for web aplications.
# lets you express patterns in a standardized way. Like formating the input from users so that your data comes in consistently

import csv
import re

counter = 0

with open("file_name.csv", "r") as file:

      reader = csv.DictReader(file)
      for row in reader:
            title = row["title"].strip().upper()
            # This is telling the function to look for "office" in title. In this case, the "office" is the pattern we are searching for
            # ^ means the begining of a string
            # the $ means the end of a string
            # This now says: "At the begining of the string better be OFFICE or THE(any chacater in between)OFFICE, and at the end of the string we need to have nothing?"
            if re.search("^(OFFICE | THE.OFFICE)$", title):
                  counter += 1

print(f"Number of people who like the office: {counter}")

# =================== SEARCHING ========================
# lets you search in the dictionary for how many times a certain title was inputed

import csv

title = input("Title: ").strip().upper()
with open("file_name.csv", "r") as file:

      reader = csv.DictReader(file)
      for row in reader:
            if row["title"].strip().upper() == title:
                  counter += 1
            

print(counter)
# =================== PYTHON WITH SQL ========================

import csv
from cs50 import SQL

db = SQL("sqlite:///favorites.dc")

title = input("Title: ").strip()

# This is writing in a command to the databas to look for anr return how many titles there are that the user is looking for:
rows = db.execute("SELECT COUNT(*) AS counter FROM favorites WHERE title LIKE ?", title)

wor = row[0]

# this was renamed above in the db command
print(row["counter"])

# ========================= INDEXES ================================

# indexed make searching in data structures faster. This is done by putting things into a tree structure. B-Trees?

# We can link tables together in SQL with shared IDs of variables....




