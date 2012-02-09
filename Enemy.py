import random

class Enemy(object):

	def __init__(self, difficulty, power, MaxHP, magic, MaxMP, speed, name, spellCost, specialCost):
		self.power = power + 2*difficulty
		self.HP = self.MaxHP = MaxHP + 5*difficulty
		self.magic = magic + 2* difficulty
		self.MP = self.MaxMP = MaxMP + 5*difficulty
		self.speed = speed
		self.name = name
		self.spellCost = spellCost + difficulty
		self.specialCost = specialCost + difficulty
	
	def setHP(self, newHP):
		self.HP = newHP
		if self.HP < 0:
			self.HP = 0
		if self.HP > self.MaxHP:
			self.HP = self.MaxHP
		print "%r: %r/%r HP" % (self.name, self.HP, self.MaxHP) 
		#This method is used instead of just Opponent.HP for enemies who can increase defense
	
	def KOed(self):
		return self.HP == 0
	
	def Attack(self):
		attackHit = random.randint(0, 99)
		damage = 0
		if attackHit < 90:
			damageVariation = int(self.power/5)
			damage = random.randint(self.power - damageVariation, self.power + damageVariation)
			if damage == 0:
				damage = 1
		
			print "Attacked for %r damage!" % damage
		
		else:
			print "Attack missed!"
			damage = 0
		
		return damage
	
	def Spell(self, name):
		pass
	
	def Special(self, name):
		pass

	def Decide(self):
		damage = 0
		if self.MP >= self.specialCost and self.MP >= self.spellCost:
			attackChoice = random.randint(0, 99)
			if attackChoice < 60:
				damage = self.Attack()
			elif attackChoice < 80:
				damage = self.Spell()
			else:
				damage = self.Special()
			
			return damage
		elif self.MP >= self.spellCost:
			attackChoice = random.randint(0, 99)
			if attackChoice < 60:
				damage = self.Attack()
			else:
				damage = self.Spell()
			
			return damage
		elif self.MP >= self.specialCost: #Some enemies will have higher costs for magic or specials, depending on enemy
			attackChoice = random.randint(0, 99)
			if attackChoice < 60:
				damage = self.Attack()
			else:
				damage = self.Special()
			
			return damage
		else:
			damage = self.Attack() #No MP left
			return damage
		
class BabyRobot(Enemy):
	def __init__(self, difficulty = 0, power = 1, MaxHP = 5, magic = 1, MaxMP = 5, speed = 3, name = "Evil Scientist", spellCost = 1, specialCost = 2):
		args = (1, 5, 1, 5, 5, "Baby Robot", 2, 3)
		super(BabyRobot, self).__init__(difficulty, *args)
			
	def Spell(self, name = "Laser Eye Beam!"):
		self.MP -= self.spellCost
		damage = int(self.magic*2)
		
		print name
		print "%r damage!" % damage
				
		return damage

	def Special(self, name = "Double Punch!"):
		self.MP -= self.specialCost
		print name
		damage = self.Attack()
		damage += self.Attack()
		
		return damage
	
class EvilScientist(Enemy):
	def __init__(self, difficulty = 0, power = 1, MaxHP = 5, magic = 1, MaxMP = 5, speed = 3, name = "Evil Scientist", spellCost = 1, specialCost = 2):
		args = (1, 5, 1, 5, 3, "Evil Scientist", 1, 2)
		super(EvilScientist, self).__init__(difficulty, *args)
		if difficulty > 0:
			self.power -= 1
		
	def Spell(self, name = "Heal"):
		print name
		if self.MaxHP - self.HP < self.magic:
			healAmount = self.MaxHP - self.HP
			print "%r healed %r HP." % (name, healAmount)
			self.HP = self.MaxHP
			print "%r/%r HP" % (self.HP, self.MaxHP)
		else:
			print "%r healed %r HP." % (name, self.magic)
			self.HP += self.magic
			print "%r/%r HP" % (self.HP, self.MaxHP)
		
		self.MP -= self.spellCost
		return 0
	
	def Special(self, name = "Scalpel"):
		print name
		self.MP -= self.specialCost
		damage = self.power + self.magic
		print "%r damage!" % damage
		return damage
	
	def Decide(self):
		damage = 0
		if self.MP >= self.specialCost and (self.MP >= self.spellCost and self.HP < self.MaxHP): #The spell for imp heals
			attackChoice = random.randint(0, 99)
			if attackChoice < 60:
				damage = self.Attack()
			elif attackChoice < 80:
				damage = self.Spell()
			else:
				damage = self.Special()
			
			return damage
		elif self.MP >= self.spellCost and self.HP < self.MaxHP:
			attackChoice = random.randint(0, 99)
			if attackChoice < 60:
				damage = self.Attack()
			else:
				damage = self.Spell()
			
			return damage
		elif self.MP >= self.specialCost: #Some enemies will have higher costs for magic or specials, depending on enemy
			attackChoice = random.randint(0, 99)
			if attackChoice < 60:
				damage = self.Attack()
			else:
				damage = self.Special()
			
			return damage
		else:
			damage = self.Attack() #No MP left
			return damage

