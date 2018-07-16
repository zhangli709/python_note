import pygame
from abc import ABCMeta,abstractmethod
from random import randint


BLACK_COLOR = (0, 0, 0)
FOOD_COLOR = (226, 115, 185)
GREEN_COLOR = (0, 255, 0)

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class GameObject(object, metaclass=ABCMeta):

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

    @abstractmethod
    def draw(self, screen):
        pass


class SnakeNode(GameObject):

    def __init__(self, x, y, size, color=GREEN_COLOR):
        super(SnakeNode, self).__init__(x, y, color)
        self._size = size

    @property
    def size(self):
        return self._size

    def draw(self, screen):
        pygame.draw.rect(screen, self._color, [self._x, self._y, self._size, self._size], 0)
        pygame.draw.rect(screen, BLACK_COLOR, [self._x, self._y, self._size, self._size], 1)


class Snake(GameObject):

    def __init__(self):
        super(Snake, self).__init__()
        self._dir = LEFT
        self._nodes = []
        self._alive = True
        for index in range(5):
            node = SnakeNode(290 + 20 * index, 250, 20)
            self._nodes.append(node)

    @property
    def dir(self):
        return self._dir

    @property
    def head(self):
        return self._nodes[0]

    @property
    def alive(self):
        return self._alive

    def draw(self, screen):
        """调用了蛇节点中的画方法"""
        for node in self._nodes:
            node.draw(screen)

    def change_dir(self, new_dir):
        if (self._dir + new_dir) % 2 != 0:
            self._dir = new_dir

    def move(self):
        snake_dir = self._dir
        x, y, size = self.head.x, self.head.y, self.head.size
        if snake_dir == UP:
            y -= size
        elif snake_dir == DOWN:
            y += size
        elif snake_dir == RIGHT:
            x += size
        elif snake_dir == LEFT:
            x -= size
        new_head = SnakeNode(x, y, size)
        self._nodes.insert(0, new_head)
        self._nodes.pop()

    def eat_food(self, food):
        if self.head.x == food.x and self.head.y == food.y:
            tail = self._nodes[-1]
            self._nodes.append(tail)
            return True
        return False

    def eat_me(self):
        new_nodes = self._nodes[1:]
        for node in new_nodes:
            if node.x == self._nodes[0].x and node.y == self._nodes[0].y:
                self._alive = False

    def collide(self, wall):
        head = self.head
        if head.x < wall.x or head.y < wall.y or (head.x + head.size) > (wall.x + wall.width) \
                or (head.y + head.size) > wall.y + wall.height:
            self._alive = False


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
        pygame.draw.rect(screen, BLACK_COLOR, [self._x, self._y, self._width,  self._height], 5)


class Food(GameObject):

    def __init__(self, x, y, size, color=FOOD_COLOR):
        super(Food, self).__init__(x, y, color)
        self._size = size

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def draw(self, screen):
        pygame.draw.circle(screen, self._color,
                           [self._x + self._size // 2, self._y + self._size // 2], self._size // 2, 0)


def main():
    def hand_key_event(key_event):
        """按键事件"""
        key = key_event.key
        if key == pygame.K_F2:
            reset_game()
        new_dir = LEFT
        if key == pygame.K_w:
            new_dir = UP
        elif key == pygame.K_d:
            new_dir = RIGHT
        elif key == pygame.K_s:
            new_dir = DOWN
        elif key == pygame.K_a:
            new_dir = LEFT
        if new_dir != snake.dir:
            snake.change_dir(new_dir)

    def refresh():
        """刷新"""
        screen.fill([242, 242, 242])
        wall.draw(screen)
        food.draw(screen)
        snake.draw(screen)
        pygame.display.flip()

    def create_food():
        row = randint(0, 29)
        col = randint(0, 29)
        return Food(10 + 20 * row, 10 + 20 * col, 20)

    def reset_game():
        nonlocal food, snake
        food = create_food()
        snake = Snake()

    pygame.init()
    wall = Wall(10, 10, 600, 600)
    food = Food(290, 290, 20)
    snake = Snake()
    screen = pygame.display.set_mode([620, 620])
    screen.fill([242, 242, 242])
    pygame.display.set_caption('贪吃蛇')
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                hand_key_event(event)
        if snake.alive:
            refresh()
            clock.tick(5)
        if snake.alive:
            snake.move()
            snake.collide(wall)
            snake.eat_me()
            if snake.eat_food(food):
                food = create_food()
    pygame.quit()


if __name__ == '__main__':
    main()