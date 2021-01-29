#**************************************************************
# *
# * Program: Tu_Lam_hw3_a.py
# * Author: Tu Lam
# * Date: January 28th, 2021
# * Description: The program is implement to ask the user to 
# * 				  enter in a year and then use that number to 
# *				  calculate if it's a leap year or not. (No Error Handle)
# *
#**************************************************************

year = 0;										# Create a variable to hold 0 as a temp holder for the year

print("\nThe Leap Year Calculator");	# The title of the program
print("------------------------\n");

year = int(input("Please enter a year you want: "));		# Enter in the year

print("\nThe Answer: ");
# Start to calculate for the leap year
if ((year % 4) == 0):			# If it is divisible by 4
	print "The year", year, "is a leap year!";
if ((year % 400) == 0):			# If it is divisible by 400
	print "The year", year, "is a leap year!";
if ((year % 100) == 0):			# If it is divisible by 100
	print "The year", year, "is not a leap year. Sorry!";
else:									# If nothing else match
	print "The year", year, "is not a leap year. Sorry!";
print("\n");
