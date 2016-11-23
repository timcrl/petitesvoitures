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

class Car:
	
	def __init__(self, window, circuit, startline, initpos, color, name):
		self.name = name
		self.startline = startline
		self.inertie = [0, 0]
		self.pos = [initpos]
		self.circuit = circuit
		self.color = color
		self.addmovement = [1, 0]
		self.inwall = False
		self.newpos = [0, 0]
		self.turnnumber = 1
		self.window = window
		pygame.draw.circle(self.window, self.color, self.pos[-1], 3, 3)
		pygame.display.update()
#		print("Init done!")
		
	def moveit(self, playersmovement):
		
		
		self.addmovement = playersmovement #Set the choice of movement of the player into a local variable
			
		if self.inwall == False:
			if self.turnnumber >=2: #if the car has played more than two turns
				#calculate inertie from the last two turns
				self.inertie[0] = self.pos[-1][0] - self.pos[-2][0]
				self.inertie[1] = self.pos[-1][1] - self.pos[-2][1]

			#Calculate new theorical position from last pos, inertie, and the player's choice
			self.newpos = [(self.pos[-1][0] + self.inertie[0] + self.addmovement[0]), (self.pos[-1][1] + self.inertie[1] + self.addmovement[1])]


			if self.incircuit(self.newpos) == True: #if it is in the circuit
				if self.crossline(self.pos[-1], self.newpos, self.startline[0], self.startline[1]) != [] and self.pos[-1][0] > self.newpos[0]: #if it crosses the startline backwards
					print("Startline crossed backwards!")
					self.pos.append(self.pos[0]) #Move the car to the startpos
				else : #if it doesn't cross the start line backwards (and is in the circuit)
					self.pos.append(self.newpos)
			else: #if a wall or more is crossed
				
				
				self.pos.append(self.impactpos(self.pos[-1], self.newpos))
				self.inertie = [0, 0]
				self.inwall = True
			
			# Debug out 
#			print("############ TURN : " + str(self.turnnumber) + " ###########")
			print(self.name + " choosed to move :" + str(self.addmovement))
			print("Your inertie is now : " + str(self.inertie))
			if self.inwall:
				print("You are in a wall")
			if self.crossline(self.pos[-2], self.pos[-1], self.startline[0], self.startline[1]) != []:
				if self.pos[-2][0] < self.pos[-1][0]:
					print(self.name + " wins! Congratulations!")
					
#			print("newpos is : " + str(self.newpos))
#			print("pos list contains : " + str(self.pos))
		
		else: #if the car is in a wall
			print("Your turn is skipped because you are in a wall")
			self.inwall = False #It skips it's turn and is set not to skip it's next turn
		
		self.draw()
		
		self.turnnumber += 1
		
	def draw(self):
#		print("Draw function was called")
		pygame.draw.line(self.window, self.color, self.pos[-1], self.pos[-2], 3)
		pygame.display.update()
		
	def incircuit(self, pos): #Checks if a given point is inside the rectangle areas that define the circuit
	
		incircuit = False
	
		for x in range(0, len(self.circuit)):
			if pos[0] >= self.circuit[x][0] and pos[0] <= self.circuit [x][0] + self.circuit[x][2]:
				if pos[1] >= self.circuit[x][1] and pos[1] <= self.circuit [x][1] + self.circuit[x][3]:
					incircuit = True
					
					
		return incircuit
		
	def impactpos(self, startpos, finishpos):
	
		middlepos = [(startpos[0] + finishpos[0]) / 2, (startpos[1] + finishpos[1]) / 2]
		impactpos = [0, 0]
		
		if self.incircuit(finishpos) == False:
			for x in range(0, 5):
				if self.incircuit(middlepos) == True:
					startpos = middlepos
					middlepos = [(startpos[0] + finishpos[0]) / 2, (startpos[1] + finishpos[1]) / 2]
				if self.incircuit(middlepos) == False:
					finishpos = middlepos
					middlepos = [(startpos[0] + finishpos[0]) / 2, (startpos[1] + finishpos[1]) / 2]
					
		if self.incircuit(startpos):
			impactpos = startpos
			
		if self.incircuit(finishpos):
			impactpos = finishpos
			
		return impactpos
			
		
	def crossline(self, iA, iB, iC, iD): # find the x and y value for the crossing od [AB] and [CD]
		
		#All points are a table of 2 rows, with (for example) iA[0] = xa and iA[1] = ya
		
		crosslines = [-1, -1]
		crosspoint = []
		
	
		
		crosslines = [-1, -1]
		
		mAB = 0
		mCD = 0
		pAB = 0
		pCD = 0
		
		if iA == iB or iC == iD:
			print("Cannot compare, to points of the same line are identical")

		#### Find the cross of (AB) and (CD) if there is one ###
	
		if iB[0] != iA[0]: #If AB is not a veritcal line, find mx + p
			mAB = (iA[1] - iB[1]) / (iA[0] - iB[0])
			pAB = iA[1] - mAB * iA[0]

		if iC[0] != iD[0]: #If CD is not a veritcal line, find mx + p
			mCD = (iC[1] - iD[1]) / (iC[0] - iD[0])
			pCD = iC[1] - mCD * iA[0]
	
		if (iB[0] != iA[0]) and (iC[0] != iD[0]): #If both (AB) and (CD) are not vertical, find the cross points between them
			if mAB != mCD: #If there is a crosspoint (if there are not parallele)
				crosslines[0] = (pCD - pAB) / (mAB - mCD)
				crosslines[1] = mAB * crosslines[0] + pAB
		
		if iA[0] == iB[0]: #If (AB) is vertical and (CD) isn't, find the crosspoint
			if iC[0] != iD[0]:
				crosslines[0] = iA[0]
				crosslines[1] = mCD * iA[0] + pCD
	
		if iC[0] == iD[0]: #If (AB) is vertical and (CD) isn't, find the crosspoint
			if iA[0] != iB[0]:
				crosslines[0] = iC[0]
				crosslines[1] = mAB * iC[0] + pAB
		
		#Defines weather the crossing of (AB) and (CD) is also the crossing of [AB] and [CD] or not 
		
		if crosslines[0] >= min(iA[0], iB[0]) and crosslines[0] <= max(iA[0], iB[0]) and crosslines[0] >= min(iC[0], iD[0]) and crosslines[0] <= max(iC[0], iD[0]) :
	
			if crosslines[1] >= min(iA[1], iB[1]) and crosslines[1] <= max(iA[1], iB[1]) and crosslines[1] >= min(iC[1], iD[1]) and crosslines[1] <= max(iC[1], iD[1]) :
		
				crosspoint.append(crosslines)
	
#		print("%%%%%%%% crosspoint debug %%%%%%%%%")
#		print("iA : " +str(iA))
#		print("iB : " +str(iB))
#		print("iC : " +str(iC))	
#		print("iD : " +str(iD))
#		print("(AB) : y=" +str(mAB) + "x+" +str(pAB))
#		print("(CD) : y=" +str(mCD) + "x+" +str(pCD))
#		print("crosslines : " +str(crosslines))
#		print("crosspoint : " +str(crosspoint))
			
		return crosspoint
		



