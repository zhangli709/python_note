import pygame
from threading import Thread


BLACK_COLOR = [0, 0, 0]
GREEN_COLOR = [0, 255, 0]


class GameObject(object):

    def __init__(self, x, y, color=BLACK_COLOR):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color


class Wall(GameObject):

    def __init__(self, x, y, width, height, color=BLACK_COLOR):
        super(Wall, self).__init__(x, y, color)
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN_COLOR, [self._x, self._y, self._width, self._height], 0)


class Car(GameObject):

    def __init__(self, x, y, size, color=BLACK_COLOR):
        super(Car, self).__init__(x, y, color)
        self._size = size

    @property
    def size(self):
        return self._size


    def draw(self, screen):
        pygame.draw.rect(screen, BLACK_COLOR, [self._x, self._y, self._size, self._size], 0)

    # def move(self, speed):
    #     self._x += speed
    #     self.draw(self,screen)


class Move(Thread):

    def __init__(self, x, y, size, speed):
        super(Move, self).__init__()
        self._speed = speed
        self._x = x
        self._y = y
        self._size = size

    def run(self):
        x, y, size = self._x, self._y, self._size
        x += self._speed
        new_car = Car(x, y, size)

def main():
    pygame.init()
    screen = pygame.display.set_mode([620, 620])
    pygame.display.set_caption('五车赛跑')
    screen.fill([242, 242, 242])
    wall = Wall(10, 10, 600, 600)
    wall.draw(screen)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()


if __name__ == '__main__':
    main()