class LooseCannon(Enemy):
	def __init__(self, difficulty = 0, power = 1, MaxHP = 5, magic = 1, MaxMP = 5, speed = 5, name = "Loose Cannon", spellCost = 1, specialCost = 0):
		super(LooseCannon, self).__init__(difficulty, power, MaxHP, magic, MaxMP, speed, name, spellCost, specialCost)
		if difficulty > 0:
			self.spellCost += 1
			self.power -= 1
			#This guy needs nerfing

	def Spell(self, name = "Fire!"):
		print name
		self.MP -= self.spellCost
		damage = int(1.5*self.power)
		print "%r damage!" % damage
		
		if self.MP < self.spellCost:
			print "%r ran out of ammo.  It is no longer dangerous." % self.name
			self.HP = 0
		
		return damage
	
	def Special(self, name = "All Out Barrage"):
		print name
		damage = 0
		while self.HP > 0: #Second should imply the first, but just in case...
			damage += self.Spell()
		
		return damage
	
	def Decide(self):
		attackChoice = random.randint(0, 99)
		#This enemy doesn't use normal attacks.  It is destroyed once its MP hits 0, so doesn't need to worry about MP being 0
		damage = 0
		if attackChoice < 75:
			damage = self.Spell()
		else:
			damage = self.Special()
		
		return damage

class EvilPlant(Enemy):
	def __init__(self, difficulty = 0, power = 1, MaxHP = 4, magic = 1, MaxMP = 5, speed = 5, name = "Evil Plant", spellCost = 2, specialCost = 2):
		super(EvilPlant, self).__init__(difficulty, power, MaxHP, magic, MaxMP, speed, name, spellCost, specialCost)
		self.PoisonCount = 0
		self.EntangleCount = 0
		if difficulty > 0:
			self.magic += 1
	
	def Spell(self, name = "Toxic Powder!"):
		print name
		self.PoisonCount = 3
		print "You were poisoned!"
		return 0
	
	def Special(self, name = "Entangle!"):
		print name
		self.EntangleCount = 3
		print "You've been binded by the enemy's vines!  You cannot escape until you are freed!"
		self.speed = 99
		return 0
	
	def Decide(self):
		damage = 0
		if (self.MP >= self.specialCost and self.EntangleCount <= 0) and (self.MP >= self.spellCost and self.PoisonCount <= 0):
			attackChoice = random.randint(0, 100)
			if attackChoice < 60:
				damage = self.Attack()
			elif attackChoice < 80:
				damage = self.Spell()
			else:
				damage = self.Special()
			
		elif self.MP >= self.spellCost and not self.PoisonCount <= 0:
			attackChoice = random.randint(0, 99)
			if attackChoice < 60:
				damage = self.Attack()
			else:
				damage = self.Spell()
			
		elif self.MP >= self.specialCost and not self.EntangleCount <= 0:
			attackChoice = random.randint(0, 99)
			if attackChoice < 60:
				damage = self.Attack()
			else:
				damage = self.Special()
			
		else:
			damage = self.Attack() #No MP left
		
		if self.PoisonCount > 0:
			damage += self.magic
			self.PoisonCount -= 1
			print "1 damage from poison!"
			
			if self.PoisonCount == 0:
				print "The poison has left your system."
		
		if self.EntangleCount > 0:
			damage += self.power
			self.EntangleCount -= 1
			print "1 damage from Entangle!"
			if self.EntangleCount == 0:
				self.speed = 5
				print "Freed from Entangle."
			
		return damage

