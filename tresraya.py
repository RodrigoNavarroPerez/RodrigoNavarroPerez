import pygame
import sys
import  numpy as np 



class SpriteSheet:
	def __init__ (self, image):
	    self.sheet = image

	def get_image(self, frame, width, height, scale, colour):
		image = pygame.Surface((width, height), pygame.SCRALPHA)
		image.blit(self.sheet,(0,0), ((frame%3 * width),(frame//3*height),width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))
		image.set_colorkey(colour)

		return image



def board(b):
	for y in range(0,7):
		for x in range(0,7):
			if y == 0:
				screen.blit(frame_TX,(x*scale,y*scale))
		    else:
		    	if b[y-1][x]==0 : frame_TX=frame_TE
		    	if b[y-1][x]==1 : frame_TX=frame_TR
		    	if b[y-1][x]==-1 : frame_TX=frame_TA
				

def check_connect4(board):
	for row in board:
		for i in range(len(row) - 3):
			if row[1] == row[i + 1] == row[i + 2] == row[i + 3] != 0:
				return row[i]

	for col in range(len(board[0])):
		for i in range(len(board - 3))
			if board[i][col] == board[i + 1][col] == board[i + 2][col] == board[i + 3][col] != 0:
			  return board[i][col]

    for i in range(len(board) - 3):
    	for j in range(len(board[0]) - 3):
    		if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3]!= 0:
               return board[i][j]

    for i in range(len(board) - 3):
    	for j in range(3, len(board[0])):
    		if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3]!= 0:
    		   return board[i][j]
    
    if np.all(board != 0):
    	print("No hay jugadas")
    	return 3

    return 0




    def count_cells(b):
    	return len(b[:,n])- np.count_nonzero(b[:,n])



    def jugar(c,player):
    	empty_cell_count=count_cells(board_example)

        if empty_cell_count==0: return player

        My=0
        Mx=c*scale
        player_speed_y=0

        while My <empty_cell_count*scale:
        	player_speed_y += 0.3
        	My += player_speed_y
        	screen.fill((0,0,0))
        	screen.blit(frame_R if player==1 else frame_A ,(Mx,My))
        	board(board_example)
        	pygame.display.update()
        	pygame.time.Clock().tick(60)

        x=c
        y=empty_cell_count

        print(x,y)
        board_example[y-1][x]=player
        print(board_example)
        return -player	

   
pygame.init()
f_scale=0.5
scale=100 * f_scale
size = 7*scale, 7*scale
screen = pygame.display.set_mode(size)
sprite_sheet_image = pygame.image.load("./c4img/connect.svg").convert_alpha()
sprite_sheet=SpriteSheet(sprite_sheet_image)
frame_R = sprite_sheet.get_image(0,98,98,f_scale,(0,0,0))
frame_A = sprite_sheet.get_image(1,98,98,f_scale,(0,0,0))
frame_E = sprite_sheet.get_image(2,98,98,f_scale,(0,0,0))
frame_TR = sprite_sheet.get_image(3,100,100,f_scale,(0,0,0))
frame_TA = sprite_sheet.get_image(4,100,100,f_scale,(0,0,0))
frame_TE = sprite_sheet.get_image(5,100,100,f_scale,(0,0,0))
Mx=0
My=0
player=1
player_speed_y = 0
empty_cell_count=6
board_example = np.zero((6,7))
print(board_example)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		elif event.type == pygame.MOUSEMOTION:
			Mxx, _ = event.pos
			Mx=round(Mxx-scale//2)
			n=round(Mxx//scale)
	    elif event.type == pygame.MOUSEBUTTONDOWN:
	    	if event.button == 1:
	    		Mx=round((Mxx//scale)*scale)
	    		x=int(Mx//scale)
	    		player=jugar(x,player)
	    		resultado = check_connect4(board_example)
	    		if resultado == 1:
	    			print("¡El jugador 1 ha ganado")
	    		elif resultado == 1:
	    			print("¡El jugador 2 ha ganado!")
	    		elif resultado == 3:
	    			print("¡Empate!")
	    		else:
	    			print("No hay ganador todavía.")


	elif event.type == pygame.KEYDOWN:
		    if event.key == pygame.K_SPACE:
		    	Mx=Mxx
		    	n=round(Mxx//scale)
		    	My=0
		    	player_speed_y = 0
		    	gravity= False
		    	player=1
		    	board_example = np.zeros((6,7))
		    	empty_cell_count=count_cells(board_example)
 
    screen.fill((0,0,0))
    Mx = 0 if Mx < 0 else Mx
    Mx = 6*scale if Mx > 6*scale else Mx

    screen.blit(frame_R if player==1 else frame_A ,(Mx,My))
    board(board_example)

    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
