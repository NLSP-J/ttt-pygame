import pygame as pg
import time
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

b_width = 400
b_height = 400
board = [['','',''],
		 ['','',''],
		 ['','','']]

x_img = pg.image.load("./assets/images/X_modified.png")
o_img = pg.image.load("./assets/images/o_modified.png")

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

game_window()
async def main():
	
	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				running = False

		pg.display.flip()
		await asyncio.sleep(0)
		
asyncio.run(main())

