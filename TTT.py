# import sys module
import pygame
import sys
import asyncio
  
  
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 500])
base_font = pygame.font.Font(None, 32)
input_rect = pygame.Rect(20, 20, 140, 32)
color_active = pygame.Color('darkblue')
color_passive = pygame.Color('chartreuse4')
color = color_passive
  

def get_keys(event, user_text):
    if event.type == pygame.KEYDOWN:
        print(event.key)
        # Check for backspace
        if event.key == pygame.K_BACKSPACE:
            # get text input from 0 to -1 i.e. end.
            user_text = user_text[:-2] + "|"
        elif event.key == pygame.K_RETURN:
            user_text = "" + "|"
        else:
            user_text = user_text[:-1]
            user_text += event.unicode + "|"
    return event, user_text

def entry(color, user_text):
    pygame.draw.rect(screen, color, input_rect)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(100, text_surface.get_width()+10)


async def main():
    user_text = ''
    active = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    if active == False:
                        user_text = user_text + "|"
                    active = True
                else:
                    active = False
                    user_text = user_text[:-1]
            if active:
                event, user_text = get_keys(event, user_text)
        screen.fill((255, 255, 255))
        if active:
            color = color_active
        else:
            color = color_passive
        entry(color, user_text)
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)

asyncio.run(main())
