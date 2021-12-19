# NOTE: All code has been commented out.

#####
#Exercise 1: Promt the user to enter their name, then welcome them
#####

#name = input("Please enter your name: ")
#print('Welcome ', name)

#####
#Exercise 2: Prompt the user to enter hours worked and hourly pay, then calculate and return gross pay
#####

#hours = float(input("Enter hours worked: "))
#rate = float(input("Enter pay rate in dollars per hour: "))
#print(hours * rate)

#####
#Exercise 3: Rewrite the pay calculation from Exercise 2 to give the employee 1.5 their hourly pay
#####

#hours = float(input("Enter hours worked: "))
#rate = float(input("Enter pay rate in dollars per hour: "))
#print(hours * (rate * 1.5))

#####
#Exercise 4: Surround the code from Exercise 3 with a Try/Except block to handle non-numeric input
#####

#try:
#	hours = float(input("Enter hours worked: "))
#	rate = float(input("Enter pay rate in dollars per hour: "))
#	print(hours * (rate * 1.5))
#except:
#	print("Invalid input. Non-numerical inputs not allowed.")

#####
#Exercise 5: Read numbers from user until "done" is entered
#####

#num = 0
#total = 0.0
#while True :
#	sval = input('Enter number: ')
	
#	# Check for "done" condition
#	if sval == "done" :
#		break

#	# Check for invalid input
#	try:
#		fval = float(sval)
#	except:
#		print('Invalid Input')
#		continue

#	# Print value
#	print(fval)
#	num = num + 1
#	total = total + fval
#print('All done!')
#print('total: ', total,', average: ', total/num)

#####
# Exercise 6: Parsing text strings
#####

#str = 'S-DSPAM-Confidence: 0.8475' # An example string

## Find the location of a colon in the string
#ipos = str.find(':')
#print(ipos)
#piece = str[ipos + 2:] # Says to start at the index two after the one stored in ipos and loop until the end of the string
#print(piece)
#value = float(piece)
#print(value)

#####
#Exercise 7: Word counting
#####

filename = input('Enter File Name: ')
if len(filename) < 1 :
	filename = 'src\exercises\clown.txt'
file = open(filename)

wordDict = dict()

#for line in file :
#	line = line.rstrip() #Clear whitespace at right of line (removing newline characters)
#	print(line)
#	words = line.split() #Split up the word based on whitespace
#	print(words)
#	for word in words : #Add all of the words to the wordDict dictionary and print the words as we go
#		if word in wordDict :
#			wordDict[word] = wordDict[word] + 1 #Increment the word count if it already exists
#			print('**EXISTING WORD:', word, wordDict[word])
#		else :
#			wordDict[word] = 1 #Add word to dictionary if it isnt already there
#			print('**NEW WORD:', word, wordDict[word])
#print(wordDict) #Print the contents of the wordDict dictionary

#####
#The above is the verbose way. Below is the concise way
#####

#for line in file :
#	line = line.rstrip()
#	words = line.split()

#	for word in words :
#		oldCount = wordDict.get(word, 0) #Checks if a word (key) is in the dictionary. If it is, return the count (value); if not, return 0.
#		print(str(word) + ', Old Count: '+ str(oldCount))
#		newCount = oldCount + 1
#		wordDict[word] = newCount
#		print(str(word) + ', New Count: '+ str(newCount))

#print(wordDict)

#####
#The above is still a bit verbose. Below condenses it some more.
#####

for line in file : 
	line = line.rstrip()
	words = line.split()

	for word in words :
		wordDict[word] = wordDict.get(word, 0) + 1 #This line checks if a word is in the dictionary. If it is, get() returns the current value an this line increments it; if not, get() returns 0 and the statement increments zero by 1.
		#print(str(word) + ', New Count: '+ str(wordDict[word]))

#print(wordDict)

#Now we want to find the largest value
largestCount = -1 #How do I avoid hard-coding a value here? This seems liable to produce errors?
mostCommonWord = None
for word,count in wordDict.items() :
	if count > largestCount :
		largestCount = count
		mostCommonWord = word
print(mostCommonWord, largestCount)