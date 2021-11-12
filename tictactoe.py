import pygame, sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
SPACE = 15

#rgb
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE BY FANG STÅLMARCK')
screen.fill( BG_COLOR )

#board
board = np.zeros((BOARD_ROWS, BOARD_COLS))

def draw_lines():
  # draw 2 lines horizontally, vertically
  pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
  pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

  pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
  pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

def draw_figures():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 1:
				pygame.draw.circle( screen, CIRCLE_COLOR, (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
			elif board[row][col] == 2:
				pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH )	
				pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH )
 
def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False

    return True

def control_win(player):
    for col in range(BOARD_COLS): 
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_line(col, player)
            return True

    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_line(row, player)
            return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
            draw_ascending_diagnal(player)
            return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            draw_descending_diagnal(player)
            return True

    return False

def draw_vertical_line(col, player):
    positionX = col * 200 - 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line( screen, color, (positionX, 15), (positionX, HEIGHT -15), 15 )

def draw_horizontal_line(row, player):
    positionY = row * 200 - 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line( screen, color, (15, positionY), (WIDTH -15, positionY), 15)

def draw_ascending_diagnal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line( screen, color, (15, HEIGHT -15), (WIDTH -15, 15), 15)

def draw_descending_diagnal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line( screen, color, (15, 15), (WIDTH -15, HEIGHT -15), 15)

def restart():
    screen.fill( BG_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


draw_lines()

player = 1
game_over = False

# mainloop for the screen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]
            mouseY = event.pos[1]
            
            clicked_row = mouseY // 200
            clicked_col = mouseX // 200
            print(mouseX,mouseY)
     
            if available_square(clicked_row,clicked_col):
                if player == 1:
                    mark_square(clicked_row,clicked_col, 1)
                    if control_win(player):
                        game_over = True
                    player = 2

                elif player == 2:
                    mark_square(clicked_row,clicked_col, 2)
                    if control_win(player):
                        game_over = True
                    player = 1

                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
        


         
    pygame.display.update()