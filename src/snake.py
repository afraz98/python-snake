import pygame
from pygame.locals import *

import random

class Square(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width=25, height=25, color=(0, 200, 255)):
        super(Square, self).__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.width = width
        self.height = height
        self.surface = pygame.Surface((width, height))

        self.surface.fill(color)
        self.rect = self.surface.get_rect()

class Snake():
    def __init__(self):
        self.active = False
        self.digits = [[40, 40], [40, 50], [40, 60], [40,70]]

        self.max_width = 800
        self.max_height = 600

        pygame.init()
        self.screen = pygame.display.set_mode((self.max_width, self.max_height))
        self.active = True

        self.pos_x = 100
        self.pos_y = 50

        self.dy = 0
        self.dx = 10

        self.spawn_food()

    def add_digit(self, x, y):
        self.digits.append([x, y])
    
    def spawn_food(self):
        self.food_x = random.randrange(1, self.max_width//10) * 10
        self.food_y = random.randrange(1, self.max_height//10) * 10

    def check_collision(self):
        return pygame.Rect.colliderect(self.digits[0].rect, self.food.rect)

    def game_over(self):
        print("GAME OVER")
        self.active = False
        self.digits = []
        pass

    def loop(self):
        self.spawn_food()
        self.clock = pygame.time.Clock()
        while self.active:
            
            # self.clock.tick(15)
            # Process events
            for event in pygame.event.get():
                # A key has been pressed
                if event.type == KEYDOWN:
                    if event.key == K_UP and self.dy != 10:
                        self.dy = -10
                        self.dx = 0

                    if event.key == K_DOWN and self.dy != -10:
                        self.dy = 10
                        self.dx = 0

                    if event.key == K_LEFT and self.dx != 10:
                        self.dx = -10
                        self.dy = 0

                    if event.key == K_RIGHT and self.dx != -10:
                        self.dx = 10
                        self.dy = 0

                    if event.key == K_BACKSPACE:
                        self.active = False
            
            # Update positions of all digits
            
            self.pos_x += self.dx
            self.pos_y += self.dy

            self.digits.insert(0, [self.pos_x, self.pos_y])
            # TODO: Find a better way to do collision
            if self.food_x == self.digits[0][0] and self.digits[0][1] == self.food_y:
                self.spawn_food()
            else:
                # Cycle through list of positions
                self.digits.pop()

            self.screen.fill((0,0,0))

            # Render snake
            for digit in self.digits:
                pygame.draw.rect(self.screen, (255, 0, 0), (digit[0], digit[1], 10, 10))
            
            # Render fruit
            pygame.draw.rect(self.screen, (255, 255, 0), (self.food_x, self.food_y, 10, 10))

            for digit in self.digits[1:]:
                if self.pos_x == digit[0] and self.pos_y == digit[1]:
                    self.game_over()

            if self.pos_x >= self.max_width or self.pos_y >= self.max_height or self.pos_x < 0 or self.pos_y < 0:
                self.game_over()

            # Update display
            pygame.display.update()

            self.clock.tick(10)

snake = Snake()
snake.loop()