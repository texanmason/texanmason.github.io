birthdays = {'Alice': 'April 1', 'Bob': 'December 12', 'Carol': 'March 4'}

while True:
	print('Enter a name: (blank to quit)')
	name = input()
	if name == '':
		break
	if name in birthdays:
		print(name + ' was born on ' + birthdays[name] + '.')
	else:
		print('I do not have birthday information for ' + name + '.')
		print('What is their birthday?')
		bday = input()
		birthdays[name] = bday
		print('Birthday database updated.')