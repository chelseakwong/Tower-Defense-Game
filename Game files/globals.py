import pygame
import os

pathList = None

winWidth = 700
winHeight = 700

rows = 20
cols = 20

cellSize = winWidth/rows #35

DISPLAYSURF = pygame.display.set_mode((winWidth,winHeight))

mapbuild = False
towers = []

startId = pygame.USEREVENT + 1
STARTGAME = pygame.event.Event(startId)
launchId = pygame.USEREVENT + 2
LAUNCHENEMIES = pygame.event.Event(launchId)
pauseId = pygame.USEREVENT + 3
PAUSE = pygame.event.Event(pauseId)
restartId = pygame.USEREVENT + 4
RESTART = pygame.event.Event(restartId)
homeId = pygame.USEREVENT + 5
HOME = pygame.event.Event(homeId)
eraseMissileId = pygame.USEREVENT + 6
ERASE = pygame.event.Event(eraseMissileId)


subMenuStartButtonX = 577
subMenuStartButtonY = 611
subMenuPauseButtonX = subMenuStartButtonX
subMenuPauseButtonY = 630
subMenuRestartButtonX = subMenuStartButtonX
subMenuRestartButtonY = 650
subMenuHomeButtonX = subMenuStartButtonX
subMenuHomeButtonY = 670
subMenuButtonWidth = 92
subMenuButtonHeight = 17

startScreenBkgd = pygame.image.load(os.path.join('img','splashScreen.png'))
startButtonX = 304
startButtonWidth = 94
startButtonY = 440
startButtonHeight = 28

pauseScreen = pygame.image.load(os.path.join('img','pausescreen.png'))
mapButtonX = 263
mapButtonY = 475
mapButtonWidth = 177
mapButtonHeight = 27

instrBeginIMG = pygame.image.load(os.path.join('img','instrBegin.png'))
instrBeginX = instrBeginY = 79

modeIMG = pygame.image.load(os.path.join('img','mode.png'))
easyX = 52
easyY = 229
easyWidth = 234
hardX = 399
hardY = 229
hardWidth = easyWidth

instructionsScreen = pygame.image.load(os.path.join('img','instructions.png'))
instrButtonX = 249
instrButtonY = 512
instrButtonWidth = 199
instrButtonHeight = 26

gameOverScreen = pygame.image.load(os.path.join('img','gameoverscreen.png'))

winScreen = pygame.image.load(os.path.join('img','winscreen.png'))

mapBuilderMenu = pygame.image.load(os.path.join('img','mapbuildmenu.png'))

enemyInfo = pygame.image.load(os.path.join('img','enemyinfo.png'))

skull1 = pygame.image.load(os.path.join('img','skull1.png'))
skull2 = pygame.image.load(os.path.join('img','skull2.png'))
skull3 = pygame.image.load(os.path.join('img','skull3.png'))

tower0IMG = pygame.image.load(os.path.join('img','tower0.png'))
tower1IMG = pygame.image.load(os.path.join('img','tower1.png'))
tower2IMG = pygame.image.load(os.path.join('img','tower2.png'))
tower3IMG = pygame.image.load(os.path.join('img','tower3.png'))

icon0startX,icon0startY = (471,610)
icon1startX,icon1startY = (512,651)
icon2startX,icon2startY = (471,651)
icon3startX,icon3startY = (512,610)
radius = 31

subMenuIMG = pygame.image.load(os.path.join('img','submenu.png'))

all_sprites_list = pygame.sprite.Group()
enemies_List = pygame.sprite.Group()
attackList = pygame.sprite.Group() #list of sprites of attacks from tower
missileList = pygame.sprite.Group()

menuX,menuY = (0,595)
endMenuX,endMenuY = (701,701)

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (232,   74,  122)
GREEN    = (  137, 235,  167)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  139, 216, 223)
LIGHTGRAY= (247,247,247)
BLACK = (0,0,0)
TOWER1COLOR = (97,138,77)
TOWER2COLOR = (225,39,236)
TOWER0COLOR = (231,120,13577)
TOWER3COLOR = (138,184,202)

