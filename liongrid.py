import pygame 
import time
import datetime
import threading

pygame.init()

# Global Constants

SCREEN_HEIGHT  =  600
SCREEN_WIDTH   =  1100
SCREEN         =  pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN_COLOR   =  (49, 150, 100)
LINE_COLOR     =  (255, 0, 0)


CROPPING_RATIO_VERT   =  0.9
CROPPING_RATIO_HOR    =  0.9
GRID_HEIGHT           =  int(CROPPING_RATIO_VERT * SCREEN_HEIGHT)
GRID_WIDTH            =  int(CROPPING_RATIO_HOR  * SCREEN_WIDTH) 
CELL_HEIGHT           =  50
CELL_WIDTH            =  60
  
pygame.display.set_caption("Lion Grid")

FRAME_DURATION = 1/2

class Grid():

	def __init__(self, pix_horiz, pix_vertic):
		self.pix_size_horizontal = pix_horiz
		self.pix_size_vertical   = pix_vertic

	def draw_grid(self):
		number_grids_hor   =  int(GRID_WIDTH / self.pix_size_horizontal) 
		shift_hor          =  (1 - CROPPING_RATIO_HOR) * SCREEN_WIDTH + (GRID_WIDTH - number_grids_hor * CELL_WIDTH)
		shift_hor          =  int(shift_hor / 2) #We evenly split the shift between the left and the right
		cord_line_vert     =  shift_hor # We split the (horizontal) width of the frame to get vertical lines. Hence the inverted hor and vert 

		number_grids_vert  =  int(GRID_HEIGHT / self.pix_size_vertical) 
		shift_vert         =  (1 - CROPPING_RATIO_VERT) * SCREEN_HEIGHT + (GRID_HEIGHT - number_grids_vert * CELL_HEIGHT)
		shift_vert         =  int(shift_vert / 2) #We evenly split the shift between the left and the right
		cord_line_hor      =  shift_vert # We split the (vertical) height of the frame to get horizontal lines. Hence the inverted hor and vert 

		while (cord_line_vert < shift_hor + GRID_WIDTH):
			pygame.draw.line(SCREEN,LINE_COLOR, (cord_line_vert, 0), (cord_line_vert, SCREEN_HEIGHT))
			cord_line_vert += self.pix_size_horizontal

		while (cord_line_hor < shift_vert + GRID_HEIGHT):
			pygame.draw.line(SCREEN,LINE_COLOR, (0, cord_line_hor), (SCREEN_WIDTH, cord_line_hor))
			cord_line_hor += self.pix_size_vertical



def main():
	gameOn = True

	while gameOn:
		t0 = datetime.datetime.now()

		current_time = t0.hour
		if 7 < current_time < 19:
	            SCREEN.fill((255, 255, 255))
		else:
	            SCREEN.fill((0, 0, 0))
		
		grid = Grid(CELL_WIDTH, CELL_HEIGHT)
		grid.draw_grid()

		t1                 =  datetime.datetime.now()
		compute_duration   =  (t1 - t0).total_seconds()

		if compute_duration > FRAME_DURATION:
			pygame.display.flip()
		else:
			time.sleep(FRAME_DURATION - compute_duration)

		pygame.display.flip()
main()