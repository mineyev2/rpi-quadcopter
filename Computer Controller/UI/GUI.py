import pygame
from random import randrange
from random import uniform

from BG import Background

class QuadUI:
    #constructor
    def __init__(self):
        self.white = (255,255,255)
        self.live = 'Assets/flight.jpg'
        self.title = 'rpi-quad'
        self.angles = (0, 0, 0)
        self.motors = (0, 0, 0, 0)
        self.battery = 1

        #window initialization
        (self.width, self.height) = (1280, 720)
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.screen.fill(self.white)
        pygame.display.flip()

    #setters
    def setAngles(x, y, z):
        self.angles = (x, y, z)
        
    def setMotors(m1, m2, m3, m4):
        self.motors = (m1, m2, m3, m4)

    #widget displays
    def display_data(self, angles, motors):
        #use font
        font = pygame.font.Font('Assets/Anonymous_Pro.ttf', 18)

        #display data
        text_angles = font.render('Angles: ' + str(angles), True, self.white)
        text_motors = font.render('Motors: ' + str(motors), True, self.white)
        self.screen.blit(text_angles, (self.width/40, 20*self.height/22))
        self.screen.blit(text_motors, (self.width/40, 21*self.height/22))

    def display_crosshairs(self):
        pygame.draw.line(self.screen, self.white, (self.width/2, self.height/2-50), (self.width/2, self.height/2+50), 5)
        pygame.draw.line(self.screen, self.white, (self.width/2-50, self.height/2), (self.width/2+50, self.height/2), 5)

    def display_battery(self, battery):
        current_color = (255*(1-battery), 255*battery, 0)

        #draw white rectangle
        w = 110
        h = 30
        out = pygame.Rect((7*self.width/8, self.height/22), (w, h))
        pygame.draw.rect(self.screen, self.white, out)
        
        #draw battery rectangle
        center = pygame.Rect((7*self.width/8+5+(1-battery)*(w-10), self.height/22+5), (battery*(w-10), h-10))
        pygame.draw.rect(self.screen, current_color, center)
    
    #main running method
    def run(self):
        #initialize pygame
        pygame.init()

        #initialize background
        BackGround = Background(self.live, [0,0])

        #program loop
        running = True
        while running:
            #load BG
            self.screen.blit(BackGround.image, BackGround.rect)

            #widgets
            self.angles = (randrange(360), randrange(360), randrange(360))
            self.motors = (uniform(0, 1), uniform(0, 1), uniform(0, 1))
            self.battery = self.battery - uniform(0, 0.1)
            if self.battery < 0:
                self.battery = 1

            #display widgets
            self.display_data(self.angles, self.motors)
            self.display_crosshairs()
            self.display_battery(self.battery)

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

q = QuadUI()
q.run()
