myName = input('What is your name? ')
myAge = int(input('What is your age? '))

if myName == 'Alice':
	print('Hello, Alice.')
elif myAge < 12:
	print('You are not Alice, child.')
elif myAge > 2000:
	print('Unlike you, Alice is not an undead, immortal vampire.')
elif myAge > 100:
	print('You are not Alice, granny.')
else:
	print('You are neither Alice, nor a child, nor a granny, nor an undead immortal vampire.')