class Marauder(Enemy):
	def __init__(self, difficulty = 0, power = 1, MaxHP = 6, magic = 1, MaxMP = 5, speed = 15, name = "Marauder", spellCost = 2, specialCost = 3):
		super(Marauder, self).__init__(difficulty, power, MaxHP, magic, MaxMP, speed, name, spellCost, specialCost)
		if difficulty > 0:
			self.power += 1
	
	def Spell(self, name = "Warp Punch!"):
		print name
		self.MP -= self.spellCost
		damage = self.power + self.magic - 1
		return damage
	
	def Special(self, name = "Slash Combo!"):
		print name
		self.MP -= self.specialCost
		damage = self.power * 2
		return damage

class HoodedMan(Enemy):
	def __init__(self, difficulty = 0, power = 1, MaxHP = 5, magic = 1, MaxMP = 6, speed = 5, name = "Hooded Man", spellCost = 2, specialCost = 0):
		super(HoodedMan, self).__init__(difficulty, power, MaxHP, magic, MaxMP, speed, name, spellCost, specialCost)
		if difficulty > 0:
			self.MaxMP += 3
			self.MP = self.MaxMP
	
	def Spell(self, name = "Fireball!"):
		print name
		self.MP -= self.spellCost
		damage = 2*self.magic
		print "%r damage!" % damage
		return damage
	
	def Special(self, name = "Recharge!"):
		print name
		self.MP = self.MaxMP
		print "%r's MP restored to max!" % self.name
		return 0
	
	def Decide(self):
		damage = 0
		if self.MP >= self.spellCost:
			damage = self.Spell()
		else:
			damage = self.Special()
		
		return damage
		
class ForestGuardian(Enemy):
	def __init__(self, difficulty = 0, power = 4, MaxHP = 20, magic = 4, MaxMP = 15, speed = 99, name = "Forest Guardian", spellCost = 3, specialCost = 5):
		super(ForestGuardian, self).__init__(difficulty, power, MaxHP, magic, MaxMP, speed, name, spellCost, specialCost)
		
	def Spell(self, name = "Absorb!"):
		print name
		self.MP -= self.spellCost
		damage = self.magic
		print "%r absorbed %r HP!" % (self.name, damage/2)
		self.setHP(self.HP + damage/2)
		return damage
	
	def Special(self, name = "Wild Rush"):
		print name
		AttackHit = random.randint(0, 99)
		self.MP -= self.specialCost
		print "%r powered itself up!" % self.name
		damage = self.power + 4
		print "%r hurt itself with its attack!" % self.name 
		if AttackHit < 25:
			self.setHP(self.HP - damage/2)
			print "But the attack missed..."
			return 0
		else:
			self.setHP(self.HP - 2*(damage/3))
			return damage
			
	def Decide(self):
		damage = 0
		#Adding in the requirement that this enemy doesn't kill itself from its special
		if (self.MP >= self.specialCost and self.HP > 2*(self.power + 4)/3) and self.MP >= self.spellCost:
			attackChoice = random.randint(0, 99)
			if attackChoice < 60:
				damage = self.Attack()
			elif attackChoice < 80:
				damage = self.Spell()
			else:
				damage = self.Special()
			
			return damage
		elif self.MP >= self.spellCost:
			attackChoice = random.randint(0, 99)
			if attackChoice < 60:
				damage = self.Attack()
			else:
				damage = self.Spell()
			
			return damage
		elif self.MP >= self.specialCost and 2*(self.HP > self.power + 4)/3:
			attackChoice = random.randint(0, 99)
			if attackChoice < 60:
				damage = self.Attack()
			else:
				damage = self.Special()
			
			return damage
		else:
			damage = self.Attack()
			return damage

