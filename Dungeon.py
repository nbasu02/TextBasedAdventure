from Player import *
from Events import *
import random

difficulty = 0
event = None
movesTilEnd = 0
numOfChoices = 2

#These values represent the monsters available in an array can be chosen
enemyMin = 0
enemyMax = 2

def DarkCave(difficulty):
	print "You walk into the dark and spooky cave."
	movesTilEnd = 10
	enemyMin = 0
	enemyMax = 2
	
	dungeon(enemyMin, enemyMax, movesTilEnd, difficulty)
	
	newGuy.acquired("Broadsword")
	difficulty += 1
	return difficulty

def BrightField(difficulty):
	print "It's a nice and sunny day out in this field."
	print "Only there's a bunch of psycho monsters trying to attack you."
	print "Gotta keep moving, go go go!"
	movesTilEnd = 10
	enemyMin = 3
	enemyMax = 5
	
	dungeon(enemyMin, enemyMax, movesTilEnd, difficulty)
		
	newGuy.acquired("MagicShot")
	difficulty += 1
	return difficulty

def Marsh(difficulty):
	print "This marsh is awfully murky.  Kinda disgusting."
	print "Good luck.  You'll need it."
	
	movesTilEnd = 15
	enemyMin = 7
	enemyMax = 9
	
	dungeon(enemyMin, enemyMax, movesTilEnd, difficulty)
		
	newGuy.acquired("Heal Spell")
	difficulty += 1
	return difficulty

def Arena(difficulty):
	print "A battleground that was once host to some of the fiercest duels in history."
	print "Now a gravesite for those who fought, they come back to haunt intruders."
	movesTilEnd = 15
	enemyMin = 10
	enemyMax = 12
	
	dungeon(enemyMin, enemyMax, movesTilEnd, difficulty)
		
	newGuy.acquired("MagicBlast")
	difficulty += 1
	return difficulty

def CastleOfDreams(difficulty):
	print "You wander into the castle, everything around you distorted in some way shape or form."
	print "Clocks tick backwards, walls look like floors, and the entrance disappeared behind you."
	movesTilEnd = 20
	enemyMin = 14
	enemyMax = 16
	
	dungeon(enemyMin, enemyMax, movesTilEnd, difficulty)
	
	newGuy.acquired("Magic Sword")
	difficulty += 1
	return difficulty
	
def dungeon(enemyMin, enemyMax, movesTilEnd, difficulty):	
	
	event = None
	Entered = False
		
	while movesTilEnd > 0:
	
		if movesTilEnd > 1 and Entered:
			LocationAndEvent = pathOfInterest()
			event = LocationAndEvent[1]
	
		move = room()
		
		movesTilEnd -= 1
		if not Entered:
			UnknownRoomEvent(enemyMin, enemyMax, difficulty)
			Entered = True
		elif movesTilEnd > 0:
			if move != LocationAndEvent[0]:
				UnknownRoomEvent(enemyMin, enemyMax, difficulty)
				event = None #The player did not go to the location with the predetermined event
			else:
				RandomEvent(enemyMin, enemyMax, difficulty, event)
def room():
	print "You may:"
	print "1. Go left"
	print "2. Go right"
	
	action = None
	
	while not newGuy.isValidAction(action, 2):
		action = raw_input("> ")

	numOfChoices = 2
	
	newGuy.setHP(newGuy.HP + int(newGuy.MaxHP/5))
	newGuy.setMP(newGuy.MP + int(newGuy.MaxMP/5))
	
	return int(action)
	
def pathOfInterest():
	path = random.randint(0, 2) #If 0, nothing happens
	
	eventNumber = 0
	message = None
	
	if path > 0:
		
		whichPath = ""
		
		if path == 1:
			whichPath = "left"
		else:
			whichPath = "right"
		
		eventNumber = random.randint(0, 5)
		
		if eventNumber <= 1:
			message = "Growl"
			print "You hear a growl coming from the path on the %r." % whichPath
		
		elif eventNumber == 2:
			message = "Water"
			print "You hear drops of water coming from the path on the %r." % whichPath
			
		elif eventNumber == 3:
			message = "Nothing"
			print "The path on the %r seems awfully quiet..." % whichPath
			
		else:
			message = "Footsteps"
			print "You hear footsteps from the path on the %r." %whichPath
			
	return [path, message]

def RandomEvent(enemyMin, enemyMax, difficulty, message = None):
	if message != None:
		if message == "Growl":
			randomEncounter(enemyMin, enemyMax, difficulty)
			return
		elif message == "Water":
			Fountain()
			return
		elif message == "Nothing":
			whatHappens = random.randint(0, 9)
			if whatHappens < 6:
				print "A monster was hiding!  How sneaky!"
				randomEncounter(enemyMin, enemyMax, difficulty)
				return
			else:
				print "Nothing here..."
		else:
			Footsteps(enemyMin, enemyMax, difficulty)
				

def UnknownRoomEvent(enemyMin, enemyMax, difficulty):
	event = random.randint(0, 99)
	if event < 65:
		randomEncounter(enemyMin, enemyMax, difficulty)
	elif event < 75:
		Fountain()
	elif event < 85:
		Footsteps(enemyMin, enemyMax, difficulty)
	else:
		print "There's nothing here..."