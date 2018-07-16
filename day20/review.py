import pygame
from random import randint
from abc import ABCMeta, abstractmethod

BLACK_COLOR = (0, 0, 0)
FOOD_COLOR = (236, 111, 187)
GREEN_COLOR = (0, 255, 0)

UP = 0
RIGHT = 1s
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

    @property
    def color(self):
        return self._color

    @abstractmethod  # 后面继承的子类都必须重写此方法，不然报错
    def draw(self, screen):
        pass


class SnakeNode(GameObject):  # 蛇节

    def __init__(self, x, y, size, color=GREEN_COLOR):
        """
        x y 为坐标，size为宽高。
        :param x:
        :param y:
        :param size:
        :param color:
        """
        super(SnakeNode, self).__init__(x, y, color)
        self._size = size

    @property
    def size(self):
        return self._size

    def draw(self, screen):
        """
        画蛇的节点，其中，位置，由左上的位置坐标和宽高组成。0，表示实心。
        :param screen:
        :return:
        """
        pygame.draw.rect(screen, self._color, [self._x, self._y, self._size, self._size], 0)
        pygame.draw.rect(screen, BLACK_COLOR, [self._x, self._y, self._size, self._size], 1)


class Snake(GameObject):

    def __init__(self):
        """由蛇节组成🐍"""
        super(Snake, self).__init__()
        self._dir = LEFT
        self._nodes = []
        self._alive = True
        for index in range(5):
            node = SnakeNode(290 + index * 20, 250, 20)
            self._nodes.append(node)

    @property
    def head(self):
        return self._nodes[0]

    @property
    def dir(self):
        return self._dir

    @property
    def alive(self):
        return self._alive

    def collide(self, wall):
        """撞到墙返回真，否则返回False"""
        head = self.head
        if head.x < wall.x or head.x + head.size > wall.x + wall.width\
            or head.y < wall.y or head.y + head.size > wall.y + wall.height:
            self._alive = False

    def eat_food(self, food):
        if self.head.x == food.x and self.head.y == food.y:
            tail = self._nodes[-1]
            self._nodes.append(tail)
            return True
        return False

    def draw(self, screen):
        for node in self._nodes:
            node.draw(screen)

    def move(self):
        if self._alive:
            snake_dir = self._dir
            x, y, size = self.head.x, self.head.y, self.head.size
            if snake_dir == UP:
                y -= size
            elif snake_dir == RIGHT:
                x += size
            elif snake_dir == DOWN:
                y += size
            else:
                x -= size
            new_head = SnakeNode(x, y, size)
            self._nodes.insert(0, new_head)
            self._nodes.pop()

    def change_dir(self, new_dir):
        if (self._dir + new_dir) % 2 != 0:
            self._dir = new_dir


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
        pygame.draw.rect(screen, self._color, [self._x, self._y, self._width, self._height], 5)


class Food(GameObject):

    def __init__(self, x, y, size, color=FOOD_COLOR):
        super(Food, self).__init__(x, y, color)
        self._size = size
        self._hidden = False

    def draw(self, screen):
        """让食物闪烁起来"""
        if not self._hidden:
            pygame.draw.circle(screen, self._color,
                               (self._x + self._size // 2, self._y + self._size // 2),
                               self._size // 2, 0)
        self._hidden = not self._hidden


def main():
    def refresh():
        """刷新游戏窗口"""
        screen.fill([242, 242, 242])
        snake.draw(screen)
        wall.draw(screen)
        food.draw(screen)
        pygame.display.flip()

    def handle_key_event(key_event):
        """接受按键事件"""
        key = key_event.key
        if key == pygame.K_F2:
            reset_game()
        else:
            if snake.alive:
                new_dir = snake.dir
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

    def create_food():
        row = randint(0, 29)
        col = randint(0, 29)
        return Food(10 + 20 * row, 10 + 20 * col, 20)

    def reset_game():
        nonlocal food, snake
        food = create_food()
        snake = Snake()

    wall = Wall(10, 10, 600, 600)
    food = create_food()
    snake = Snake()
    pygame.init()
    pygame.display.set_caption('贪吃蛇')
    screen = pygame.display.set_mode([620, 620])  # 左上角是坐标原点。
    screen.fill([242, 242, 242])
    pygame.display.flip()
    clock = pygame.time.Clock()  # 帧数，游戏每秒的刷新次数。帧数越高越好，但是要机器能跟上。
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                handle_key_event(event)  # 调用按键函数
        if snake.alive:
            refresh()  # 调用刷新函数
        clock.tick(10)  # 刷新次数
        if snake.alive:
            snake.move()
            snake.collide(wall)
            if snake.eat_food(food):
                food = create_food()
    pygame.quit()


if __name__ == '__main__':
    main()