#REALLY LONG LISTS
map1 = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, 'path', 'path', 'path', 'path', 'path', 'path', 'path', None, None, None, None, None, None, None], [None, None, None, None, None, None, 'path', None, None, None, None, None, 'path', None, None, None, None, None, None, None], [None, None, None, None, None, None, 'path', None, None, None, None, None, 'path', None, None, None, None, None, None, None], [None, None, None, None, None, None, 'path', None, None, None, None, None, 'path', None, None, None, None, None, None, None], [None, None, None, None, None, None, 'path', None, None, None, None, None, 'path', None, None, None, None, None, None, None], [None, None, None, None, None, None, 'path', None, None, None, None, None, 'path', None, None, None, None, None, None, None], ['start', 'path', 'path', 'path', 'path', 'path', 'path', None, None, None, None, None, 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'end'], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]

map2 = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], ['start', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, 'path', None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, 'path', None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, 'path', None, None, None, None, None, None, None, None, None, None], [None, None, 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', None, None, None], [None, None, 'path', None, None, None, None, None, None, 'path', None, None, None, None, None, None, 'path', None, None, None], [None, None, 'path', None, None, None, None, None, None, 'path', None, None, None, None, None, None, 'path', None, None, None], [None, None, 'path', None, None, None, None, None, None, 'path', None, None, None, None, None, None, 'path', None, None, None], [None, None, 'path', None, None, None, None, None, None, 'path', None, None, None, None, None, None, 'path', None, None, None], [None, None, 'path', None, None, None, None, None, None, 'path', None, None, None, None, None, None, 'path', None, None, None], [None, None, 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', None, None, None, None, None, None, 'path', None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'path', None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'path', 'path', 'path', 'end'], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]

