from car import Car
import time, sys
import pygame
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS


#####################################################################
##################  Quit function  ##################################
#####################################################################

def quitGame():
	print("Quit signal sended. Closing the game... ")
	pygame.quit()
	sys.exit()

#####################################################################
##################  Player's choice function  #######################
#####################################################################
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

			if event.type == pygame.KEYDOWN:

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

			if event.type == pygame.KEYUP:

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
				
				
			if event.type == GAME_GLOBALS.QUIT:
				quitGame()

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

#####################################################################
##################  Init  ###########################################
#####################################################################

#Define the size of the window
windowwidth = 640
windowheight = 480

#Set up pygame and the window
pygame.init()
window = pygame.display.set_mode((windowwidth, windowheight))

#### CIRCUIT 1 #####
#'''
window.fill((0,20,0))
circuitcolor = [240, 245, 255]
startline = [[300, 20], [300, 120]]
circuitrectangles = [ [20, 20, 200, 440], [420, 20, 200, 440], [220, 20, 200, 100], [220, 360, 200, 100] ]
startp1 = [310, 75]
startp2 = [310, 100]
startp3 = [310, 50]
startp4 = [310, 25]
#'''

#### CIRCUIT 2 #####
'''
window.fill((0, 0, 50))
circuitcolor = [200, 200, 200]
startline = [[320, 350], [320, 460]]
circuitrectangles = [[20, 20, 150, 440], [470, 20, 150, 440], [170, 350, 300, 110], [170, 20, 40, 120], [210, 60, 40, 120], [250, 100, 40, 120], [290, 140, 60, 120], [350, 100, 40, 120], [390, 60, 40, 120], [430, 20, 40, 120] ]
startp1 = [330, 370]
startp2 = [330, 390]
startp3 = [330, 410]
startp4 = [330, 430]
'''



for x in range(0, len(circuitrectangles)):
	pygame.draw.rect(window, circuitcolor, circuitrectangles[x], 0)

pygame.draw.line(window, (0,0,0), startline[0], startline[1], 3)

pygame.display.update()

#Define players with their start pos
player1 = Car(window, circuitrectangles, startline, startp1, [200, 0, 50], "Tanguy")
player2 = Car(window, circuitrectangles, startline, startp2, [0, 150, 0], "Master")
#player3 = Car(window, circuitrectangles, startline, startp3, [200, 0, 255], "Tanguy")
#player4 = Car(window, circuitrectangles, startline, startp4, [0, 50, 255], "Loic")


#####################################################################
##################  Main Loop  ######################################
#####################################################################


while True:

	print("======= It is now " + player1.name +"'s turn (no " +str(player1.turnnumber) + ")=======" )
	player1.moveit(getchoice())

	print("======= It is now " + player2.name +"'s turn (no " +str(player2.turnnumber) + ")=======" )
	player2.moveit(getchoice())

#	print("======= It is now " + player3.name +"'s turn (no " +str(player3.turnnumber) + ")=======" )
#	player3.moveit(getchoice())

#	print("======= It is now " + player4.name +"'s turn (no " +str(player4.turnnumber) + ")=======" )
#	player4.moveit(getchoice())

	time.sleep(0.002)


