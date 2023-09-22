import pygame
import time # for count down------------------------->
import sys
#time.sleep(1)
#print (time.asctime())  #today's date and time 
#print (time.time())   #the time when computer first opened to now in sec
#print (time.gmtime()) #being more specific

pygame.init() #initializing pygame----
pygame.font.init() #initializing font ----->

#Total window
WIDTH , HEIGHT = 504 , 650 
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

#color palate--->
MAROON = (78,20,39)
BEIGE = (247, 202, 201)
PINK =(216, 191, 216)
GREEN = (192, 130, 97)
CREAM = (237, 174, 192)
MULBERRY = (112, 41, 99)


#Variable set for timer ------------------------>
COUNTDOWN_MINUTES = 0
COUNTDOWN_SECONDS = 30
COUNTDOWN_MILLISECONDS = 0

# Convert to milliseconds----------------->
countdown = (
    COUNTDOWN_MINUTES * 60 * 1000
    + COUNTDOWN_SECONDS * 1000
    + COUNTDOWN_MILLISECONDS
)  
running = False
game_over = False

#Title and Icon
pygame.display.set_caption("SUDOKU")
img = pygame.image.load('icon.jpg')
pygame.display.set_icon(img)

x = 15
y = 15
dif = 500 / 9
val = 0
FPS = 0  #Frame Per Second 
# Default Sudoku Board.    #grid[i][j]
grid =[
		[7, 8, 0, 4, 0, 0, 1, 2, 0],
		[6, 0, 0, 0, 7, 5, 0, 0, 9],
		[0, 0, 0, 6, 0, 1, 0, 7, 8],
		[0, 0, 7, 0, 4, 0, 2, 6, 0],
		[0, 0, 1, 0, 5, 0, 9, 3, 0],
		[9, 0, 4, 0, 6, 0, 0, 0, 5],
		[0, 7, 0, 3, 0, 0, 0, 1, 2],
		[1, 2, 0, 0, 0, 7, 4, 0, 0],
		[0, 4, 9, 2, 0, 6, 0, 0, 7]
	]

# Font list---------------------->
NUMB_FONT = pygame.font.SysFont('cambria', 30)
TEXT = pygame.font.SysFont('javanesetext', 15)
TIME_FONT = pygame.font.SysFont('javanesetext', 20)
RIGHTS = pygame.font.SysFont('leelawadeeui', 12)

opening = pygame.image.load('sudoku cover.jpg')
opening = pygame.transform.scale(opening, (WIDTH, HEIGHT)) 

def game_opening(): #------------------------>
    WINDOW.blit(opening,(0,0))
    pygame.display.update()
    pygame.time.delay(4000)
    WINDOW.fill(BEIGE)
   
    

def get_cord(pos):
	global x ,y
	x = pos[0]//dif
	y = pos[1]//dif

