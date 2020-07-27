import pygame
from random import randrange

from BG import Background

class QuadUI:
    def run():
        #initialize pygame
        pygame.init()

        #initialize background
        BackGround = Background('Assets/flight.jpg', [0,0])
        white = (255,255,255)

        #window initialization
        (width, height) = (1280, 720)
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('rpi-quad')
        screen.fill(white)
        pygame.display.flip()

        #program loop
        running = True
        while running:
            #load BG
            screen.blit(BackGround.image, BackGround.rect)

            #widgets
            font = pygame.font.Font('Assets/Anonymous_Pro.ttf', 18)
            data = (randrange(360), randrange(360), randrange(360))
            text = font.render(str(data), True, white)
            textRect = text.get_rect()
            textRect.center = (width/12, height/22)
            screen.blit(text, textRect)
            pygame.draw.line(screen, white, (width/2, height/2-50), (width/2, height/2+50), 5)
            pygame.draw.line(screen, white, (width/2-50, height/2), (width/2+50, height/2), 5)

            #check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            #keyboard
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                print(('Forward', 5))
            if keys[pygame.K_a]:
                print(('Left', 5))
            if keys[pygame.K_s]:
                print(('Back', 5))
            if keys[pygame.K_d]:
                print(('Right', 5))
            if keys[pygame.K_SPACE]:
                print(('Up', 5))
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                print(('Down', 5))
            
            #update display
            pygame.display.update()

QuadUI.run()
