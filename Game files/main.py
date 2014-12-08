#####
#Graphics taken with minor changes from:
#https://www.iconfinder.com/icons/85607/download/png/30
#http://payload41.cargocollective.com/1/6/222850/3135466/ItalyTowerIllustration-01.png
#https://cdn1.iconfinder.com/data/icons/halloween-6/96/Skull-512.png
####
import math
import pygame
import sys
from pygame.locals import *
from map import *
from makeMap import *
from tower import *
from towerAttack import *
from enemy import *
from player import *
from menu import *
from globals import *

def bulletOutRadius(bullet):
	minX = bullet.originalX - bullet.radius
	maxX = bullet.originalX + bullet.radius
	minY = bullet.originalY - bullet.radius
	maxY = bullet.originalY + bullet.radius
	if ((bullet.rect.centerx > maxX or bullet.rect.centerx < minX) or
		(bullet.rect.centery > maxY or bullet.rect.centery < minY)):
		return True

def inRadius(tower,enemy):
	#towers a list
	#enemies a sprite grouop
	# if enemy in radius of tower then shoot
	dist = 0
	xDist = tower.x - enemy.rect.centerx
	yDist = tower.y - enemy.rect.centery
	dist = (xDist**2 + yDist**2) **0.5
	if dist <= tower.radius:
		return True

def gameStartAttack(towers,enemies):
	for tower in towers:
		for enemy in enemies:
			if inRadius(tower,enemy):
				tower.launchAttack()
				

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