# Highlight the cell selected
def draw_box():
	for i in range(2):
		pygame.draw.line(WINDOW, GREEN, (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
		pygame.draw.line(WINDOW, GREEN, ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)

# Function to draw required lines for making Sudoku grid-------------------------->		
def draw():
	# Draw the lines
		
	for i in range (0,9):
		for j in range (0,9):
			if grid[i][j]!= 0:

				# Fill blue color in already numbered grid
				pygame.draw.rect(WINDOW,PINK, (i * dif, j * dif, dif + 1, dif + 1))

				# Fill grid with default numbers specified
				text1 = NUMB_FONT.render(str(grid[i][j]), True, MAROON)
				WINDOW.blit(text1, (i * dif + 15+5, j * dif + 15-5))
	# Draw lines horizontally and verticallyto form grid		
	for i in range(10): #for i=1 i<=10 , i++  dif = 500/9 =55.55
		if i % 3 == 0 :
			line_width = 10
		else:
			line_width = 3                   #1, 2
		pygame.draw.line(WINDOW, MAROON, (0, i * dif), (500, i * dif), line_width)
		pygame.draw.line(WINDOW, MAROON, (i * dif, 0), (i * dif, 500), line_width)	
   

# Fill value entered in cell	
def draw_val(val):
	text1 = NUMB_FONT.render(str(val), 1, MAROON)
	WINDOW.blit(text1, (x * dif + 15, y * dif + 15))

# Raise error when wrong value entered
def raise_error1():
	text1 = TEXT.render("WRONG !!!", True, MAROON)
	WINDOW.blit(text1, (190, 600))
def raise_error2():
	text1 = TEXT.render("Wrong !!! Not a valid Key", True, MAROON)
	WINDOW.blit(text1, (100, 600))

# Check if the value entered in board is valid----------------------->
def valid(m, i, j, val):
	for k in range(9):     
		if m[i][k]== val:   # Check row
			return False
		if m[k][j]== val:   # Chcek col
			return False
    #Check the box 
	ROW_BOX = i//3 * 3
	COL_BOX = j//3 * 3
	for i in range(ROW_BOX, ROW_BOX + 3):
		for j in range (COL_BOX, COL_BOX + 3):
			if m[i][j]== val:
				return False
	return True



# Solves the sudoku board using Backtracking Algorithm
def solve(grid, i, j):
	
    #Traversing to find empty cell
	while grid[i][j]!= 0:
		if i<8:      ## row check korbe 
			i+= 1
		elif i == 8 and j<8:   ### row te empty na thakle column check korbe
			i = 0
			j+= 1
		elif i == 8 and j == 8:  ## none empty found 
			return True
	
	for k in range(1, 10):
		if valid(grid, i, j, k)== True:
			grid[i][j]= k
			global x, y
			x = i
			y = j
   
			# Pink color background
			WINDOW.fill((CREAM))
			draw()
			draw_box()
			pygame.display.update()
			pygame.time.delay(20)
			if solve(grid, i, j) == 1:
				return True
			else:
				grid[i][j]= 0
			
			draw()
			draw_box()
			pygame.display.update()
			pygame.time.delay(50)
            
	return False

# Display instruction for the game
def instruction():
    text = TEXT.render ("INSTRUCTIONS:",True,MAROON)
    text1 = TEXT.render("FOR GETTING BACK TO THE DEFAULT PRESS D", True, MAROON)
    text2 = TEXT.render("FOR VISUALIZE PRESS ENTER", True, MAROON)
    text3 = RIGHTS.render("Copyright©2022 Fairooz Nahiyan|All Rights Reserved", True, (60, 42, 33))
    WINDOW.blit(text, (10, 560))
    WINDOW.blit(text1, (90, 580))
    WINDOW.blit(text2, (90, 600))
    WINDOW.blit(text3, (100, 625))
    
#Timer--------------------------------->
"""
def getTime(milisec):
    decsec = (milisec % 1000) // 100
    sec = (milisec // 1000) % 60
    mint = (milisec // 1000 // 60) % 60
    time = str(mint) + ":" + str(sec) + ":" + str(decsec)
    return time

def time(): #------------------------------------->
    timerText = TIME_FONT.render("Timer: " + getTime(FPS),True , MULBERRY)
    timerRect = timerText.get_rect()
    timerRect.center = (400,530)
    WINDOW.blit(timerText,timerRect) 
"""  
# Timer event
TIMER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT, 100)

# Display options when solved
def result():
	text1 = NUMB_FONT.render("GAME OVER!!", True, MAROON)
	WINDOW.blit(text1, (WIDTH//2, HEIGHT//2))
run = True
f1 = 0
f2 = 0
rs = 0
error = 0
# The loop thats keep the window running
game_opening()
while run:
    
    WINDOW.fill(BEIGE)
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False    
        #timer------------------>
        if event.type == pygame.MOUSEBUTTONDOWN:
                time_x, time_y = event.pos
                if 200 <= time_x <= 300 and 520 <= time_y <= 560:
                    if not running:
                        running = True
                        start_time = pygame.time.get_ticks()
                        game_over = False
                    else:
                        running = False
                        countdown = (
                            COUNTDOWN_MINUTES * 60 * 1000
                            + COUNTDOWN_SECONDS * 1000
                            + COUNTDOWN_MILLISECONDS
                        )
                        
        elif event.type == TIMER_EVENT and running:
                elapsed_time = pygame.time.get_ticks() - start_time
                countdown = (
                    COUNTDOWN_MINUTES * 60 * 1000
                    + COUNTDOWN_SECONDS * 1000
                    + COUNTDOWN_MILLISECONDS
                    - elapsed_time
                )
                if countdown <= 0:
                    countdown = 0
                    running = False
                    game_over = True
        #------------------------------> 
        if event.type == pygame.MOUSEBUTTONDOWN: # Get the mouse position to insert number
            f1 = 1
            pos = pygame.mouse.get_pos()
            if 0 <= time_x <= 504 and 0 <= time_y <= 504:
                get_cord(pos)
                     
        if event.type == pygame.KEYDOWN:  # Get the number to be inserted if key pressed
            if event.key == pygame.K_LEFT:
                x -= 1
                f1 = 1
            if event.key == pygame.K_RIGHT:
                x +=1
                f1 = 1
            if event.key == pygame.K_UP:
                y-= 1
                f1 = 1
            if event.key == pygame.K_DOWN:
                y+= 1
                f1 = 1
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9
            if event.key == pygame.K_RETURN:
                f2 = 1
            if event.key == pygame.K_r: # If R pressed clear the sudoku board
                rs = 0
                error = 0
                f2 = 0
                grid =[
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0]
				]
            if event.key == pygame.K_d:  # If D is pressed reset the board to default
                rs = 0
                error = 0
                f2 = 0
                grid =[
					[7, 8, 0, 4, 0, 0, 1, 2, 0],
					[6, 0, 0, 0, 7, 5, 0, 0, 9],
					[0, 0, 0, 6, 0, 1, 0, 7, 8],
					[0, 0, 7, 0, 4, 0, 2, 6, 0],
					[0, 0, 1, 0, 5, 0, 9, 3, 0],
					[9, 0, 4, 0, 6, 0, 0, 0, 5],
					[0, 7, 0, 3, 0, 0, 0, 1, 2],
					[1, 2, 0, 0, 0, 7, 4, 0, 0],
					[0, 4, 9, 2, 0, 6, 0, 0, 7]
				]
    
    # Calculate minutes, seconds, and milliseconds
    minutes = countdown // (60 * 1000)
    seconds = (countdown // 1000) % 60
    milliseconds = countdown % 1000
    
    # Draw the countdown text in the "minute : seconds : milliseconds" format
    countdown_text = f"Timer: {minutes:02}:{seconds:02}:{milliseconds:03}"
    text = TIME_FONT.render(countdown_text, True, MAROON)
    text_rect = text.get_rect(center=(400, 545))
    WINDOW.blit(text, text_rect)
    
     # Draw the start/stop button
    button_text = "Start" if not running else "Stop"
    button = TIME_FONT.render(button_text, True, CREAM)
    button_rect = button.get_rect(center=(WIDTH // 2, 545))
    pygame.draw.rect(WINDOW, MAROON, (200, 520, 100, 40))
    #pygame.draw.rect(WINDOW, (255,0,0), (0, 0, 504, 504), 10)
    WINDOW.blit(button, button_rect)
    
    if game_over:
            game_over_text = TIME_FONT.render("Game Over", True, (255, 0, 0))
            game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, 260))
            WINDOW.blit(game_over_text, game_over_rect)

    
    
    if f2 == 1:
        if solve(grid,0,0) == False:
            error = 1
        else:
            rs = 1
        f2 = 0
    if val != 0:
        draw_val(val)
        if valid(grid,int(x), int(y), val) == True:
            grid[int(x)][int(y)] = val
            f1 = 0
        else:
            grid[int(x)][int(y)] = 0
            raise_error2()
        val = 0
    if error == 1:
        raise_error1()
    if rs == 1 :
        result()
    draw()
    if f1 == 1:
        draw_box()
        
    
    instruction()
    #time()
    pygame.display.update()
 	
	# Update window
	

# Quit pygame window
pygame.quit()	
	
