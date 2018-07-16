import pygame


class Ball(object):

    def __init__(self, center, color, radius, sx, sy):


def main():
    pygame.init()
    pygame.display.set_caption('球球大作战')
    pygame.display.set_mode([800, 600])
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == '__main__':
    main()