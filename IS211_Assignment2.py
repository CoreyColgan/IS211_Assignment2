#!/usr/bin/env python
# coding: utf-8

# In[11]:
from urllib.request import urlopen
import csv
import datetime
import logging
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--url", help = "Please enter URL for CSV data.")
args = parser.parse_args()

logging.basicConfig(filename='assignment2_errors.log', level=logging.ERROR)
logger = logging.getLogger('assignment2')

    
def main():
    if not args.url:
        print ('No URL entered')
        raise SystemExit
    try:
        csvData = downloadData(args.url)
    except urllib2.URLError:
        print ('Invalid URL')
    else:
        personData = processData(csvData)
        chooseID = raw_input('Please enter user ID:')
        print (chooseID)

        chooseID = int(chooseID)

        if chooseID <= 0 or chooseID > 100:
            print ('Invalid entry')
            raise SystemExit
        else:
            displayPerson(chooseID, personData)
            main()

            
# Write a function called ​downloadData​, which takes in a string called ​url​. 
# The purpose of this function isto download the contents located at the ​url​ and return it to the caller. 

def downloadData(url):
   
    content = urllib.urlopen(url)
    return content

#Write a function called ​processData​, which takes the contents of the file as the first parameter, processes the 
#file line by line, and returns a dictionary that maps a person’s ID to a tuple of the form (name, birthday).

def processData(content):
  
    csv_file = csv.DictReader(content)
    Dictionary = {}

    for num, line in enumerate(csv_file):
        try:
            born = datetime.datetime.strptime(line['birthday'], '%d/%m/%Y')
            Dictionary[line['id']] = (line['name'], born)
        except:
            logging.error('Error -- line #{} for ID# {}'.format(num, line['id']))

    return Dictionary

# Write a function called ​displayPerson​, which takes in an integer called ​id​ as its first parameter,
# and adictionary as its second parameter, called ​personData​. The purpose of this function is to print the 
# name and birthday of a given user identified by the input ​id​.

def displayPerson(id, personData):
    uniqueID = str(id)
    if uniqueID in personData.keys():
        print ('ID# {} = {}, their birthday is {}'.format(id, personData[uniqueID][0], datetime.datetime.strftime(personData[uniqueID][1], '%Y-%m-%d')))
    else:
        print ('No person matches ID#. Enter another.')
        

if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:





# In[ ]:




