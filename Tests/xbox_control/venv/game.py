from controller import Controller
import pygame

pygame.init()
pygame.joystick.init()
mac_controller = Controller()

WHITE = (255, 255, 255)
RED = (255, 0, 0)



screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Xbox360 Test')

clock = pygame.time.Clock()

done = False


circle_pos = [400.0, 300.0]
integer_pos = [400, 300]
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        #print(event)

    screen.fill(WHITE)

    left_pos = mac_controller.get_left_stick()
    right_pos = mac_controller.get_right_stick()

    circle_pos[0] = circle_pos[0] + left_pos[0] * 15
    circle_pos[1] = circle_pos[1] + left_pos[1] * 15
    integer_pos[0] = int(circle_pos[0])
    integer_pos[1] = int(circle_pos[1])
    pygame.draw.circle(screen, RED, integer_pos, 20, 0)

    print(left_pos)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()