map3= [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', None, None, None, None, None, None, None, None], [None, None, None, 'path', None, None, None, None, None, None, None, 'path', None, None, None, None, None, None, None, None], [None, None, None, 'path', None, None, None, None, None, None, None, 'path', None, None, None, None, None, None, None, None], ['start', 'path', 'path', 'path', 'path', 'path', 'path', 'path', None, 'path', 'path', 'path', 'path', 'path', 'path', None, None, None, None, None], [None, None, None, 'path', None, None, None, 'path', None, 'path', None, 'path', None, None, 'path', None, None, None, None, None], [None, None, None, 'path', None, None, None, 'path', None, 'path', None, 'path', None, None, 'path', None, None, None, None, None], [None, None, None, 'path', None, None, None, 'path', None, 'path', None, 'path', None, None, 'path', None, None, None, None, None], [None, None, None, 'path', None, None, None, 'path', None, 'path', None, 'path', None, None, 'path', None, None, None, None, None], [None, None, None, 'path', None, None, None, 'path', None, 'path', None, 'path', None, None, 'path', None, None, None, None, None], [None, None, None, 'path', 'path', 'path', 'path', 'path', None, 'path', None, 'path', None, None, 'path', None, None, None, None, None], [None, None, None, None, None, None, None, None, None, 'path', 'path', 'path', 'path', 'path', 'path', None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, 'path', None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, 'path', None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, 'path', None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'end'], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]

map4= [[None, 'start', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, 'path', None, None, 'path', 'path', 'path', 'path', 'path', None, None, None, None, None, None, None, None, None, None, None], [None, 'path', None, None, 'path', None, None, None, 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'end'], [None, 'path', None, None, 'path', None, None, None, 'path', 'path', None, None, None, None, None, None, None, None, None, None], [None, 'path', None, None, 'path', None, None, None, 'path', 'path', None, 'path', 'path', 'path', 'path', None, None, None, None, None], [None, 'path', None, None, 'path', None, None, None, 'path', 'path', None, 'path', None, None, 'path', None, None, None, None, None], [None, 'path', None, None, 'path', None, None, None, 'path', 'path', None, 'path', None, None, 'path', None, None, None, None, None], [None, 'path', None, None, 'path', None, None, None, 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', None, None], [None, 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', None, None, 'path', None, None, 'path', None, None, 'path', None, None], [None, None, None, None, 'path', None, None, None, None, None, None, 'path', None, None, 'path', None, None, 'path', 'path', None], [None, None, None, None, 'path', None, None, None, None, None, None, 'path', None, None, 'path', None, None, None, 'path', None], [None, 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', None, 'path', 'path', None, None, None, 'path', None], [None, 'path', None, None, 'path', None, None, None, None, None, None, None, None, 'path', None, None, None, None, 'path', None], [None, 'path', None, None, 'path', None, None, None, None, None, None, None, None, 'path', None, None, None, None, 'path', None], [None, 'path', 'path', None, 'path', None, None, None, 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', 'path', None], [None, None, 'path', 'path', 'path', None, None, None, 'path', None, None, None, None, 'path', None, None, None, None, None, None], [None, None, None, None, None, None, None, None, 'path', 'path', 'path', 'path', 'path', 'path', None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]

mapPath1 = [[11, 0], [11, 1], [11, 2], [11, 3], [11, 4], [11, 5], [11, 6], [10, 6], [9, 6], [8, 6], [7, 6], [6, 6], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10], [5, 11], [5, 12], [6, 12], [7, 12], [8, 12], [9, 12], [10, 12], [11, 12], [11, 13], [11, 14], [11, 15], [11, 16], [11, 17], [11, 18], [11, 19]]

mapPath2 = [[2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [9, 9], [10, 9], [11, 9], [12, 9], [12, 8], [12, 7], [12, 6], [12, 5], [12, 4], [12, 3], [12, 2], [11, 2], [10, 2], [9, 2], [8, 2], [7, 2], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [6, 10], [6, 11], [6, 12], [6, 13], [6, 14], [6, 15], [6, 16], [7, 16], [8, 16], [9, 16], [10, 16], [11, 16], [12, 16], [13, 16], [14, 16], [14, 17], [14, 18], [14, 19]]

mapPath3 = [[4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [5, 7], [6, 7], [7, 7], [8, 7], [9, 7], [10, 7], [10, 6], [10, 5], [10, 4], [10, 3], [9, 3], [8, 3], [7, 3], [6, 3], [5, 3], [4, 3], [3, 3], [2, 3], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [2, 11], [3, 11], [4, 11], [5, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11], [11, 11], [11, 12], [11, 13], [11, 14], [10, 14], [9, 14], [8, 14], [7, 14], [6, 14], [5, 14], [4, 14], [4, 13], [4, 12], [4, 11], [4, 10], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [9, 9], [10, 9], [11, 9], [11, 10], [12, 10], [13, 10], [14, 10], [15, 10], [15, 11], [15, 12], [15, 13], [15, 14], [15, 15], [15, 16], [15, 17], [15, 18], [15, 19]]

mapPath4 = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [7, 8], [6, 8], [5, 8], [4, 8], [3, 8], [2, 8], [1, 8], [1, 7], [1, 6], [1, 5], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4], [10, 4], [11, 4], [12, 4], [13, 4], [14, 4], [15, 4], [15, 3], [15, 2], [14, 2], [14, 1], [13, 1], [12, 1], [11, 1], [11, 2], [11, 3], [11, 4], [11, 5], [11, 6], [11, 7], [11, 8], [11, 9], [11, 10], [11, 11], [10, 11], [9, 11], [8, 11], [7, 11], [6, 11], [5, 11], [4, 11], [4, 12], [4, 13], [4, 14], [5, 14], [6, 14], [7, 14], [8, 14], [9, 14], [10, 14], [11, 14], [11, 13], [12, 13], [13, 13], [14, 13], [15, 13], [16, 13], [16, 12], [16, 11], [16, 10], [16, 9], [16, 8], [15, 8], [14, 8], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13], [14, 14], [14, 15], [14, 16], [14, 17], [14, 18], [13, 18], [12, 18], [11, 18], [10, 18], [9, 18], [9, 17], [8, 17], [7, 17], [7, 16], [7, 15], [7, 14], [7, 13], [7, 12], [7, 11], [7, 10], [7, 9], [6, 9], [5, 9], [4, 9], [3, 9], [2, 9], [2, 10], [2, 11], [2, 12], [2, 13], [2, 14], [2, 15], [2, 16], [2, 17], [2, 18], [2, 19]]

