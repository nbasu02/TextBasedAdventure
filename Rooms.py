from Player import *
from Dungeon import *

def first_room():
	darkcave = False
	brightfield = False
	bossbeaten = False
	
	print "You wake up in the middle of a field, hungover.  It's going to be one of those days."
	print 'Suddenly, a mysterious old man hands you a sword and shield, saying "Take this to defend thyself."'
	print 'He then disappears.  Definitely one of those days.  However, this sword is definitely real.'
	
	difficulty = 0
	
	chancesToAct = 3
	actionTaken = None
	
	while not newGuy.isValidAction(actionTaken, 3):
		if chancesToAct == 0:
			print "Okay, eff this."
			newGuy.dead()
		
		if chancesToAct == 3:
			print 'There are now three paths.  One is a dark cave, one is a bright field, the other is to a forest, and is guarded by a giant wolf.'  
			print 'What action will you take?'

			print '\t1. Dark Cave'
			print '\t2. Bright Field'
			print '\t3. Attack the wolf to enter forest.'


		actionTaken = raw_input("> ")
		chancesToAct -= 1

	while not darkcave or not brightfield or not bossbeaten:
	

		if (darkcave or brightfield) and not bossbeaten:
			print 'But now comes the question, which path shall you take?'  
			print "Choosing a path you already went to is boring, so we're not letting you do it, but still making it an option."
			print "Are we devious or lazy?  You decide."

			print '\t1. Dark Cave'
			print '\t2. Bright Field'
			print '\t3. Attack the wolf to enter forest.'
			
			actionTaken = None
			
			while not newGuy.isValidAction(actionTaken, 3):
				actionTaken = raw_input("> ")
		
		if actionTaken == "1" and not darkcave:
			difficulty = DarkCave(difficulty)
			print "You find a nearby river and take a drink.  HP and MP restored!"
			newGuy.HealHP()
			newGuy.HealMP()
			print "You take a practice slash on a nearby tree with your newfound sword.  The tree uproots itself and tries to attack."
			print "Luckily it couldn't get very far and stumbled over.  You do not get experience points for this, tough luck."
			print 'But what a strange world you popped up in.  In fact, who are "you"?'
			darkcave = True
		
		if actionTaken == "2" and not brightfield:
			difficulty = BrightField(difficulty)
			print "You find a nearby river and take a drink.  HP and MP restored!"
			newGuy.HealHP()
			newGuy.HealMP()
			brightfield = True
			
		if actionTaken == "3":
			if darkcave and brightfield:
				print "The wolf suddenly released a powerful aura!"
				randomEncounter(6, 6, difficulty)
				newGuy.wonBattle()
				newGuy.wonBattle()
				newGuy.wonBattle()
				newGuy.HealHP()
				newGuy.HealMP()
				bossbattle = True
				second_room()
			else:
				print "You are not be ready to fight this one yet..."
				actionTaken = None
				
				while not newGuy.isValidAction(actionTaken, 3):
					print '\t1. Dark Cave'
					print '\t2. Bright Field'
					print '\t3. Attack the wolf to enter forest.'
					actionTaken = raw_input("> ")

def second_room(difficulty = 1):

	marsh = False
	arena = False
	bossbeaten = False
	
	print "With the guardian of the forest defeated, you move onward to explore more of this strange world."
	print "Who was the old man?  Why do you have magical powers?  What is up with these ridiculous battles you keep getting thrown into?"
	print "You look around and find a couple of options.  One is to explore a nearby marsh."
	print "Another is an old abandoned arena.  There is also a third, blocked off path."
	print "Where will you go?"
	
	actionTaken = None
	
	while not newGuy.isValidAction(actionTaken, 3):
	
		print '\t1. Marsh'
		print '\t2. Arena'
		print '\t3. Try to brave the third path.'
		
		actionTaken = raw_input("> ")
		
	while not marsh or not arena or not bossbeaten:
	

		if (marsh or arena) and not bossbeaten:
			print 'You know the drill, pick a path.'
			
			print '\t1. Marsh'
			print '\t2. Arena'
			print '\t3. Try to brave the third path.'			
			actionTaken = None
			
			while not newGuy.isValidAction(actionTaken, 3):
				actionTaken = raw_input("> ")
		elif not marsh and not arena:
			while not newGuy.isValidAction(actionTaken, 3):
			
				print '\t1. Marsh'
				print '\t2. Arena'
				print '\t3. Try to brave the third path.'
				
				actionTaken = raw_input("> ")
			
			
		if actionTaken == "1" and not marsh:
			difficulty = Marsh(difficulty)
			print "You find a nearby river and take a drink.  HP and MP restored!"
			newGuy.HealHP()
			newGuy.HealMP()
			print "You take a practice slash on a nearby tree with your newfound sword.  The tree uproots itself and tries to attack."
			print "Luckily it couldn't get very far and stumbled over.  You do not get experience points for this, tough luck."
			print 'But what a strange world you popped up in.  In fact, who are "you"?'
			marsh = True
		
		if actionTaken == "2" and not arena:
			difficulty = Arena(difficulty)
			print "You find a nearby river and take a drink.  HP and MP restored!"
			newGuy.HealHP()
			newGuy.HealMP()
			arena = True
			
		if actionTaken == "3":
			if marsh and arena:
				print "A dark figure grabs you from behind!"
				print '"Who are you?", you hear him yell.'
				print "You quickly break away from the figure's grip."
				randomEncounter(13, 13, difficulty)
				newGuy.wonBattle()
				newGuy.wonBattle()
				newGuy.wonBattle()
				newGuy.wonBattle()
				newGuy.wonBattle()
				newGuy.wonBattle()
				print "You find a nearby river and take a drink.  HP and MP restored!"
				newGuy.HealHP()
				newGuy.HealMP()
				bossbattle = True
				print "Defeating the dark figure caused the path to be revealed!  You can now go through."
				print "I'm really not trying to make a coherant story here.  Bare with me."
				last_room(difficulty)
			else:
				print "There's nothing here, and you can't seem to get through..."
				actionTaken = None

def last_room(difficulty):
	print "The path leads to an enormous palace, filled with lightning, ominous clouds, and other spooky things."
	print "Let's call it the Castle of Dreams.  Sounds like a good name, doesn't it?"
	print "So yeah, last level champ.  Go for it."
	
	difficulty = CastleOfDreams(difficulty)
	
	print "You actually made it through that?"
	print "I mean woo!  You made it to the throne room."
	print "There's no one here..."
	print "But hey, we can't let this be the end can we?"
	print "Remember that shadowy figure you fought before?"
	print "Well, look behind you."
	
	newGuy.HealHP()
	newGuy.HealMP()
	
	playerLevel = newGuy.level
	
	randomEncounter(17, 17, difficulty)
	while playerLevel == newGuy.level:
		newGuy.wonBattle()
	
	print '"Who are you?", you ask.'
	print '"My servant.", a voice says.  A man appears from behind a secret door in the back of the room.'
	print '"I am the King of Dreams. And you, young warrior, have caused me enough trouble.  It\'s time to wake up.'
	
	randomEncounter(18, 18, difficulty)
	
	print '"Oh good god you\'re tough.  But it\'s time to wake up.  Get your lazy ass up."'
	print '"Get your lazy ass up," you hear a woman say.  The voice belongs to your girlfriend.  You -were- hungover after all!"'
	print "You may have defeated the strongest fighters in the world of dreams, but this is one battle you can't win."
	
	exit()