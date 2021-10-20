import pygame
import math

run = True

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
dark_grey = (30, 30, 30)
black = (0, 0, 0)

width = 1000
height = 900


def length(v_1, v_2, distance_to_surface):
    value = 0
    for x in range(len(v_1)):
        value += math.pow(v_2[x] - v_1[x], 2)
    return math.sqrt(value) - distance_to_surface


def change_pos(pos, keys_pressed_var):
    speed = 3
    speed_count = 0
    if keys_pressed_var[pygame.K_w]:
        speed_count += 1
    if keys_pressed_var[pygame.K_a]:
        speed_count += 1
    if keys_pressed_var[pygame.K_s]:
        speed_count += 1
    if keys_pressed_var[pygame.K_d]:
        speed_count += 1

    if speed_count == 0:
        pass
    elif speed_count > 1:
        speed = speed / 2

    if keys_pressed_var[pygame.K_w]:
        pos = (pos[0], pos[1] - speed)
    if keys_pressed_var[pygame.K_a]:
        pos = (pos[0] - speed, pos[1])
    if keys_pressed_var[pygame.K_s]:
        pos = (pos[0], pos[1] + speed)
    if keys_pressed_var[pygame.K_d]:
        pos = (pos[0] + speed, pos[1])
    return pos


window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Boids")

player_coords = (0, 0)
circle_coords = (500, 450)
laser_point = (1000, 450)

player_width = 10
circle_width = 20

fps = 120
clock = pygame.time.Clock()

while run:
    for this_event in pygame.event.get():
        if this_event.type == pygame.QUIT:
            run = False

    clock.tick(fps)

    keys_pressed = pygame.key.get_pressed()
    player_coords = change_pos(player_coords, keys_pressed)

    window.fill(dark_grey)

    point = length(player_coords, circle_coords, circle_width)

    pygame.draw.circle(window, (60, 60, 60), player_coords, point)  # greyed out circle
    pygame.draw.circle(window, white, player_coords, point, 2)  # outline

    pygame.draw.circle(window, white, player_coords, player_width)  # center circle
    pygame.draw.circle(window, black, circle_coords, circle_width)  # circle object

    pygame.draw.line(window, (0, 255, 0), player_coords, laser_point)

    point2 = length(player_coords, laser_point, 0)
    # print(point2)

    pygame.draw.circle(window, white, (player_coords[0] + point, player_coords[1]), player_width)  # center circle
    # print(player_coords, circle_width, laser_point, (player_coords[0] + point, player_coords[1]))

    pygame.display.update()

pygame.quit()
