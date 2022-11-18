import csv
import sys














def get_maximum_length_substring(s, sub):
# This algo is set to work backwards from the list vs forwards. IDK why though...
# SAME: for(int i = strlen(s)-strlen(sub); i > -1; i--)
      for i in range(len(s) - len(sub), -1, -1):







def main():

      # TODO: Check for command-line usage

      csv_path = sys.argv[1]
      # Opening the file and putting the name data into a variable. 
      with open(csv_path) as csv_file:
            # Reader here becomes the dictionary where the name data is stored  
            reader = csv.reader(csv_file)
            
            # Interesting.... we can open another file within  this with open block AGAIN
            # This is now reading in the text file to be searched. 
            with open(txt_path) as txt_file:
                  s = txt_file.read()


      # TODO: Read database file into a variable

      # TODO: Read DNA sequence file into a variable


      # TODO: Find longest match of each STR in DNA sequence

            
      # make a new dictionary for each of the sequences that we are working on for a key value pair?
      
      # Need to get variable for each sequence to be searched for. Get it from the large.csv? AGATC,TTTTTTCT etc.
      # Need to find where sequence in dnaData starts
            # count how many times it repeats, and add that to a variable to count them
            # if the number of repeats is greater later on, make sure it is updated to that number.
      # longest_sequence = 44

      # TODO: Check database for matching profiles

      # loop through each sequence in the database and look for the sequence key value pairs that we found. 
      # if thery all match, return that name from the database
      # name is row[0][1]......?

      return

main()
