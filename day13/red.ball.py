from random import randint
import pygame


class Ball(object):

    def __init__(self, center, color, radius, sx, sy):
        self._center = center
        self._color = color
        self._radius = radius
        self._sx = sx
        self._sy = sy

    @property
    def center(self):
        return self._center

    @property
    def radius(self):
        return self._radius

    def move(self):
        """移动后的坐标"""
        x, y = self._center[0], self._center[1]
        x += self._sx
        y += self._sy
        self._center = (x, y)
        if (x + self._radius >= 800 and self._sx > 0) or (x - self._radius <= 0 and self._sx < 0):
            self._sx = -self._sx
        if (y + self._radius >= 600 and self._sy > 0) or (y - self._radius <= 0 and self._sy < 0):
            self._sy = - self._sy

    def eat(self, other):
        pass

    def draw(self, screen):
        """画一个圆"""
        pygame.draw.circle(screen, self._color, self._center,
                           self._radius, 0)


def refresh(screen, balls):
    bg_color = (242, 242, 242)
    screen.fill(bg_color)
    for ball in balls:
        ball.draw(screen)
    pygame.display.flip()


def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return red, green, blue


def main():
    pygame.init()
    balls = []
    screen = pygame.display.set_mode([800, 600])  # 窗口大小
    pygame.display.set_caption('大球吃小球')  # 标题
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and \
                    event.button == 1:
                # = event.pos
                color = random_color()
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                ball = Ball(event.pos, color, radius, sx, sy)
                balls.append(ball)
        refresh(screen, balls)
        clock.tick(20)
        for ball in balls:
            ball.move()
    pygame.quit()


if __name__ == '__main__':
    main()