class MarshMonster(Enemy):
	def __init__(self, difficulty = 0, power = 1, MaxHP = 20, magic = 1, MaxMP = 6, speed = 15, name = "Marsh Monster", spellCost = 0, specialCost = 4):
		super(MarshMonster, self).__init__(difficulty, power, MaxHP, magic, MaxMP, speed, name, spellCost, specialCost)
		self.defenseUp = False
		self.defenseIncrease = 4 + difficulty
		
	def setHP(self, newHP):
		if self.defenseUp:
			self.HP = newHP + self.defenseIncrease
			print "Barrier lowered damage by %r" % self.defenseIncrease
		else:
			self.HP = newHP
		
		if self.HP < 0:
			self.HP = 0
		if self.HP > self.MaxHP:
			self.HP = self.MaxHP
		print "%r: %r/%r HP" % (self.name, self.HP, self.MaxHP) 

	def Spell(self, name = "Barrier!"):
		print name
		print "Defense increased by %r!" % self.defenseIncrease
		self.defenseUp = True
		self.MP -= self.spellCost
		return 0
	
	def Special(self, name = "Marsh Stomp"):
		print name
		self.MP -= self.specialCost
		damage = self.power + 3
		print "%r damage!" % damage
		return damage
	
	def Decide(self):
		damage = 0
		if self.MP >= self.specialCost and not self.defenseUp and self.MP >= self.spellCost:
			attackChoice = random.randint(0, 99)
			if attackChoice < 60:
				damage = self.Attack()
			elif attackChoice < 80:
				damage = self.Spell()
			else:
				damage = self.Special()
			
			return damage
		elif self.MP >= self.spellCost and not self.defenseUp:
			attackChoice = random.randint(0, 99)
			if attackChoice < 60:
				damage = self.Attack()
			else:
				damage = self.Spell()
			
			return damage
		elif self.MP >= self.specialCost:
			attackChoice = random.randint(0, 99)
			if attackChoice < 60:
				damage = self.Attack()
			else:
				damage = self.Special()
			
			return damage
		else:
			damage = self.Attack()
			return damage
		
class Dragonfly(Enemy):
	def __init__(self, difficulty = 0, power = 2, MaxHP = 15, magic = 3, MaxMP = 10, speed = 20, name = "Dragonfly", spellCost = 3, specialCost = 4):
		super(Dragonfly, self).__init__(difficulty, power, MaxHP, magic, MaxMP, speed, name, spellCost, specialCost)
	
	def Spell(self, name = "Wing Vibration!"):
		print name
		self.MP -= self.spellCost
		damage = int(self.magic*1.5)
		print "%r damage!" % damage
		return damage
	
	def Special(self, name = "Bite Off"):
		print name
		self.MP -= self.specialCost
		damage = self.power + 4
		print "%r damage!" % damage
		return damage

class MuddyGuy(Enemy):
	def __init__(self, difficulty = 0, power = 2, MaxHP = 15, magic = 3, MaxMP = 10, speed = 20, name = "Muddy Guy", spellCost = 2, specialCost = 2):
		super(MuddyGuy, self).__init__(difficulty, power, MaxHP, magic, MaxMP, speed, name, spellCost, specialCost)
		self.suffocation = 0
	
	def setHP(self, newHP):
		if self.suffocation == 0:
			self.HP = newHP
		else:
			self.HP = self.HP - int(2*(self.HP - newHP)/3)

		if self.HP < 0:
			self.HP = 0
		if self.HP > self.MaxHP:
			self.HP = self.MaxHP
		print "%r: %r/%r HP" % (self.name, self.HP, self.MaxHP) 
					
	
	def Spell(self):
		self.suffocation = random.randint(3, 5)
		self.MP -= self.spellCost
		print "Being dragged into mud!  Unable to attack effectively while being pulled under!"
		return 0
	
	def Special(self, name = "Suffocate"):
		print name
		self.MP -= self.specialCost
		damage = self.Attack()
		self.Spell()
		return damage

	def Decide(self):
		damage = 0
		if self.suffocation == 0:
			if self.MP >= self.specialCost and self.MP >= self.spellCost:
				attackChoice = random.randint(0, 99)
				if attackChoice < 60:
					damage = self.Attack()
				elif attackChoice < 80:
					damage = self.Spell()
				else:
					damage = self.Special()
				
				return damage
			elif self.MP >= self.spellCost:
				attackChoice = random.randint(0, 99)
				if attackChoice < 60:
					damage = self.Attack()
				else:
					damage = self.Spell()
				
				return damage
			elif self.MP >= self.specialCost: #Some enemies will have higher costs for magic or specials, depending on enemy
				attackChoice = random.randint(0, 99)
				if attackChoice < 60:
					damage = self.Attack()
				else:
					damage = self.Special()
				
				return damage
			else:
				damage = self.Attack() #No MP left
				return damage
		else:
			damage = self.magic + 1
			self.suffocation -= 1
			if self.suffocation > 0:
				print "Enemy continues to drag you under!"
			else:
				print "You broke free from the enemy!"
			
			return damage
		
