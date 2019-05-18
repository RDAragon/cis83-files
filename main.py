"""
NAME: main.py
AUTHOR: Roger Aragon
EMAIL: aragonr87056@student.vvc.edu
DATE: 17 May 2019
DESCRIPTION: generates a list of 10 numbers and calculates the average
"""

import os                    #the OS library is needed for the end of this program
from random import randint   #using "randint" from the random library to generate the numbers   

def create_data_file(filename):     #First, we create the number generator
    outfile = open(filename, 'a')
    for i in range (10):
        outfile.write(str(randint(00,100))+'\n')
    outfile.close()

def get_numbers(filename):          #Next, the means to add the numbers to the file
    myfile = open(filename, 'r')
    numbers = []
    for n in myfile.readlines():
        numbers.append(int(n))
    return numbers



create_data_file('data.dat')        #Now, the file itself is creted...
numbers = get_numbers('data.dat')   #...and populated.

print('The numbers chosen are:',numbers)    #The numbers are displayed
	
print('The sum of the chosen numbers are:',sum(numbers)) #The numbers are added

print('The average of the numbers is',sum(numbers)/10)   #And are calculated to show the average of all generated numbers

os.remove('data.dat')       #Finally, having done its job, the file created can now be deleted
                            #This is done to avoid artifacts from previous iterations
                            #of this program.
