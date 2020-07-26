import pygame

class QuadUI:
    def run():
        background_colour = (255,255,255)
        (width, height) = (300, 200)
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Tutorial 1')
        screen.fill(background_colour)
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                print(('Up', 5))
            if keys[pygame.K_a]:
                print(('Left', 5))
            if keys[pygame.K_d]:
                print(('Right', 5))
            if keys[pygame.K_s]:
                print(('Back', 5))
            if keys[pygame.K_SPACE]:
                print(('Up', 5))
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                print(('Down', 5))
                
