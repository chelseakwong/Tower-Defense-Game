from globals import *
from tower import *
import pygame
import sys
from pygame.locals import *

class Menu(object):
	def __init__(self,player,font):
		self.font = font
		self.startY = 605
		self.startX = 15
		self.txtinc = 24
		self.moneyText = "Money: $%d" %(player.money)
		self.levelText = "Level: %d, Wave: %d of %d" %(player.level,player.wave,player.maxWave)
		self.livesText = "Lives: %d" %(player.lives)
		if player.highScore != None:
			self.highScoreText = "High Score: $%s" %(player.highScore)
		else:
			self.highScoreText = "High Score: None"
		

	def update(self,player):
		self.moneyText = "Money: $%d" %(player.money)
		self.levelText = "Level: %d, Wave: %d of %d" %(player.level,player.wave,player.maxWave)
		self.livesText = "Lives: %d" %(player.lives)
		
		moneySurfObj = self.font.render(self.moneyText,True,BLACK)
		moneyRectObj = moneySurfObj.get_rect()
		moneyX,moneyY = (self.startX,self.startY)
		moneyRectObj.topleft = (moneyX,moneyY)
		DISPLAYSURF.blit(moneySurfObj,moneyRectObj)

		levelSurfObj = self.font.render(self.levelText,True,BLACK)
		levelRectObj = levelSurfObj.get_rect()
		levelX,levelY = (self.startX,self.startY+self.txtinc)
		levelRectObj.topleft = (levelX,levelY)
		DISPLAYSURF.blit(levelSurfObj,levelRectObj)

		livesSurfObj = self.font.render(self.livesText,True,BLACK)
		livesRectObj = livesSurfObj.get_rect()
		livesX,livesY = (self.startX,self.startY + 2*self.txtinc)
		livesRectObj.topleft = (livesX,livesY)
		DISPLAYSURF.blit(livesSurfObj,livesRectObj)	

		hsSurfObj = self.font.render(self.highScoreText,True,BLACK)
		hsRectObj = hsSurfObj.get_rect()
		hsX,hsY = (self.startX,self.startY + 3*self.txtinc)
		hsRectObj.topleft = (hsX,hsY)
		DISPLAYSURF.blit(hsSurfObj,hsRectObj)	


class towersMenu(object):
	def __init__(self,tower,font):
		self.font = font
		self.startY = 605
		self.startX = 250
		self.txtinc = 18
		self.color = None
		if tower != None:
			self.nameText = tower.name
			self.damageText = "Damage: %d" %(tower.attack)
			self.costText = "Cost: $%d" %(tower.cost)
			self.upgradeCostText = "Upgrade Cost: %d" %(tower.upgradeCost)
			self.upgradeFeaturesText = "Upgrade tower damage by +%d" %(tower.upgrade)
		else: 
			self.nameText = None
			self.damageText = None
			self.costText = None
			self.upgradeCostText = None
			self.upgradeFeaturesText = None
		
	def update(self,tower):
		if tower != None:
			self.nameText = tower.name + " Level %d" % (tower.level)
			self.damageText = "Damage: %d" %(tower.attack)
			self.costText = "Cost: $%d" %(tower.cost)
			self.upgradeCostText = "Upgrade Cost: %d" %(tower.upgradeCost)
			self.upgradeFeaturesText = "Upgrade tower damage by +%d" %(tower.upgradePoint)
			self.color = WHITE

		else: 
			self.nameText = None
			self.damageText = None
			self.costText = None
			self.upgradeCostText = None
			self.upgradeFeaturesText = None
			self.color = None

		#start white box x y 244,621
		# widht height 209 93
		startWhiteBkgdX = 242
		startWhiteBkgdY = 600
		whiteWidth = 224
		whiteHeight = 98
		if self.color != None:
			pygame.draw.rect(DISPLAYSURF, self.color, 
							(startWhiteBkgdX,startWhiteBkgdY,
							whiteWidth,
							whiteHeight))
		nameSurfObj = self.font.render(self.nameText,True,BLACK)
		nameRectObj = nameSurfObj.get_rect()
		nameX,nameY = (self.startX,self.startY)
		nameRectObj.topleft = (nameX,nameY)
		DISPLAYSURF.blit(nameSurfObj,nameRectObj)

		damageSurfObj = self.font.render(self.damageText,True,BLACK)
		damageRectObj = damageSurfObj.get_rect()
		damageX,damageY = (self.startX,self.startY+self.txtinc)
		damageRectObj.topleft = (damageX,damageY)
		DISPLAYSURF.blit(damageSurfObj,damageRectObj)		

		costSurfObj = self.font.render(self.costText,True,BLACK)
		costRectObj = costSurfObj.get_rect()
		costX,costY = (self.startX,self.startY+2*self.txtinc)
		costRectObj.topleft = (costX,costY)
		DISPLAYSURF.blit(costSurfObj,costRectObj)

		upgradeCostSurfObj = self.font.render(self.upgradeCostText,True,BLACK)
		upgradeCostRectObj = upgradeCostSurfObj.get_rect()
		upgradeCostX,upgradeCostY = (self.startX,self.startY+3*self.txtinc)
		upgradeCostRectObj.topleft = (upgradeCostX,upgradeCostY)
		DISPLAYSURF.blit(upgradeCostSurfObj,upgradeCostRectObj)

		upgradeFeaturesSurfObj = self.font.render(self.upgradeFeaturesText,True,BLACK)
		upgradeFeaturesRectObj = upgradeFeaturesSurfObj.get_rect()
		upgradeFeaturesX,upgradeFeaturesY = (self.startX,self.startY+4*self.txtinc)
		upgradeFeaturesRectObj.topleft = (upgradeFeaturesX,upgradeFeaturesY)
		DISPLAYSURF.blit(upgradeFeaturesSurfObj,upgradeFeaturesRectObj) 

class TowerIcons(object):
	def __init__(self):
		self.startX = 475
		self.startY = 610
		self.inc = 40
		self.basicIcon = tower1IMG
		self.betterIcon = tower2IMG
		self.bestIcon = tower3IMG
		DISPLAYSURF.blit(tower0IMG,(self.startX,self.startY))
		DISPLAYSURF.blit(tower2IMG,(self.startX,self.startY + self.inc))
		DISPLAYSURF.blit(tower3IMG,(self.startX+self.inc,self.startY))
		DISPLAYSURF.blit(tower1IMG,(self.startX+self.inc,self.startY+self.inc))

class subMenu(object):
	def __init__(self):
		self.startX = 576
		self.startY = 610
		DISPLAYSURF.blit(subMenuIMG,(self.startX,self.startY))

def instrScreen():
	for event in pygame.event.get():
		if event.type == MOUSEBUTTONDOWN: 
			return True
		if event.type == QUIT:
			pygame.quit()
			sys.exit()