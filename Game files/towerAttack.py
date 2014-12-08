from globals import *
import math

class towerAttack(pygame.sprite.Sprite):
 
	def __init__(self,color,width,height,attack,map,row,col,radius,id,dir=(0,0)):
		""" Constructor. Pass in the color of the block,
		and its x and y position. """
 
		# Call the parent class (Sprite) constructor
		# super(towerAttack,self).__init__()
 		pygame.sprite.Sprite.__init__(self,attackList)
 		self.map = map

		# Create an image of the block, and fill it with a color.
		# This could also be an image loaded from the disk.
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.speed = 15
		self.attack = attack
		self.row = row
		self.col = col
		self.closest = None
		# Update the position of this object by setting the values
		# of rect.x and rect.y
		self.rect = self.image.get_rect()
		self.originalX = self.col*cellSize + cellSize/2
		self.originalY = self.row*cellSize + cellSize/2
		self.radius = radius
		self.oldAngle = None
		self.towerId = id
		self.dirX = dir[0]
		self.dirY = dir[1]

	def inRadius(self,enemy):
		#towers a list
		#enemies a sprite grouop
		# if enemy in radius of tower then shoot
		dist = 0
		xDist = self.rect.centerx - enemy.rect.centerx
		yDist = self.rect.y - enemy.rect.centery
		dist = (xDist**2 + yDist**2) **0.5
		if dist <= self.radius:
			return True
	
	def findNearestPath(self):
		#determine direction to shoot at
		oldDist = ((len(self.map)**2)*2)**0.5
		closest = (None,None)
		for pathRow in xrange(len(self.map)):
			for pathCol in xrange(len(self.map[pathRow])):
				if self.map[pathRow][pathCol] == 'path':
					deltaRow = self.row - pathRow
					deltaCol = self.col - pathCol
					newDist = (((deltaRow))**2 + (abs(deltaCol))**2)**0.5
					if newDist < oldDist:
						oldDist = newDist
						self.closest = (pathRow,pathCol)

	def findNearestEnemy(self):
		for enemy in enemies_List:
			if self.inRadius(enemy):
				return enemy

	def tower2Update(self):
		if len(enemies_List)>0:
			target = self.findNearestEnemy()
			if target == None:
				angle = self.oldAngle
			else: 
				aimX = target.rect.centerx
				aimY = target.rect.centery
				deltaX = self.rect.x - aimX
				deltaY = self.rect.y - aimY
				angle = math.atan2(deltaY,deltaX)
				self.oldAngle = angle
		if self.oldAngle != None:
			#taken with minor changes from:
			#http://www.pygame.org/project-Wesnoth+Tower+Defense-2790-.html
			self.rect.x -= math.cos(self.oldAngle)*7
			self.rect.y-= math.sin(self.oldAngle)*7

	def tower1Update(self):
		self.rect.x += self.speed*(self.dirX)
		self.rect.y += self.speed*(self.dirY)

	def tower0Update(self):
		self.findNearestPath()
		rowDirection = self.closest[0]
		colDirection = self.closest[1]
		changeX = 0
		changeY = 0
		if abs(self.row-rowDirection) > 0:
			changeX = (rowDirection-self.row)/abs(rowDirection-self.row)
		if abs(self.col-colDirection) > 0:
			changeY = (colDirection-self.col)/abs(self.col-colDirection)
		self.rect.x += self.speed*(changeY)
		self.rect.y += self.speed*(changeX)

	def update(self): #type 1 shoots straight, type 2 missile, type 3 missile
		if self.towerId == 0:
			self.tower0Update()
		elif self.towerId == 1:
			self.tower1Update()
		elif self.towerId == 2:
			self.tower2Update()
		elif self.towerId == 3:
			self.tower2Update()
			