class ZombieGladiator(Enemy):
	def __init__(self, difficulty = 0, power = 3, MaxHP = 15, magic = 1, MaxMP = 10, speed = 20, name = "Zombie Gladiator", spellCost = 3, specialCost = 4):
		super(ZombieGladiator, self).__init__(difficulty, power, MaxHP, magic, MaxMP, speed, name, spellCost, specialCost)
		self.maxPower = self.power #Special causes a one-time loss of attack power
		
	def Spell(self, name = "Leech!"):
		print name
		self.MP -= self.spellCost
		damage = int(self.magic*2.5)
		self.setHP(self.HP + int(damage/2))
		print "%r damage" % damage
		return damage
	
	def Special(self, name = "Chaaaaaaarge!"):
		print name
		damage = self.power*2
		self.MP -= self.specialCost
		print "%r damage" % damage
		if self.power == self.maxPower:
			print "%r's left arm fell off!" % self.name
			self.power -= 3
			print "-3! Attack"
		return damage

	def Decide(self):
		#Only addition is decay damage
		damage = 0
		if self.MP >= self.specialCost and self.MP >= self.spellCost:
			attackChoice = random.randint(0, 99)
			if attackChoice < 60:
				damage = self.Attack()
			elif attackChoice < 80:
				damage = self.Spell()
			else:
				damage = self.Special()
			
			decay = int(self.MaxHP/10)
			print "%r took %r damage from decay." % (self.name, decay)
			self.setHP(self.HP - decay)
			
			return damage
		elif self.MP >= self.spellCost:
			attackChoice = random.randint(0, 99)
			if attackChoice < 60:
				damage = self.Attack()
			else:
				damage = self.Spell()
			
			return damage
		elif self.MP >= self.specialCost: #Some enemies will have higher costs for magic or specials, depending on enemy
			attackChoice = random.randint(0, 99)
			if attackChoice < 60:
				damage = self.Attack()
			else:
				damage = self.Special()
			
			return damage
		else:
			damage = self.Attack() #No MP left
			return damage

class ZombieLion(Enemy):
	def __init__(self, difficulty = 0, power = 3, MaxHP = 15, magic = 2, MaxMP = 10, speed = 30, name = "Zombie Lion", spellCost = 1, specialCost = 3):
		super(ZombieLion, self).__init__(difficulty, power, MaxHP, magic, MaxMP, speed, name, spellCost, specialCost)
		self.maxPower = self.power #One-time loss of power
	
	def Spell(self, name = "Lion's Roar"):
		print name
		self.MP -= self.spellCost
		damage = int(self.magic*1.5)
		print "%r damage" % damage
		return damage
	
	def Special(self, name = "Feast"):
		print name
		damage = self.power+2
		self.MP -= self.specialCost
		self.setHP(self.HP + int(damage/2))
		print "Healed %r HP" % int(damage/2)
		if self.power > 2:
			print "Its stomach couldn't handle the digestion."
			print "-2 attack"
			self.power -= 2
		return damage	
			
	def Decide(self):
		#Only addition is decay damage
		damage = 0
		if self.MP >= self.specialCost and self.MP >= self.spellCost:
			attackChoice = random.randint(0, 99)
			if attackChoice < 60:
				damage = self.Attack()
			elif attackChoice < 80:
				damage = self.Spell()
			else:
				damage = self.Special()
			
			decay = int(self.MaxHP/10)
			print "%r took %r damage from decay." % (self.name, decay)
			self.setHP(self.HP - decay)
			
			return damage
		elif self.MP >= self.spellCost:
			attackChoice = random.randint(0, 99)
			if attackChoice < 60:
				damage = self.Attack()
			else:
				damage = self.Spell()
			
			return damage
		elif self.MP >= self.specialCost: #Some enemies will have higher costs for magic or specials, depending on enemy
			attackChoice = random.randint(0, 99)
			if attackChoice < 60:
				damage = self.Attack()
			else:
				damage = self.Special()
			
			return damage
		else:
			damage = self.Attack() #No MP left
			return damage

