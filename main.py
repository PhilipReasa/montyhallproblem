import random

def runMonteProblem():
	doors = [1,2,3]
	winner = random.choice(doors)  #choose our winning door

	selection = random.choice(doors) #choose the door we want

	doorsToRemove = doors[:]
	doorsToRemove.remove(selection)
	if winner in doorsToRemove:
		doorsToRemove.remove(winner)
	remove = random.choice(doorsToRemove) #pick the door to remove

	doors.remove(remove)
	doors.remove(selection)
	selectionWithSwitch = random.choice(doors) #choose from the other doors

	correctWithoutSwitch = False
	correctWithSwitch = False
	if winner == selection:
		correctWithoutSwitch = True

	if winner == selectionWithSwitch:
		correctWithSwitch = True

	return (correctWithoutSwitch, correctWithSwitch)

count = 0
winsWithSwitch = 0
winsWithoutSwitch = 0

for index in range(1000000):
	results = runMonteProblem()
	if results[0]:
		winsWithoutSwitch += 1

	if results[1]:
		winsWithSwitch += 1

	count += 1;

print "iterations %d" % count
print "wins with switching %d" % winsWithSwitch
print "wins without switching %d" % winsWithoutSwitch



