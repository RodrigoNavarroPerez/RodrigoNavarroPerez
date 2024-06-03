import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame

pygame


player_rect = pygame.Rect(100, 100, 50, 50)
player_speed_y = 0


def reset_player_position():
	player_rect.y = 100  


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN
            if event.button == 1:
            	reset_player_position()
            	player_speed_y = 0


    player_speed_y += 0.5
    player_rect.y += player_speed_y


    if player_rect.bottom > screen_height:
    	player_rect.bottom = screen_height


    	screen.fill((0, 0, 0))
    	pygame.draw.rect(screen, (255, 255, 0), player_rect)
    	pygame.display.flip()

    	pygame.time.Clock().tick(60)
