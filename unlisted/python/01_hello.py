# This program says "hello" and asks for my name, then uses it.

print ('Hello, world!')	# Print statement.

print ('What is your name?') # Ask for their name.
myName = input()	# grab their name
print('It is good to meet you, ' + myName + ".")
print('The length of your name is ' + str(len(myName)) + ' characters.')

print('What is your age?')
myAge = input()
print ('You will be ' + str(int(myAge)+1) + ' next year.')