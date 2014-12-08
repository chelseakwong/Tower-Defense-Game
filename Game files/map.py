from globals import *
from tower import *
import copy

class Map:
	def __init__(self,level):
		self.level = level
		if self.level == 0:
			localMap = []
			for row in xrange(20): localMap += [[None]*cols]
			self.map = localMap
			self.pathList = None
		elif self.level == 1:
			self.map = copy.deepcopy(map1)
			self.pathList = mapPath1
		elif self.level == 2:
			self.map = copy.deepcopy(map2)
			self.pathList = mapPath2
		elif self.level ==3:
			self.map = copy.deepcopy(map3)
			self.pathList = mapPath3
		elif self.level == 4:
			self.map = copy.deepcopy(map4)
			self.pathList = mapPath4
		self.bkgdColor = LIGHTGRAY #non-path
		self.pathColor = CYAN #path
		self.rows = rows
		self.cols = cols
		self.cellSize = winWidth/self.rows

	def clear(self):
		newMap = []
		for row in xrange(self.rows): 
			newMap += [[None]*self.cols]
		self.map = newMap

	def hover(self,row,col,tower):
		x = col*self.cellSize + self.cellSize/2
		y = row*self.cellSize + self.cellSize/2
		radius = self.cellSize/2 - 1
		if tower == "tower1":
			pygame.draw.circle(DISPLAYSURF, TOWER1COLOR, (x,y),radius,0)
		elif tower == "tower2":
			pygame.draw.circle(DISPLAYSURF, TOWER2COLOR, (x,y),radius,0)
		elif tower == "tower3":
			pygame.draw.circle(DISPLAYSURF, TOWER3COLOR, (x,y),radius,0)

	def drawMap(self):
		DISPLAYSURF.fill(WHITE)
		for i in xrange(self.rows):
			for j in xrange(self.cols):
				xTop = j*self.cellSize
				xBottom = xTop + self.cellSize
				yTop = i*self.cellSize
				yBottom = yTop + self.cellSize
				radius = self.cellSize/2 - 1
				x = j*self.cellSize + self.cellSize/2
				y = i*self.cellSize + self.cellSize/2
				if self.map[i][j] == "path":
					color = self.pathColor
					pygame.draw.circle(DISPLAYSURF, color, (x,y),radius,0)
				elif self.map[i][j] == None:
					color = self.bkgdColor
					pygame.draw.circle(DISPLAYSURF, color, (x,y),radius,0)
				elif self.map[i][j] == 'start':
					color = GREEN
					pygame.draw.circle(DISPLAYSURF, color, (x,y),radius,0)
				elif self.map[i][j] == 'end':
					color = RED
					pygame.draw.circle(DISPLAYSURF, color, (x,y),radius,0)
				elif (isinstance(self.map[i][j],Tower0)):
					DISPLAYSURF.blit(tower0IMG,(xTop,yTop))
				elif (isinstance(self.map[i][j],Tower1)):
					DISPLAYSURF.blit(tower1IMG,(xTop,yTop))
				elif (isinstance(self.map[i][j],Tower2)):
					DISPLAYSURF.blit(tower2IMG,(xTop,yTop))
				elif (isinstance(self.map[i][j],Tower3)):
					DISPLAYSURF.blit(tower3IMG,(xTop,yTop))
				
				

