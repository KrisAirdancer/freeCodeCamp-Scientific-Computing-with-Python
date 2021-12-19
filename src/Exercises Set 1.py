# NOTE: All code has been commented out.

# Exercise 1: Promt the user to enter their name, then welcome them.
"""
name = input("Please enter your name: ")
print('Welcome ', name)
"""
# Exercise 2: Prompt the user to enter hours worked and hourly pay, then calculate and return gross pay
"""
hours = float(input("Enter hours worked: "))
rate = float(input("Enter pay rate in dollars per hour: "))
print(hours * rate)
"""
# Exercise 3: Rewrite the pay calculation from Exercise 2 to give the employee 1.5 their hourly pay
"""
hours = float(input("Enter hours worked: "))
rate = float(input("Enter pay rate in dollars per hour: "))
print(hours * (rate * 1.5))
"""
# Exercise 4: Surround the code from Exercise 3 with a Try/Except block to handle non-numeric input
"""
try:
	hours = float(input("Enter hours worked: "))
	rate = float(input("Enter pay rate in dollars per hour: "))
	print(hours * (rate * 1.5))
except:
	print("Invalid input. Non-numerical inputs not allowed.")
"""
# Exercise 5: Read numbers from user until "done" is entered
"""
num = 0
total = 0.0
while True :
	sval = input('Enter number: ')
	
	# Check for "done" condition
	if sval == "done" :
		break

	# Check for invalid input
	try:
		fval = float(sval)
	except:
		print('Invalid Input')
		continue

	# Print value
	print(fval)
	num = num + 1
	total = total + fval
print('All done!')
print('total: ', total,', average: ', total/num)
"""

#Exercise 6: Parsing text strings
"""
str = 'S-DSPAM-Confidence: 0.8475' # An example string

# Find the location of a colon in the string
ipos = str.find(':')
print(ipos)
piece = str[ipos + 2:] # Says to start at the index two after the one stored in ipos and loop until the end of the string
print(piece)
value = float(piece)
print(value)
"""

#Exercise 7: Word counting

file = input('Enter File Name: ')
if len(file) < 1 : file = 'freeCodeCamp Scientific Computing with Python\clown.txt'
handle = open(file)

for line in handle :
	line = line.rstrip()
	print(line)