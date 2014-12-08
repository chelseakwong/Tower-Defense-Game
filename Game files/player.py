from __future__ import with_statement # for Python 2.5 and 2.6
from globals import *
import os

class Player:
	def __init__(self,difficulty):
		self.difficulty = difficulty
		self.money = 300
		self.original= 300
		self.wave = 1 
		self.maxWave = 3
		self.level = 4
		self.maxLevel = 4
		self.highScore = None
		if self.difficulty == 0:
			#easy mode
			self.waveCount = self.wave * 4 * self.level
			self.lives = 8
		else:
			self.waveCount = self.wave * 6 * self.level
			self.lives = 5
	
	def update(self):	
		if self.difficulty == 0:
			#easy mode
			self.waveCount = self.wave * 4 * self.level
			self.lives = 8
		else:
			#hard mode
			self.waveCount = self.wave * 6 * self.level
			self.lives = 5

	def restart(self):
		if self.difficulty == 0:
			self.lives = 8
		elif self.difficulty == 1:
			self.lives = 5
		self.wave = 1
		self.original = 300

	# from class notes
	def readFile(self,filename, mode="rt"):
		# rt = "read text"
		with open(filename, mode) as fin:
			return fin.read()

	# from class notes
	def writeFile(self,filename, contents, mode="wt"):
	# wt = "write text"
		with open(filename, mode) as fout:
			fout.write(contents)

	def findHighScore(self,path):
		# search for highest score in file
		scoreFile = self.readFile(path)
		scores = scoreFile.split(",")
		intscores= []
		for i in scores:
			if len(i)>0:
				j = int(i) 
				intscores += [j] #add each entry to a list
		if intscores == []: self.highScore = "NONE" #initialize score = None
		else: self.highScore = str(max(intscores))

	def addHighScore(self):
		# at end of game, add score to file
		path = "tempDir" + os.sep + "sameGameHighScore.txt"
		newContent = str(self.money) + "," #separate list with comas
		oldContent = str(self.readFile(path))
		contents = oldContent + newContent 
		#overwrite old file with updated content
		self.writeFile(path, contents)

	def setHighScore(self): 
		# find the high score of file
		path = "tempDir" + os.sep + "sameGameHighScore.txt"
		if (not os.path.exists("tempDir")):
			# doesn't exist, then set highscore to None
			self.highScore = "None"
			os.makedirs("tempDir") #make directory
			assert(os.path.exists("tempDir"))
			self.writeFile(path,"") #add nothing to file
		else: 
			# get max score from file
			self.findHighScore(path)