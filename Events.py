from Player import *
from Enemy import *
import random

def randomEncounter(monsterMin, monsterMax, difficulty):
	Opponent = getOpponent(monsterMin, monsterMax, difficulty)
	print "Under attack by %r" % Opponent.name
	
	#This loop will end in the return statement if player runs, player dying, or while loop ending and player winning
	
	while not newGuy.KOed() and not Opponent.KOed():
		DamageToOpponent = newGuy.BattleMenu()
		
		if not DamageToOpponent: #If DamageToOpponent false, that means trying to escape, otherwise is number
			if newGuy.run(Opponent.speed):
				print "You successfully escaped!"
				return
			else:
				if Opponent.speed == 99:
					print "You can't escape from this battle."
				else:
					print "Unable to escape!"
		
		elif DamageToOpponent != 0.5: #0.5 is the value returned from a miss.  Not 0 because we don't want run activated
			DamageToOpponent = int(DamageToOpponent) 
			print "%r damage to %r!" % (DamageToOpponent, Opponent.name)
			Opponent.setHP(Opponent.HP - DamageToOpponent)
		
		if not Opponent.KOed():
			damage = Opponent.Decide()
			if not (type(damage) == int):
				Opponent = damage
			elif damage != 0: #Damage < 0 implies healing
				newGuy.setHP(newGuy.HP - damage)
			
		
		
	print "Enemy %r defeated!" % Opponent.name
	newGuy.wonBattle()
		
		
def Fountain():
	print "You find a mysterious fountain.  Drink from it?\n1. Yes\n2. No"
	
	action = None
	
	while not newGuy.isValidAction(action, 2):
		action = raw_input("> ")
		
	if action == "1":
		fountain = random.randint(1, 10)
		if fountain <=  3:
			print "You feel amazing!  Even better than before!"
			newGuy.acquired("HP Upgrade", 3)
			newGuy.HealMP
		elif fountain < 8:
			print "You feel pretty good.  HP restored."
			newGuy.HealHP()
			newGuy.HealMP()
		else:
			print "This water tastes weird..."
			CurrentHP = newGuy.HP
			newGuy.setHP(CurrentHP - 5)

def Footsteps(enemyMin, enemyMax, difficulty):
	whatHappens = random.randint(0, 99)
	
	if whatHappens < 60:
		randomEncounter(enemyMin, enemyMax, difficulty)
		return
	elif whatHappens < 70:
		print "A mysterious man dressed in an awfully bright shade of pink appears."
		print '"Wha-heyheyhey how\'s is goooooing?  I can give you some speeeeecial training.'
		print '"Do you want some mental training?  Or more... physical?"'
		print "1. Physical\n2. Mental"
		
		action = None
	
		while not newGuy.isValidAction(action, 2):
			action = raw_input("> ")
		
		print "Excellent chooooooiiiice.  Okay, here.  We.  Go."
		if action == "1":
			newGuy.acquired("HP Upgrade", 3)
			newGuy.acquired("Power Up")
		else:
			newGuy.acquired("MP Upgrade", 3)
			newGuy.acquired("Magic Up")
		
		print "That was fun.  Bye-bye!"
		return
	elif whatHappens < 85:
		print "A mysterious stranger in a dark hood hands you a potion."
		print "Will you drink the potion?\n1. Yes\n2. No"
		
		action = None
		
		while not newGuy.isValidAction(action, 2):
			action = raw_input("> ")
		
		if action == "1":
			heal = random.randint(0, 99)
			if heal < 75:
				print "Health up!"
				newGuy.setHP(newGuy.HP + newGuy.MaxHP/2)
				newGuy.setMP(newGuy.MP + newGuy.MaxMP/2)
			else:
				print "That tasted disgusting..."
				newGuy.setHP(newGuy.HP - 10)
				
	else:
		print "That's strange... nothing's here."