class Ghost(Enemy):
	def __init__(self, difficulty = 0, power = 0, MaxHP = 15, magic = 3, MaxMP = 10, speed = 30, name = "Ghost", spellCost = 0, specialCost = 0):
		super(Ghost, self).__init__(difficulty, power, MaxHP, magic, MaxMP, speed, name, spellCost, specialCost)
		self.spellCost = 0
		self.difficulty = difficulty #To summon other monsters
		
	def setHP(self, newHP):
		attackHit = random.randint(0, 99)
		if attackHit < 75:
			self.HP = newHP
			if self.HP < 0:
				self.HP = 0
			if self.HP > self.MaxHP:
				self.HP = self.MaxHP
			print "%r: %r/%r HP" % (self.name, self.HP, self.MaxHP) 
		else:
			print "The attack went right through the Ghost!"
		
	def Spell(self, name = "Haunt"):
		print name
		damageVariation = int(self.magic/5)
		damage = random.randint(self.magic, self.magic + damageVariation)
		print "%r damage!" % damage
		return damage
	
	def Special(self, name = "Summon and Possess"):
		print name
		NewEnemy = getOpponent(7, 11, self.difficulty)
		print "Possessed %r!" % NewEnemy.name
		
		return NewEnemy
		
	def Decide(self):
		choice = random.randint(0, 99)
		damage = 0
		
		if self.HP > self.MaxHP/3:
			if choice < 75:
				damage = self.Spell()
			else:
				damage = self.Special() #Though technically not "damage"
		else:
			if choice < 50:
				damage = self.Spell()
			else:
				damage = self.Special()
		
		return damage
		
class BattleCaster(Enemy):
	def __init__(self, difficulty = 0, power = 3, MaxHP = 30, magic = 5, MaxMP = 30, speed = 99, name = "Battle Caster", spellCost = 0, specialCost = 3):
		super(BattleCaster, self).__init__(difficulty, power, MaxHP, magic, MaxMP, speed, name, spellCost, specialCost)
		self.Fire = 0
	
	def setHP(self, newHP):
		if self.Fire > 0:
			self.HP -= (self.HP - newHP)/2
			print "Ring of Fire lowered damage by half!"
		else:
			self.HP = newHP
		
		if self.HP < 0:
			self.HP = 0
		if self.HP > self.MaxHP:
			self.HP = self.MaxHP
		print "%r: %r/%r HP" % (self.name, self.HP, self.MaxHP) 
	
	def Spell1(self, name = "Blast!"):
		print name
		self.MP -= self.spellCost
		damageVariation = int(self.magic/5)
		damage = random.randint(self.magic, self.magic + damageVariation)
		print "%r damage!" % damage
		return damage
	
	def Spell2(self, name = "Telekenisis!"):
		print name
		self.MP -= self.spellCost
		damage = self.power + self.magic - 2 #-2 just for some balance
		print "%r damage!" % damage
		return damage
		
	def Special(self, name = "Ring of Fire!"):
		print name
		self.Fire = 3
		self.MP -= self.specialCost
		print "A huge ring of fire has appeared around %r!  It will slowly damage you and prevent you from doing full damage!" % self.name
		return 0
	
	def Decide(self):
		damage = 0
		choice = random.randint(0, 99)
		
		if self.MP >= self.spellCost:
			if self.HP >= self.MaxHP/3 or self.Fire > 0:
				if choice < 50:
					damage = self.Spell1()
				else:
					damage = self.Spell2()
			else:
				self.Special()
		
		else:
			damage = self.Attack()
		
		if self.Fire > 0:
			damage += 5
			print "5 damage from the fire!"
			self.Fire -= 1
			if self.Fire == 0:
				print "The fire has gone out."
		
		return damage
		
