import pygame


def create_controls(drone):
    pygame.init()
    width, height = 400, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Drone controls")

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            drone.move_forward(100)
        if keys[pygame.K_s]:
            drone.move_back(100)
        if keys[pygame.K_a]:
            drone.move_left(50)
        if keys[pygame.K_d]:
            drone.move_right(50)
        if keys[pygame.K_UP]:
            drone.move_up(30)
        if keys[pygame.K_DOWN]:
            drone.move_down(30)
        if keys[pygame.K_LEFT]:
            drone.rotate_counter_clockwise(30)
        if keys[pygame.K_RIGHT]:
            drone.rotate_clockwise(30)
        if keys[pygame.K_q]:
            drone.land()
        if keys[pygame.K_e]:
            drone.takeoff()
        
        clock.tick(30)

    pygame.quit()
