catNames = []

while True:
	print ('Enter the name of cat №' + str(len(catNames)) + ' (or press ENTER to stop). : ')
	name = input()
	if name == '':
		break
	catNames = catNames + [name] # list concatenation
print('The cat names are: ')
for name in catNames:
	print('   ' + name)