def main():
	pygame.init()
	FPS = 30
	FPSCLOCK = pygame.time.Clock()

	difficulty = 0
	player = Player(difficulty)
	player.setHighScore() #get highscore from tempDir, or create file

	level = player.level
	wave = player.wave

	towers = []
	enemyLevel = 1

	DISPLAYSURF.fill(WHITE)
	pygame.display.set_caption('T O W E R   D E F E N S E')
	gameMap = Map(level)
	
	enemyCount = 0
	instr = True
	done = False
	noSelect = True
	pause = False
	mapBuild = False
	towerType = None
	gameOver = False
	win = False
	enemy_hit_list = None
	inGamePause = False
	choose = True
	backUpMap = None
	
	while True:
		"""HOME PAGE"""
		while noSelect:
			DISPLAYSURF.blit(startScreenBkgd,(0,0))
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					cursorX = pygame.mouse.get_pos()[0]
					cursorY = pygame.mouse.get_pos()[1]
					#start gamePlay
					if (cursorX in xrange(startButtonX,startButtonX+startButtonWidth) and 
						cursorY in xrange(startButtonY,startButtonY+startButtonHeight)):
						noSelect = False
					elif (cursorX in xrange(mapButtonX,mapButtonX+mapButtonWidth) and 
						cursorY in xrange(mapButtonY,mapButtonY+mapButtonHeight)):
						#lead to map screen
						mapBuild = True
						while mapBuild:
							gameMap = draw()
							backUpMap = gameMap
							pygame.display.flip()
							mapBuild = False
					elif (cursorX in xrange(instrButtonX,instrButtonX+instrButtonWidth) and 
						cursorY in xrange(instrButtonY,instrButtonY+instrButtonHeight)):
						instr = True
						while instr:
							DISPLAYSURF.blit(instructionsScreen,(0,0))
							if instrScreen():
								instr = False
							pygame.display.flip()

			pygame.display.flip()

		"""CHOOSE DIFFICULTY MODE"""
		if player.level == 4:
			while choose:
				DISPLAYSURF.blit(modeIMG,(0,0))
				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
					if event.type == MOUSEBUTTONDOWN:
						mouseX = pygame.mouse.get_pos()[0]
						mouseY = pygame.mouse.get_pos()[1]
						# easy mode
						if (mouseX in xrange(easyX,easyX+easyWidth) and 
							mouseY in xrange(easyY,easyY+easyWidth)):
							difficulty = 0
							player.difficulty = difficulty
							choose = False
						elif (mouseX in xrange(hardX,hardX+hardWidth) and 
							mouseY in xrange(hardY,hardY+hardWidth)):
							difficulty = 1
							player.difficulty = difficulty
							choose = False
						player.update()
				pygame.display.flip()

		gameMap.drawMap()

		"""FIRST TIME INSTRUCTION SCREEN"""
		if player.level == 4:
			while instr:
				DISPLAYSURF.blit(instrBeginIMG,(instrBeginX,instrBeginY))
				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
					if event.type == MOUSEBUTTONDOWN:
						instr = False
				pygame.display.flip()


		"""MENU"""
		pygame.draw.rect(DISPLAYSURF, WHITE, (menuX,menuY,endMenuX,endMenuY))
		playerMenuFont = pygame.font.Font("Neou-Bold.ttf",16)
		towerMenuFont = pygame.font.Font("Neou-Bold.ttf",12)
		
		playerMenu = Menu(player,playerMenuFont)
		playerMenu.update(player)

		startWhiteBkgdX = 242
		startWhiteBkgdY = 600
		DISPLAYSURF.blit(enemyInfo,(startWhiteBkgdX,startWhiteBkgdY)) 

		towerMenu = towersMenu(None,towerMenuFont)
		towerMenu.update(None)
		
		selectTowersMenu = TowerIcons()
		subRightMenu = subMenu()

		row = None
		col = None

		mouseX = pygame.mouse.get_pos()[0]
		mouseY = pygame.mouse.get_pos()[1]

		"""SHOW INFO ABOUT TOWER WHEN HOVERED OVER ICON"""
		if mouseX in xrange(menuX,endMenuX) and mouseY in xrange(menuY,endMenuX):
			if (mouseX in xrange(icon0startX,icon0startX+radius) and 
				mouseY in xrange(icon0startY,icon0startY+radius)):
				#icon tower 0
				iconTower = Tower0(0,0,gameMap)
				towerMenu.update(iconTower)
			if (mouseX in xrange(icon1startX,icon1startX+radius) and 
				mouseY in xrange(icon1startY,icon1startY+radius)):
				#icon tower 1
				iconTower = Tower1(0,0,gameMap)
				towerMenu.update(iconTower)
			if (mouseX in xrange(icon2startX,icon2startX+radius) and 
				mouseY in xrange(icon2startY,icon2startY+radius)):
				iconTower = Tower2(0,0,gameMap)
				towerMenu.update(iconTower)
			if (mouseX in xrange(icon3startX,icon3startX+radius) and 
				mouseY in xrange(icon3startY,icon3startY+radius)):
				iconTower = Tower3(0,0,gameMap)
				towerMenu.update(iconTower)

		else:
			# on map, hover over circles
			box = getSpotClicked(gameMap.map, gameMap.cellSize, 
								mouseY, mouseX)
			row = box[0]
			col = box[1]
			if (isinstance(gameMap.map[row][col],Tower0) or
				isinstance(gameMap.map[row][col],Tower1) or 
				isinstance(gameMap.map[row][col],Tower2) or
				isinstance(gameMap.map[row][col],Tower3)):
				tower = gameMap.map[row][col]
				towerMenu.update(tower)

		"""GAME PLAY"""
		#event handling for special user events
		if pygame.event.get(startId):
				pygame.time.set_timer(startId,400)
				gameStartAttack(towers,enemies_List)
				inGamePause = False
		if pygame.event.get(launchId):
				pygame.time.set_timer(launchId,2000)
				pygame.time.set_timer(eraseMissileId,2000)
				if enemyCount < player.waveCount:
					enemyLaunch(gameMap.map,enemyLevel,gameMap.pathList,player.level)
					enemyCount += 1
		if pygame.event.get(eraseMissileId):
			missileList.empty()
			# attackList.empty()
		if pygame.event.get(pauseId):
				pygame.time.set_timer(startId,0)
				pygame.time.set_timer(launchId,0)
				inGamePause = True
				while inGamePause:
					for event in pygame.event.get():
						if event.type == QUIT:
							pygame.quit()
							sys.exit()
						if event.type == MOUSEBUTTONDOWN:
							mouseX = event.pos[0]
							mouseY = event.pos[1]
							if (mouseX in xrange(subMenuPauseButtonX,subMenuPauseButtonX+subMenuButtonWidth) and 
								mouseY in xrange(subMenuPauseButtonY,subMenuPauseButtonY+subMenuButtonHeight)):
								pygame.time.set_timer(startId,400)
								pygame.time.set_timer(launchId,2000)
								inGamePause = False
		
		if pygame.event.get(restartId):
			pygame.time.set_timer(startId,0)
			pygame.time.set_timer(launchId,0)
			enemies_List.empty()
			attackList.empty()
			all_sprites_list.empty()
			towers = []
			if backUpMap != None:
				gameMap = backUpMap
			else:
				gameMap = Map(player.level)
			player.restart()

			enemyCount = 0
		if pygame.event.get(homeId):
			pygame.time.set_timer(startId,0)
			pygame.time.set_timer(launchId,0)
			enemies_List.empty()
			attackList.empty()
			all_sprites_list.empty()
			towers = []
			main()

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if event.type == MOUSEBUTTONDOWN:
				mouseX = event.pos[0]
				mouseY = event.pos[1]
				box = getSpotClicked(gameMap.map, gameMap.cellSize, 
									mouseY, mouseX)
				
				#check if have selected tower from map, can upgrade
				row = box[0]
				col = box[1]
				selection = gameMap.map[row][col]
				if (isinstance(selection,Tower0) or isinstance(selection,Tower1)
					or isinstance(selection,Tower2)or isinstance(selection,Tower3)):
					selectedTower = selection
					if player.money >= selectedTower.upgradeCost:
						player.money -= selectedTower.upgradeCost
						selectedTower.upgrade()

				#check if have selected tower from menu
				
				if (mouseX in xrange(icon0startX,icon0startX+radius) and 
					mouseY in xrange(icon0startY,icon0startY+radius)):
					tower = Tower0(0,0,gameMap)
					if player.money >= tower.cost:
						towerType = "tower0"

				if (mouseX in xrange(icon1startX,icon1startX+radius) and 
					mouseY in xrange(icon1startY,icon1startY+radius)):
					tower = Tower1(0,0,gameMap)
					if player.money >= tower.cost:
						towerType = "tower1"
				
				if (mouseX in xrange(icon2startX,icon2startX+radius) and 
					mouseY in xrange(icon2startY,icon2startY+radius)):
					tower = Tower2(0,0,gameMap)
					if player.money >= tower.cost:
						towerType = "tower2"

				if (mouseX in xrange(icon3startX,icon3startX+radius) and 
					mouseY in xrange(icon3startY,icon3startY+radius)):
					tower = Tower3(0,0,gameMap)
					if player.money >= tower.cost:
						towerType = "tower3"

				#check if selected from subMenu
				#start game
				if (mouseX in xrange(subMenuStartButtonX,subMenuStartButtonX+subMenuButtonWidth) and 
					mouseY in xrange(subMenuStartButtonY,subMenuStartButtonY+subMenuButtonHeight)):
					pygame.event.post(STARTGAME)
					pygame.event.post(LAUNCHENEMIES)
				#pause game
				if (mouseX in xrange(subMenuPauseButtonX,subMenuPauseButtonX+subMenuButtonWidth) and 
					mouseY in xrange(subMenuPauseButtonY,subMenuPauseButtonY+subMenuButtonHeight)):
					pygame.event.post(PAUSE)
				#restart game
				if (mouseX in xrange(subMenuRestartButtonX,subMenuRestartButtonX+subMenuButtonWidth) and 
					mouseY in xrange(subMenuRestartButtonY,subMenuRestartButtonY+subMenuButtonHeight)):
					pygame.event.post(RESTART)
				#go home
				if (mouseX in xrange(subMenuHomeButtonX,subMenuHomeButtonX+subMenuButtonWidth) and 
					mouseY in xrange(subMenuHomeButtonY,subMenuHomeButtonY+subMenuButtonHeight)):
					pygame.event.post(HOME)

				if towerType != None:
					clicked = True
					while clicked:
						for event in pygame.event.get():
							if event.type == QUIT:
								pygame.quit()
								sys.exit()
							if (event.type == MOUSEBUTTONDOWN and
								not(event.pos[0] in xrange(menuX,endMenuX) and
								(event.pos[1] in xrange(menuY,endMenuY)))):
								placement = getSpotClicked(gameMap.map, 
															gameMap.cellSize, 
															event.pos[1], 
															event.pos[0])
								if  towerType== "tower0":
									tower = Tower0(placement[1],placement[0],gameMap.map)
									if player.money >= tower.cost:
										if placeTower(gameMap.map,placement,
														tower,gameMap.cellSize):
											towers.append(tower)
											player.money -= tower.cost
									clicked = False
									towerType = None
								if  towerType== "tower1":
									tower = Tower1(placement[1],placement[0],gameMap.map)
									if player.money >= tower.cost:
										if placeTower(gameMap.map,placement,
														tower,gameMap.cellSize):
											towers.append(tower)
											player.money -= tower.cost
									clicked = False
									towerType = None
								elif towerType == "tower2":
									tower = Tower2(placement[1],placement[0],gameMap.map)
									if player.money >= tower.cost:
										if placeTower(gameMap.map,placement,
														tower,gameMap.cellSize):
											towers.append(tower)
											player.money -= tower.cost
									clicked = False
									towerType = None
								elif towerType == "tower3":
									tower = Tower3(placement[1],placement[0],gameMap.map)
									if player.money >= tower.cost:
										if placeTower(gameMap.map,placement,
														tower,gameMap.cellSize):
											towers.append(tower)
											player.money -= tower.cost
									clicked = False
									towerType = None

							elif event.type == QUIT:
								pygame.quit()
								sys.exit()

		for enemy in enemies_List:
			if not(enemy.rect.x in xrange(winWidth) or 
					enemy.rect.y in xrange(winHeight)):
				enemy.kill()
			if enemy.health <= 0:
				enemy.kill()
				enemyWorth = 10
				player.money += enemyWorth
			if enemy.end:
				enemy.kill()
				player.lives -= 1
				if player.lives == 0:
					gameOver = True
			# print "num bullets in attackList: ", len(attackList)
			# print "num bullets in missile list: ", len(missileList)

		for enemy in enemies_List:
			#taken with minor changes from:
			#http://www.pygame.org/project-Basic+TD-1337-.html
		 	pygame.draw.line(DISPLAYSURF, (0,0,0), (enemy.rect.left,enemy.rect.top-2),\
				(enemy.rect.right,enemy.rect.top-2), 3)
			pygame.draw.line(DISPLAYSURF, (255,0,0), (enemy.rect.left,enemy.rect.top-2),\
				(enemy.rect.left+(enemy.health*1.0/enemy.starthealth*1.0)\
				*enemy.rect.width,enemy.rect.top-2), 3)

		if len(enemies_List) == 0 and enemyCount == player.waveCount:
			#wave is over
			done = True

		enemy_hit_list = pygame.sprite.groupcollide(enemies_List,attackList,False,False)
		
		if enemy_hit_list != None:
			for item in enemy_hit_list.keys():
				shotList = enemy_hit_list[item]
				for shot in shotList:
					damage = shot.attack
					item.health -= damage
					shot.kill()
		for attack in attackList:
			newHitList = pygame.sprite.spritecollide(attack,enemies_List,True)	

		for bullet in attackList:
			if bulletOutRadius(bullet):
				bullet.kill()
		for missile in missileList:
			if bulletOutRadius(missile):
				missile.kill()

		if done:
			if player.wave >= player.maxWave and player.level <= player.maxLevel:
				#increase level once wave reaches max wave
				player.level += 1
				if player.level > player.maxLevel:
					win = True
				else:
					pause = True
				player.wave = 1
				enemyCount = 0
				done = False
				enemyLevel = 1
				gameMap = Map(player.level)

			elif player.wave < player.maxWave:
				player.wave += 1
				player.update()
				enemies_List.empty()
				enemyLevel += 1
				enemyCount = 0
				done = False
		
		while pause:
			pygame.time.set_timer(startId, 0)
			pygame.time.set_timer(launchId, 0)
			DISPLAYSURF.blit(pauseScreen,(0,0))
			enemies_List.empty()
			attackList.empty()
			all_sprites_list.empty()
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == MOUSEBUTTONDOWN:
					towers = []
					gameMap.drawMap()
					pause = False
			pygame.display.flip()

		count = 0
		while win:
			if count == 0:
				player.addHighScore()
			pygame.time.set_timer(startId, 0)
			pygame.time.set_timer(launchId, 0)
			DISPLAYSURF.blit(winScreen,(0,0))
			enemies_List.empty()
			attackList.empty()
			all_sprites_list.empty()
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == MOUSEBUTTONDOWN:
					towers = []
					gameMap = Map(1)
					gameOver = False
					win = False
					main()
			pygame.display.flip()

		while gameOver:
			pygame.time.set_timer(startId, 0)
			pygame.time.set_timer(launchId, 0)
			DISPLAYSURF.blit(gameOverScreen,(0,0))
			enemies_List.empty()
			attackList.empty()
			all_sprites_list.empty()
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == MOUSEBUTTONDOWN:
					towers = []
					gameMap = Map(1)
					gameOver = False
					main()
			pygame.display.flip()

		FPSCLOCK.tick(FPS)
		attackList.draw(DISPLAYSURF)
		missileList.draw(DISPLAYSURF)
		enemies_List.draw(DISPLAYSURF)
		all_sprites_list.update()
		enemies_List.update()
		pygame.display.update()