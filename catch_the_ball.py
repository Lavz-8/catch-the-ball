import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Paddle settings
paddle_width = 100
paddle_height = 20
paddle_speed = 10

# Ball settings
ball_radius = 10
ball_speed = 5

# Player settings
lives = 3
score = 0

# Paddle class
class Paddle:
    def __init__(self):
        self.x = (screen_width - paddle_width) // 2
        self.y = screen_height - paddle_height - 10
        self.width = paddle_width
        self.height = paddle_height
        self.speed = paddle_speed
        self.color = blue

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, dx):
        self.x += dx
        if self.x < 0:
            self.x = 0
        elif self.x > screen_width - self.width:
            self.x = screen_width - self.width

# Ball class
class Ball:
    def __init__(self):
        self.x = random.randint(ball_radius, screen_width - ball_radius)
        self.y = ball_radius
        self.radius = ball_radius
        self.speed = ball_speed
        self.color = red

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.y += self.speed

# Game loop
def game_loop():
    global lives, score

    clock = pygame.time.Clock()
    paddle = Paddle()
    balls = [Ball()]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move(-paddle_speed)
        if keys[pygame.K_RIGHT]:
            paddle.move(paddle_speed)

        screen.fill(black)

        paddle.draw()

        for ball in balls:
            ball.move()
            ball.draw()
            if ball.y > screen_height:
                balls.remove(ball)
                balls.append(Ball())
                lives -= 1
                if lives == 0:
                    print(f"Game Over! Final Score: {score}")
                    pygame.quit()
                    return
            elif paddle.y < ball.y + ball.radius < paddle.y + paddle.height and paddle.x < ball.x < paddle.x + paddle.width:
                balls.remove(ball)
                balls.append(Ball())
                score += 1

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
