from globals import *
from towerAttack import *

def placeTower(map,pos,obj,cellSize):
	row = pos[0]
	col = pos[1]
	if map[row][col] == None:
		map[row][col] = obj
		if isinstance(obj,Tower1): color = BLUE
		elif isinstance(obj,Tower2): color = PURPLE
		return True
	return False

def gameStartAttack(towers):
	for tower in towers:
		tower.launchAttack()
	
class Tower(object):
	def __init__(self,x,y,map):
		self.level = 1
		self.radius = 200
		self.attack = 5
		self.cost = 20
		self.upgradeCost = 10
		self.upgradePoint = 2
		self.row = y
		self.col = x
		self.color = ORANGE
		self.map = map
		self.cellSize = cellSize
		self.id = 0
		self.x = self.col * self.cellSize + self.cellSize/2
		self.y = self.row * self.cellSize + self.cellSize/2

	def startAttack(self):
		attacks = []
		xLocation = self.col * self.cellSize + self.cellSize/2
		yLocation = self.row * self.cellSize + self.cellSize/2
		if self.id == 1:
			newAttackEast = towerAttack(self.color, 3, 3,self.attack, 
								self.map,self.row,self.col,self.radius,
								self.id,(1,0))
			newAttackWest = towerAttack(self.color, 3, 3,self.attack, 
								self.map,self.row,self.col,self.radius,
								self.id,(-1,0))
			newAttackNorth = towerAttack(self.color, 3, 3,self.attack, 
								self.map,self.row,self.col,self.radius,
								self.id,(0,-1))
			newAttackSouth = towerAttack(self.color, 3, 3,self.attack, 
								self.map,self.row,self.col,self.radius,
								self.id,(0,1))
			(newAttackEast.rect.x,newAttackEast.rect.y) = (xLocation,yLocation)
			(newAttackWest.rect.x,newAttackWest.rect.y) = (xLocation,yLocation)
			(newAttackNorth.rect.x,newAttackNorth.rect.y) = (xLocation,yLocation)
			(newAttackSouth.rect.x,newAttackSouth.rect.y) = (xLocation,yLocation)
			attacks.append(newAttackEast)
			attacks.append(newAttackWest)
			attacks.append(newAttackNorth)
			attacks.append(newAttackSouth)
		else:
			newAttack = towerAttack(self.color, 3, 3,self.attack, 
									self.map,self.row,self.col,self.radius,
									self.id)
			newAttack.rect.x = xLocation
			newAttack.rect.y = yLocation
			attacks.append(newAttack)
		return attacks

	def launchAttack(self): 
		shootingList = self.startAttack()
		for attack in shootingList:
			if self.id == 1:
				attackList.add(attack)
			elif self.id == 2 or self.id ==3:
				missileList.add(attack)
		all_sprites_list.add(attackList)
		all_sprites_list.add(missileList)
	def upgrade(self):
		self.attack += self.upgradePoint
		self.level += 1

class Tower0(Tower):
	def __init__(self,x,y,map):
		super(Tower0, self).__init__(x,y,map)
		self.name = "Machine Gun"
		self.radius = 150
		self.img = tower0IMG
		self.id=0
		self.cost = 15
		self.upgradeCost = 7
		self.color = ORANGE

class Tower1(Tower):
	def __init__(self,x,y,map):
		super(Tower1, self).__init__(x,y,map)
		self.name = "Tank"
		self.img = tower1IMG
		self.id=1
		self.cost = 30
		self.color = TOWER1COLOR


class Tower2(Tower):
	def __init__(self,x,y,map):
		super(Tower2, self).__init__(x,y,map)
		self.attack = 7
		self.cost = 60
		self.upgradeCost = 20
		self.upgradePoint = 2
		self.color = PURPLE 
		self.name = "Missile"
		self.img = tower2IMG
		self.radius = 150
		self.id=2

class Tower3(Tower):
	def __init__(self,x,y,map):
		super(Tower3, self).__init__(x,y,map)
		self.attack = 10
		self.cost = 80
		self.upgradeCost = 25
		self.upgradePoint = 3
		self.color = BLUE 
		self.name = "Superb Missle"
		self.img = tower3IMG
		self.radius = 200
		self.id=3
