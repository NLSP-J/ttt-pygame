import pygame as pg
import asyncio

pg.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

win_width = 400
win_height = 500
screen = pg.display.set_mode([win_width, win_height])
pg.display.set_caption('Tic-Tac-Toe')

font = pg.font.Font(None, 30)

player = 'x'
moves = 0
draw = False
winner = False
running = True

b_width = 400
b_height = 400
board = [['','',''],
	 ['','',''],
	 ['','','']]

x_img = pg.image.load("X_modified.png")
o_img = pg.image.load("o_modified.png")

x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(o_img, (80, 80))


def update_text():
	global draw, player
	if draw:
		text = "It's a draw!"
	elif winner != False:
		text = f"{winner} wins!"
	else:
		text = f"{player}'s turn"

	screen.fill(black, (0, 400, 500, 100))
	text = font.render(text, True, white)
	text_rect = text.get_rect(center=(b_width / 2, win_height-50))
	screen.blit(text, text_rect)	

def game_window():

	screen.fill(white)

	# drawing vertical lines
	pg.draw.line(screen, black, (b_width / 3, 0),
				(b_width / 3, b_height), 7)
	pg.draw.line(screen, black, (b_width / 3 * 2, 0),
				(b_width / 3 * 2, b_height), 7)

	# drawing horizontal lines
	pg.draw.line(screen, black, (0, b_height / 3),
				(b_width, b_height / 3), 7)
	pg.draw.line(screen, black, (0, b_height / 3 * 2),
				(b_width, b_height / 3 * 2), 7)
	
	update_text()


def check_win():
	global draw, winner

	# checking for winning rows
	for row in range(3):
		if((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] != '')):
			winner = board[row][0]
			pg.draw.line(screen, red,
						(0, (row + 1)*b_height / 3 - b_height / 6),
						(b_width, (row + 1)*b_height / 3 - b_height / 6),
						4)

	# checking for winning columns
	for col in range(3):
		if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] != '')):
			winner = board[0][col]
			pg.draw.line(screen, red, ((col + 1) * b_width / 3 - b_width / 6, 0),
						((col + 1) * b_width / 3 - b_width / 6, b_height), 4)

	# check for diagonal winners
	if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] != ''):
		winner = board[0][0]

		# game won diagonally left to right
		pg.draw.line(screen, red, (50, 50), (350, 350), 4)

	if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] != ''):
		winner = board[0][2]

		# game won diagonally right to left
		pg.draw.line(screen, red, (350, 50), (50, 350), 4)

	if (winner == False and moves == 9):
		draw = True


def draw_img(row, col):
	global board, player

	if row == 1:
		posy = 30
	elif row == 2:
		posy = b_width / 3 + 30
	elif row == 3:
		posy = b_width / 3 * 2 + 30

	if col == 1:
		posx = 30
	elif col == 2:
		posx = b_height / 3 + 30
	elif col == 3:
		posx = b_height / 3 * 2 + 30

	board[row-1][col-1] = player

	if player == 'x':
		screen.blit(x_img, (posx, posy))
		player = 'o'

	else:
		screen.blit(o_img, (posx, posy))
		player = 'x'

	
def check_click():

	x, y = pg.mouse.get_pos()

	if (x < b_width / 3):
		col = 1
	elif (x < b_width / 3 * 2):
		col = 2
	elif (x < b_width):
		col = 3
	else:
		col = 'Invalid'

	if (y < b_height / 3):
		row = 1
	elif (y < b_height / 3 * 2):
		row = 2
	elif (y < b_height):
		row = 3
	else:
		row = 'Invalid'

	if(row != 'Invalid' and col != 'Invalid' and board[row-1][col-1] == ''):
		global moves
		moves += 1
		draw_img(row,col)

async def main():
    game_window()
    while running:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                check_click()
        if draw or winner != False:
            time.sleep(2)
            running = False

        check_win()
        update_text()

        pg.display.flip()
        await asyncio.sleep(0)
		
asyncio.run(main())

