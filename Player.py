import random

class Player:
		
		def __init__(self):
			self.power = 1
			self.magic = 0
			self.MP = 0
			self.HP = 20
			self.MaxHP = 20
			self.MaxMP = 0
			self.BroadSword = False
			self.MagicSword = False
			self.LegendSword = False
			self.MagicShot = False
			self.MagicBlast = False
			self.MagicSlice = False
			self.BattleActions = 2
			#Power upgrades will multiply damage done
			self.damageMultiplier = 1
			self.magicMultiplier = 1
			self.level = 1
			self.battleswon = 0 #In place of EXP
			self.magicCost = 0
			self.healSpell = False
			
		def acquired(self, item, amount = 10):
			if item == "Broadsword" and not self.BroadSword and not self.MagicSword:
				self.power += 3
				self.BroadSword = True
				self.damageMultiplier = 2
				print "You found the Broadsword!  Power +3!"
				return
				
			if item == "Magic Sword" and self.BroadSword and not self.MagicSword:
				self.power += 3
				self.magic += 3
				self.MagicSword = True
				self.MagicSlice = True
				self.MaxMP += amount
				self.damageMultiplier = 3
				self.magicMultiplier = 8
				print "You found the Magic Sword!"
				print "Power +3, Magic +3, Max MP +%r" % amount
				print "Your Magic Blast has been upgraded to Magic Slice!  Uses 12 MP to cast."
				self.magicCost = 12
				return
				
			if item == "HP Upgrade":
				self.MaxHP += amount
				self.HP = self.MaxHP
				print "Max HP +%r!  Your health has been restored." % amount
				return
				
			if item == "MP Upgrade":
				self.MaxMP += amount
				self.MP = self.MaxMP
				print "Max MP + %r!  Your MP has been restored." % amount
				return
			
			if item == "MagicShot":
				self.MagicShot = True
				self.magic += 3
				self.BattleActions += 1
				self.magicMultiplier = 3
				self.magicCost = 4
				print "You have learned Magic Shot!"
				print "In battle, you can use Magic Shot instead of attacking.  Does more damage but uses 4 MP"
				self.acquired("MP Upgrade")
				return
				
			if item == "MagicBlast":
				self.MagicBlast = True
				self.magic += 3
				self.magicMultiplier = 5
				print "Your Magic Shot has been upgraded to Magic Blast!  8 MP to use."
				self.acquired("MP Upgrade")
				self.magicCost = 8
				return
				
			if item == "Power Up":
				self.power += 1
				print "Power +1!"
				return
				
			if item == "Magic Up":
				self.magic += 1
				print "Magic +1!"
				return
				
			if item == "Heal Spell":
				print "You learned Heal!"
				print "It costs 1/5 of your max MP to use, and recovers 50% of your max HP!"
				self.healSpell = True
				return
		
		def HealHP(self):
			self.HP = self.MaxHP
		
		def HealMP(self):
			self.MP = self.MaxMP
		
		def setHP(self, newHP):
			
			if self.HP == self.MaxHP and newHP >= self.MaxHP:
				return
			
			self.HP = newHP
			if self.HP < 0:
				self.HP = 0
			
			if self.HP > self.MaxHP:
				self.HP = self.MaxHP		
								
			print "Current HP: %r/%r" % (self.HP, self.MaxHP)
			
			if self.HP <= 0:
				self.dead("Sorry, seems you got yourself killed.")
				#Exit condition
						
		def setMP(self, newMP):
			
			if self.MP == self.MaxMP and newMP >= self.MaxMP:
				return
		
			self.MP = newMP
			if self.MP < 0:
				self.MP = 0
			
			if self.MP > self.MaxMP:
				self.MP = self.MaxMP
				
			print "Current MP: %r/%r" % (self.MP, self.MaxMP)
		
		def HealSpell(self):
			if self.MP > self.MaxMP/5:
				self.setMP(self.MP - self.MaxMP/5)
				self.setHP(self.HP + self.MaxHP/2)
			else:
				print "Not enough MP!"
		
		def KOed(self):
			if self.HP <= 0:
				dead("You've been killed!")
			else:
				return False
		
		def dead(self, causeofdeath = "You have been smitten by Zeus.  9999 damage, unblockable and undodgeable."):
			print causeofdeath
			exit()

		def isValidAction(self, actionChoice, maxActions): #In hindsight, probably does not need to be in this class...
			
			if actionChoice is None:
				return False
				
			try:
				actionChoice = int(actionChoice)
			except:
				if actionChoice == "q" or actionChoice == "Q":
					exit()
				else:				
					print "Please use numbers."
					return False
				
			#actionChoice will always be an int by this point
			if actionChoice <= maxActions and actionChoice > 0:
				return True
			elif actionChoice < 1:
				print "Positive numbers only, please."
				return False
			else:
				print "Um.  There's only %r actions available." % maxActions
				return False

		def BattleMenu(self):
			count = 1 #The options
			damage = 0
			
			print "%r. Attack" % count
			count += 1
			if self.MagicShot:
				print "%r. Magic" % count
				count += 1
				
			if self.healSpell:
				print "%r. Heal" % count
				count += 1
		
			print "%r. Run Away" % count
			
			action = None
			
			while not self.isValidAction(action, self.BattleActions):
				action = raw_input ("> ")
			
			if action == "1":
				damage = self.attack()
				return damage
			if action == "2" and self.MagicShot:
				damage = self.Magic()
				return damage
			elif action == "3" and self.healSpell:
				self.HealSpell()
				return 0.5
			else:
				return False #This gives the command to try and escape
				
		def attack(self):
			attackHit = random.randint(0, 99)
			
			if attackHit < 90:
				damageRadius = int((self.damageMultiplier*self.power)/5) 
				damage = random.randint(self.power-(damageRadius/2), self.power+damageRadius)
				if damage <= 0:
					damage = 1
				return damage
				
			else:
				print "Attack missed..."
				return 0.5
		
		def Magic(self):
			if self.MP >= self.magicCost:
				damageRadius = int((self.magicMultiplier*self.magic)/5)
				damage = random.randint(self.magic, self.magic+damageRadius)
				self.MP -= self.magicCost
				print "MP: %r/%r" % (self.MP, self.MaxMP)
				return damage
			else:
				print "Not enough MP. %r/%r" % (self.MP, self.MaxMP)
				return 0.5
				
			
		def run(self, enemySpeed):
			#Enemy speed is a value between 0 and 99.  If 99, you cannot escape
			ableToRun = random.randint(0, 99)
			if ableToRun > enemySpeed:
				return True
			else:
				return False
			
		def wonBattle(self):
			self.battleswon += 1
			self.whenToLevel()
		
		def whenToLevel(self):
			requirement = self.level + 1
			if self.battleswon == requirement:
				self.levelUp()
				
		def levelUp(self):
			self.level += 1
			print "Level Up!  You are now level %r!" % self.level
			self.battleswon = 0
			self.acquired("Power Up")
			self.acquired("Magic Up")
			
			if self.level % 5 == 0:
				self.acquired("HP Upgrade")
				self.acquired("MP Upgrade")
			
			if self.level % 4 == 0:
				print "Bonus!"
				self.acquired("Power Up")
				self.acquired("Magic Up")
			
			self.setHP(self.MaxHP)
			self.setMP(self.MaxMP)
			

#The player character is created here
newGuy = Player()