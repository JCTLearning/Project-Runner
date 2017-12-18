db = [('111', '2'), ('334', '1')] # Our vdot list
Vmiles = '156' # User miles
output = []
x = 0
for miles in db:
	print(miles)
	list = []
	"""
	x is the math
	"""
	x = int(Vmiles) - int(miles[0])
	x = str(x)
	x = x.replace('-', '')
	print(x)
	x = int(x)
	list.insert(0, x)
	list.insert(1, miles[1])
	output.insert(x, list)
	x = x + 1
print(output)
sortedOutput = sorted(output, key = lambda tup: tup[0])
print(sortedOutput)
vdot = sortedOutput[0]
print(vdot[1])
