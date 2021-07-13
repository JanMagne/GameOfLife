"""
Python 3.9.6 implementation of Conway's Game of Life, using Pygame to display.

The rules of GoL are as follow
	1. Any live cell with two or three live neighbours survives.
	2. Any dead cell with three live neighbours becomes a live cell.
	3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.
"""



import pygame, random




width = 1000
height = 1000
resolution = (width, height)

black = (0,0,0)
white =	(255,255,255)

block_size = 20
num_blocks_x = width//block_size
num_blocks_y = height//block_size





def initialize_pygame_and_screen():
	pygame.init()
	#pygame.display.set_icon(pygame.image.load("logo.png"))
	global screen 
	screen = pygame.display.set_mode(size=resolution)
	pygame.display.set_caption("Game of Life")
	
	if pygame.display.get_init():
		print("Pygame display initialized OK")


def countNeighbors(i, j, matrix):
	total = 0

	# edges
	if i == 0 or i == num_blocks_x-1 or j == 0 or j == num_blocks_y-1 :
		return 2 #with 2 neighbors the cell is left as is
	else:
		for x in range(-1,2):
			for y in range(-1,2):
				if (x == 0 and y == 0):
					continue
				if matrix[i+x][j+y] == 1:
					total = total + 1

	return total



def updateMatrix(matrix):
	new = createMatrix(num_blocks_x, num_blocks_y)
	old = matrix.copy()

	for i in range(num_blocks_x):
		for j in range(num_blocks_y):			
			numNeighbors = countNeighbors(i , j, old)
			
			if numNeighbors == 3:
				new[i][j] = 1
			
			elif matrix[i][j] == 1 and numNeighbors == 2:
				new[i][j] = 1
			
			else:
				new[i][j] = 0

	return new



def drawMatrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			x = i*block_size
			y = j*block_size
			if matrix[i][j]:
				pygame.draw.polygon(screen, black, [(x,y),(x+block_size, y),(x+block_size, y+block_size),(x, y+block_size)])
			else:
				pygame.draw.polygon(screen, white, [(x,y),(x+block_size, y),(x+block_size, y+block_size),(x, y+block_size)])


def createMatrix(x, y, live=0):
	""" Create a matrix of cells all set to 0 """
	
	matrix = [[0]*num_blocks_x for i in range(num_blocks_y)]
	for i in range(num_blocks_x):
		for j in range(num_blocks_y):
			if i == 0 or j == 0 or i == num_blocks_x-1 or j == num_blocks_y-1:
				matrix[i][j] = 0
			elif live == 0:
				matrix[i][j] = 0
			elif random.randint(0,100) < live:
				matrix[i][j] = 1
			else:
				matrix[i][j] = 0

	return matrix



def mouseAction(cells):
	tmp = pygame.mouse.get_pressed()
	isPressedLeft = tmp[0]
	isPressedRight = tmp[2]
	
	x, y = pygame.mouse.get_pos()
	i = x//block_size
	j = y//block_size
	
	if isPressedLeft:
		cells[i][j] = 1
	if isPressedRight:
		cells[i][j] = 0

	return cells

def main():
	initialize_pygame_and_screen()
	clock = pygame.time.Clock()
	cells = createMatrix(num_blocks_x, num_blocks_y)


	while 1:
		if pygame.key.get_pressed()[pygame.K_RIGHT]:
			pygame.time.wait(200)
			cells = updateMatrix(cells)
		
		screen.fill(white)
		cells = mouseAction(cells)
		drawMatrix(cells)


			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			

		pygame.display.flip()

	print("Mainloop done, quitting now")
	quit()


if __name__ == '__main__':
	main()