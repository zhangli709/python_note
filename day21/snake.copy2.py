import pygame
from abc import ABCMeta,abstractmethod

BLACK_COLOR = [0, 0, 0]
FOOD_COLOR = [188, 155, 155]
GREEN_COLOR = [0, 255, 255]

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class Gameobject(object, metaclass=ABCMeta):

    def __init__(self, x=0, y=0, color=BLACK_COLOR):
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

    @abstractmethod
    def draw(self, screen):
        pass


class Wall(Gameobject):

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
        pygame.draw.rect(screen,BLACK_COLOR, [self._x, self._y, self._width, self._height], 5)


class Food(Gameobject):

    def __init__(self, x, y, size, color=FOOD_COLOR):
        super(Food, self).__init__(x, y, color)
        self._size = size

    @property
    def size(self):
        return self._size

    def draw(self, screen):
        pygame.draw.circle(screen, FOOD_COLOR, [self._x + self._size // 2, self._y + self._size // 2], self._size // 2, 0)


class SnakeNode(Gameobject):

    def __init__(self, x, y, size, color=GREEN_COLOR):
        super(SnakeNode, self).__init__(x, y, color)
        self._size = size

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN_COLOR, [self._x, self._y, self._size, self._size], 0)
        pygame.draw.rect(screen, BLACK_COLOR, [self._x, self._y, self._size, self._size], 1)


class Snake(Gameobject):

    def __init__(self):
        super(Snake, self).__init__()

        self._nodes = []
        self._dir = LEFT
        self._alive = True
        for index in range(5):
            node = SnakeNode(190 + 20 * index, 250, 20)
            self._nodes.append(node)
    @property
    def dir(self):
        return self._dir

    @property
    def nodes(self):
        return self._nodes

    @property
    def alive(self):
        return self._alive

    @property
    def head(self):
        return self._nodes[0]

    def draw(self, screen):
        for index, node in enumerate(self._nodes):
            node.draw(screen)

    def move(self):
        if self._alive:
            snake_dir = self._dir
            x, y, size = self.






def main():
    pygame.init()
    pygame.display.set_caption('贪吃蛇')
    screen = pygame.display.set_mode([620, 620])
    screen.fill([242, 242, 242])
    wall = Wall(10, 10, 600, 600)
    wall.draw(screen)
    food = Food(110, 250, 20)
    food.draw(screen)
    snake = Snake()
    snake.draw(screen)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()


if __name__ == '__main__':
    main()