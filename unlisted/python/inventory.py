inventory = {'pack': {'rope': 1, 'torch': 6, 'arrow': 12, 'dagger': 2}, 'hip': {'gold coin': 42, 'dagger': 1}}

def subInventory(location, thing):
	numInventory = 0
	for i, v in location.items():
		numInventory = numInventory + v.get(thing,0)
	return numInventory

print("")
print('Inventory:')
for i, v in inventory.items():
	for j, w in v.items():
		print(j + " - " + str(subInventory(inventory, j)))