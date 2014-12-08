import pygame
from pygame.locals import *
from globals import *

def enemyLaunch(map,level,pathList,playerLevel):
	enemy = Enemy(GRAY,cellSize,cellSize,map,level,pathList,playerLevel)
	enemies_List.add(enemy)
	all_sprites_list.add(enemy)

class Enemy(pygame.sprite.Sprite): 
	global pathList
	def searchMap(self,keyword):
		for i in xrange(len(self.map)):
			for j in xrange(len(self.map[i])):
				if self.map[i][j] == keyword:
					return [i,j]

	def getSpotClicked(self,map,cellSize,x,y):
		#which box is enemy in
		box = [None,None]
		for i in xrange(len(map)):
			for j in xrange(len(map[i])):
				xTop = i*cellSize
				xBottom = xTop + cellSize
				yTop = j*cellSize
				yBottom = yTop + cellSize
				if x in xrange(xTop,xBottom):
					box[1] = i #row
				if y in xrange(yTop,yBottom):
					box[0] = j #col
		return box

	def __init__(self, color, width, height, map, level, pathList,playerLevel):
		""" Constructor. Pass in the color of the block,
		and its x and y position. """
 
		# Call the parent class (Sprite) constructor
		super(Enemy,self).__init__()

		# Create an image of the block, and fill it with a color.
		# This could also be an image loaded from the disk.
		self.level = level
		if self.level == 1:
			self.image = skull1
		elif self.level == 2:
			self.image = skull2
		elif self.level == 3:
			self.image = skull3
		self.map = map
		self.cellSize = cellSize
		self.starthealth = self.level*20*playerLevel
		self.health = self.level*20*playerLevel
 		if playerLevel == 1:
 			self.speed = self.level*1.2
 		elif playerLevel == 2:
 			self.speed = self.level*1.5
 		elif playerLevel == 3:
 			self.speed = self.level*1.7
 		elif playerLevel == 4:
 			self.speed = self.level*1.7

		# Fetch the rectangle object that has the dimensions of the image
		# image.
		# Update the position of this object by setting the values
		# of rect.x and rect.y
		self.rect = self.image.get_rect()
		startBox = self.searchMap("start")
		startX = startBox[0] * self.cellSize
		startY = startBox[1] * self.cellSize
		self.rect.x = startY
		self.rect.y = startX
		self.nextBox = None
		self.movingBox = self.getSpotClicked(self.map,self.cellSize,
											startY,startX)
		self.moves = []
		self.moveX = 1
		self.moveY = 0
		self.end = False
		self.dir = None
		self.oldPlace = 0
		self.pathList = pathList

	def findNextPath(self):
		#return the next box enemy should move to
		if self.oldPlace + 1 < len(self.pathList):
			nextPlace = self.oldPlace + 1
			oldBox = self.pathList[self.oldPlace]
			newBox = self.pathList[nextPlace]
			deltaRow = newBox[0] - oldBox[0]
			deltaCol = newBox[1] - oldBox[1]
			directions = (deltaRow,deltaCol)
			self.dir = directions
			self.nextBox = [oldBox[0]+deltaRow,oldBox[1]+deltaCol]

	def move(self):
		self.findNextPath()
		checkX, checkY = (0,0)
		ofs = 3 #offset to check x and y
		if self.dir == (0,-1):
			checkX = self.rect.right-ofs
			checkY = self.rect.centery
		elif self.dir == (0,1):
			checkX = self.rect.left+ofs
			checkY = self.rect.centery
		elif self.dir == (1,0):
			checkX = self.rect.centerx
			checkY = self.rect.top+ofs
		elif self.dir == (-1,0):
			checkX = self.rect.centerx
			checkY = self.rect.bottom-ofs
		self.movingBox = self.getSpotClicked(self.map,self.cellSize,
											checkX,checkY)
		self.moveX = self.speed * self.dir[1]
		self.moveY = self.speed * self.dir[0]
		if self.movingBox != self.nextBox:
			self.rect.x += self.moveX
			self.rect.y += self.moveY
		elif self.movingBox == self.nextBox:
			self.oldPlace += 1

	def update(self):
		currentRow = self.movingBox[0]
		currentCol = self.movingBox[1]
		if currentRow < rows and currentCol < cols:
			self.move()
		if self.map[self.movingBox[0]][self.movingBox[1]] == 'end':
			self.end = True
