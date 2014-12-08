import pygame
import sys
from map import *
from pygame.locals import *
from globals import *

global globalMap

def getSpotClicked(map,cellSize,x,y):
	#which box clicked in
	box = [None,None]
	for i in xrange(len(map)):
		for j in xrange(len(map[i])):
			xTop = j*cellSize
			xBottom = xTop + cellSize
			yTop = i*cellSize
			yBottom = yTop + cellSize
			if x in xrange(xTop,xBottom):
				box[0] = j #row
			if y in xrange(yTop,yBottom):
				box[1] = i #col
	return box

def draw():
	global pathList
	FPS = 30
	FPSCLOCK = pygame.time.Clock()
	level = 0

	DISPLAYSURF.fill(WHITE)
	pygame.display.set_caption('T O W E R   D E F E N S E')
	drawMap = Map(level)
	path = []
	#add row and col of every path, first one is start and last one is end
	done = False
	start = False

	buttonWidth = 124
	buttonHeight = 55
	clearX = 47
	clearY = 621
	doneX = 287
	doneY = 621
	playX = 526
	playY = 622
	building = True

	oldRow = None
	oldCol = None
	while building:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if event.type == MOUSEBUTTONDOWN:
				mouseX = event.pos[0]
				mouseY = event.pos[1]
				#clear button
				if (mouseX in xrange(clearX,clearX+buttonWidth) 
					and mouseY in xrange(clearY,clearY+buttonHeight)):
					drawMap.clear()
					path = []
					start = False
				#done button
				elif (mouseX in xrange(doneX,doneX+buttonWidth) 
						and mouseY in xrange(doneY,doneY+buttonHeight)):
					startPoint = path[0]
					startRow = startPoint[0]
					startCol = startPoint[1]
					endList = len(path)-1
					end = path[endList]
					endRow = end[0]
					endCol = end[1]
					drawMap.map[startRow][startCol] = 'start'
					drawMap.map[endRow][endCol] = 'end'
					#list of moves for enemy to walk through
					
				#play button
				elif (mouseX in xrange(playX,playX+buttonWidth)
						and mouseY in xrange(playY,playY+buttonHeight)):
					#start playing
					building = False
				else:
					start = not(start)
			
			if start and event.type == MOUSEMOTION:
				box = getSpotClicked(drawMap.map, drawMap.cellSize, 
									event.pos[1], event.pos[0])
				row = box[0]
				col = box[1]
				if (row,col) != (oldRow,oldCol):
					oldRow = row
					oldCol = col
					path += [[row,col]]
				drawMap.map[row][col] = 'path'
				

		drawMap.drawMap()
		DISPLAYSURF.blit(mapBuilderMenu,(menuX,menuY))
		pygame.display.update()
		FPSCLOCK.tick(FPS)
	drawMap.pathList = path 
	return drawMap
