import random

def simulateMontyHallProblem():
	# You start with your choice of three doors
	doors = {1,2,3}

	# Behind one of them is a fabulous prize
	winner = random.sample(doors, 1)[0]

	# You get to pick which door you think holds this treasure
	selection = random.sample(doors, 1)[0]

	# The host opens one of the other two doors.
	doorsThatCanBeOpened = doors.copy()
	doorsThatCanBeOpened.discard(selection) ## not your door
	doorsThatCanBeOpened.discard(winner)	## the host cannot open the winning door
	doorToOpen = random.sample(doorsThatCanBeOpened, 1)[0]
	doors.remove(doorToOpen)

	# The big question: Do you switch doors?
	correctWithoutSwitch = False
	if winner == selection:
		correctWithoutSwitch = True

	return (correctWithoutSwitch, not correctWithoutSwitch)

# Run the Monty Hall problem 1,000,000 times!
RUN_COUNT = 1000000
winsWithSwitch = 0
winsWithoutSwitch = 0

for index in range(RUN_COUNT):
	results = simulateMontyHallProblem()
	if results[0]:
		winsWithoutSwitch += 1

	if results[1]:
		winsWithSwitch += 1

print "iterations %d" % RUN_COUNT
print "wins with switching %d" % winsWithSwitch
print "wins without switching %d" % winsWithoutSwitch