class Anubis(Enemy):
	def __init__(self, difficulty = 0, power = 4, MaxHP = 20, magic = 5, MaxMP = 20, speed = 25, name = "Anubis", spellCost = 0, specialCost = 6):
		args = (3, 30, 5, 10, 99, "Anubis", 0, 3)
		super(Anubis, self).__init__(difficulty, *args)
		self.CountDown = 5
		self.Underworld = False
	
	def Spell(self, name = "Path to the Underworld"):
		print name
		self.Underworld = True
		self.MP -= self.spellCost
		print "Soul will be taken away in 5 turns!"
		return 0
	
	def Special(self, name = "Rogue Spirit"):
		print name
		damage = 0
		if self.Underworld:
			self.CountDown += 1
			self.MP -= self.specialCost
			print "One of the spirits dragging you down attacked!  Your soul has gained one more turn."
			damage = 5 - self.CountDown
		damage += int(self.magic*1.5)
		print "%r damage!" % damage
		return damage
	
	def Decide(self):
		damage = 0
		choice = random.randint(0, 99)
		
		if not self.Underworld:
			if choice < 30:
				damage = self.Attack()
			elif choice < 80:
				damage = self.Spell()
			else:
				damage = self.Special()
			
			return damage
		
		else:
			if self.CountDown > 1:
				self.CountDown -= 1
				if choice < 80:
					print "%r turns until your soul is taken." % self.CountDown
					damage = self.Attack()
				else:
					print "%r turns until your soul is taken." % self.CountDown
					damage = self.Special()
				
			else:
				damage = 999
				print "Your soul has been taken."

			return damage
		

class RoShamBo(Enemy):
	def __init__(self, difficulty = 0, power = 4, MaxHP = 30, magic = 5, MaxMP = 30, speed = 30, name = "Ro Sham Bo", spellCost = 0, specialCost = 3):
		args = (3, 30, 5, 10, 99, "Ro Sham Bo", 0, 3)
		super(RoShamBo, self).__init__(difficulty, *args)
		
	#This monster does nothing besides playing Rock-Paper-Scissors with you	
		
	def Decide(self):
		choice = random.randint(0, 2)
		print '"Let\'s play Ro Sham Bo!"'
		PlayerChoice = None
		RockPaperScissors = ["Rock", "Paper", "Scissors"]
		damage = 0
		
		while not isValidAction(PlayerChoice, 3):
		
			print "1. Rock\n2. Paper\n3. Scissors"		
			PlayerChoice = raw_input("> ")
		
		#For enemy, 0 = Scissors, 1 = Rock, 2 = Paper
		#If enemy choice = (your choice + 1) % 3, enemy wins, and vice versa
		
		PlayerChoice = int(PlayerChoice)
		
		if choice == PlayerChoice%3:
			print "Ro Sham Bo chose %r!  It's a tie!  Ro Sham Bo attacks!" % RockPaperScissors[choice]
			damage = self.Attack()
		elif choice == (PlayerChoice+1)%3:
			print "Ro Sham Bo chose %r!  Ro Sham Bo attacks twice!" % RockPaperScissors[choice]
			damage = self.Attack()
			damage += self.Attack()
		else:
			print "Ro Sham Bo chose %r!  You win!  Ro Sham Bo heals you!" % RockPaperScissors[choice]
			damage = -1*(self.magic)
			heal = -1*damage
			print "Healed %r HP!" % heal
			
		
		return damage


