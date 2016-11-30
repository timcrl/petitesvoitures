###########################################################################
#                                                                         #
# Copyright Timothee CAREL, 2016 (C)                                      #
#                                                                         #
# This file is part of Petites voitures                                   #
#                                                                         #
# Petites voitures is free software: you can redistribute it and/or modify#
# it under the terms of the GNU General Public License as published by    #
# the Free Software Foundation, either version 3 of the License, or       #
# (at your option) any later version.                                     #
#                                                                         #
# Petites voitures is distributed in the hope that it will be useful,     #
# but WITHOUT ANY WARRANTY; without even the implied warranty of          #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
# GNU General Public License for more details.                            #
#                                                                         #
# You should have received a copy of the GNU General Public License       #
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.         #
#                                                                         #
###########################################################################

import pygame
import time
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

class interract:
	
	def __init__(self, circuitNumber):
		
		#### CIRCUIT 1 #####
		if self.circuitNumber = 1
			window.fill((0,20,0))
			self.circuitcolor = [240, 245, 255]
			self.startline = [[300, 20], [300, 120]]
			self.circuitrectangles = [ [20, 20, 200, 440], [420, 20, 200, 440], [220, 20, 200, 100], [220, 360, 200, 100] ]
			self.startp1 = [310, 75]
			self.startp2 = [310, 100]
			self.startp3 = [310, 50]
			self.startp4 = [310, 25]
		#'''

		#### CIRCUIT 2 #####
		#'''
			self.window.fill((0, 0, 50))
			self.circuitcolor = [200, 200, 200]
			self.startline = [[320, 350], [320, 460]]
			self.circuitrectangles = [[20, 20, 150, 440], [470, 20, 150, 440], [170, 350, 300, 110], [170, 20, 40, 120], [210, 60, 40, 120], [250, 100, 40, 120], [290, 140, 60, 120], [350, 100, 40, 120], [390, 60, 40, 120], [430, 20, 40, 120] ]
			self.startp1 = [330, 370]
			self.startp2 = [330, 390]
			self.startp3 = [330, 410]
			self.startp4 = [330, 430]
		#'''

		
	def getchoice():

		playerschoice = [0, 0]
		print("Please press arrowkeys to move")
		
		#Key states
		leftDown = False
		rightDown = False
		upDown = False
		downDown = False
		kp1Down = False
		kp2Down = False
		kp3Down = False
		kp4Down = False
		kp5Down = False
		kp6Down = False
		kp7Down = False
		kp8Down = False
		kp9Down = False
	
		while upDown == False and downDown == False and leftDown == False and rightDown == False and kp1Down == False and kp2Down == False and kp3Down == False and kp4Down == False and kp5Down == False and kp6Down == False and kp7Down == False and kp8Down == False and kp9Down == False:

			#Key detection
			for event in GAME_EVENTS.get():

				if event.type == pygame.KEYDOWN: # Dertect if keys are pressed (down)

					if event.key == pygame.K_LEFT:
						leftDown = True
					if event.key == pygame.K_RIGHT:
						rightDown = True
					if event.key == pygame.K_UP:
						upDown = True
					if event.key == pygame.K_DOWN:
						downDown = True
					
					if event.key == pygame.K_KP1:
						kp1Down = True
					if event.key == pygame.K_KP2:
						kp2Down = True
					if event.key == pygame.K_KP3:
						kp3Down = True
					if event.key == pygame.K_KP4:
						kp4Down = True
					if event.key == pygame.K_KP5:
						kp5Down = True
					if event.key == pygame.K_KP6:
						kp6Down = True
					if event.key == pygame.K_KP7:
						kp7Down = True 
					if event.key == pygame.K_KP8:
						kp8Down = True
					if event.key == pygame.K_KP9:
						kp9Down = True

					if event.key == pygame.K_ESCAPE:
						quitGame()

				if event.type == pygame.KEYUP: # detects if keys are released (up)

					if event.key == pygame.K_LEFT:
						leftDown = False
					if event.key == pygame.K_RIGHT:
						rightDown = False
					if event.key == pygame.K_UP:
						upDown = False
					if event.key == pygame.K_DOWN:
						downDown = False
				
					if event.key == pygame.K_KP1:
						kp1Down = False	
					if event.key == pygame.K_KP2:
						kp2Down = False
					if event.key == pygame.K_KP3:
						kp3Down = False
					if event.key == pygame.K_KP4:
						kp4Down = False
					if event.key == pygame.K_KP5:
						kp5Down = False
					if event.key == pygame.K_KP6:
						kp6Down = False
					if event.key == pygame.K_KP7:
						kp7Down = False
					if event.key == pygame.K_KP8:
						kp8Down = False
					if event.key == pygame.K_KP9:
						kp9Down = False
				
				
				if event.type == GAME_GLOBALS.QUIT: # Detects if the window is closed
					quitGame()

			#change the value of the player's choice variable depending on what keys have been pressed
			if downDown == True :
				playerschoice[1] += 10

			if upDown == True :
				playerschoice[1] -= 10

			if leftDown == True :
				playerschoice[0] -= 10

			if rightDown == True :
				playerschoice[0] += 10
			
			if kp1Down == True :
				playerschoice[0] -= 10
				playerschoice[1] += 10
			
			if kp2Down == True :
				playerschoice[1] += 10
			
			if kp3Down == True :
				playerschoice[0] += 10
				playerschoice[1] += 10
			
			if kp4Down == True :
				playerschoice[0] -= 10
			
			#Do nothing for kp5	
		
			if kp6Down == True :
				playerschoice[0] += 10

			if kp7Down == True :
				playerschoice[0] -= 10
				playerschoice[1] -= 10
			
			if kp8Down == True :
				playerschoice[1] -= 10
		
			if kp9Down == True :
				playerschoice[0] += 10
				playerschoice[1] -= 10

			time.sleep(0.1) # Prevent the program from using all ressources

		return playerschoice
		
	def displayUpdate:
	
		self.window.fill
		
		for x in range(0, len(self.circuitrectangles)):
			pygame.draw.rect(self.window, self.circuitcolor, self.circuitrectangles[x], 0)

		pygame.draw.line(self.window, (0,0,0), self.startline[0], self.startline[1], 3)