class BlackKnight(Enemy):
	def __init__(self, difficulty = 0, power = 6, MaxHP = 25, magic = 0, MaxMP = 15, speed = 25, name = "Black Knight", spellCost = 4, specialCost = 5):
		args = (3, 30, 5, 10, 99, "Black Knight", 4, 5)
		super(BlackKnight, self).__init__(difficulty, *args)

	def Spell(self, name = "Giant Fireball!"):	
		print name
		damage = int(2*self.magic)
		print "%r damage!" % damage
		self.MP -= self.spellCost
		return damage
	
	def Special(self, name = "I'm not dead yet!"):
		print name
		damage = self.power + (self.MaxHP-self.HP)/5
		self.MP -= self.specialCost
		print "%r damage!" % damage
		return damage

class KingOfDreams(Enemy):
	def __init__(self, difficulty = 0, power = 8, MaxHP = 50, magic = 7, MaxMP = 50, speed = 99, name = "King of Dreams", spellCost = 4, specialCost = 5):
		args = (3, 30, 5, 10, 99, "King of Dreams", 4, 5)
		super(KingOfDreams, self).__init__(difficulty, *args)
		self.Fire = 0
		self.Charging = False
		
	def setHP(self, newHP):
		if self.Fire > 0:
			self.HP -= (self.HP - newHP)/2
			print "Ring of Fire lowered damage by half!"
		else:
			self.HP = newHP
		
		if self.HP < 0:
			self.HP = 0
		if self.HP > self.MaxHP:
			self.HP = self.MaxHP
		print "%r: %r/%r HP" % (self.name, self.HP, self.MaxHP) 
			
	def Spell1(self, name = "Absorb"):
		print name
		self.MP -= self.spellCost
		damage = self.magic
		print "%r absorbed %r HP!" % (self.name, damage/2)
		self.setHP(self.HP + damage/2)
		return damage

	def Spell2(self, name = "Ring of Fire"):
		print name
		self.Fire = 4
		self.MP -= self.spellCost
		print "A huge ring of fire has appeared around %r!  It will slowly damage you and prevent you from doing full damage!" % self.name
		return 0
	
	def Special(self, name = "Oblivion"):
		self.MP -= self.specialCost
		if not self.Charging:
			print "%r is charging!" % self.name
			self.Charging = True
			return 0
		else:
			self.Charging = False
			print name
			damage = int(1.5*self.magic + self.power)
			print "%r charges forward!" % self.name
			damage += self.Attack()
			print "%r damage!" % damage
			return damage
	
	def Decide(self):
		choice = random.randint(0, 99)
		damage = 0
		
		if self.MP >= self.spellCost:
			if self.HP > self.MaxHP:
				if self.Fire > 0:
					if choice < 60:
						damage = self.Attack()
					else:
						damage = self.Spell1()
				else:
					if choice < 35:
						damage = self.Attack()
					elif choice < 75:
						damage = self.Spell2()
					else:
						damage = self.Spell1()
			else:
				if not self.Charging:
					if choice < 50:
						damage = self.Attack()
					elif choice < 85:
						damage = self.Spell2()
					elif self.MP >= self.specialCost:
						damage = self.Special()
					else:
						damage = self.Attack()
				else:
					damage = self.Special()
			
		if self.Fire > 0:
			damage += 5
			print "5 damage from the fire!"
			self.Fire -= 1
			if self.Fire == 0:
				print "The fire has gone out."			
		
		return damage
			
def getOpponent(enemyMin, enemyMax, difficulty):
	monster = random.randint(enemyMin, enemyMax)

	OpponentList = [
	BabyRobot(difficulty),
	EvilScientist(difficulty),
	LooseCannon(difficulty),
	EvilPlant(difficulty),
	Marauder(difficulty),
	HoodedMan(difficulty),
	ForestGuardian(difficulty),
	MarshMonster(difficulty),
	Dragonfly(difficulty),
	MuddyGuy(difficulty),
	ZombieGladiator(difficulty),
	ZombieLion(difficulty),
	Ghost(difficulty),
	BattleCaster(difficulty),
	Anubis(difficulty),
	RoShamBo(difficulty),
	BlackKnight(difficulty),
	BattleCaster(difficulty, 4, 35, 6, 35),
	KingOfDreams(difficulty)]
	
	return OpponentList[monster]
	
def isValidAction(actionChoice, maxActions): #Put back in here for RoShamBo
	
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
