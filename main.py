import sys
from sys import version

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    # print("Hello from asteroids-game!")
    # print(f"Starting Asteroids with pygame version: {version}")
    # print("Starting Asteroids...")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

    # Khởi tạo pygame, tạo screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y)

    Shot.containers = (shots, updatable, drawable)

    frames_rate = 60.0
    dt = 0  # stand for delta

    while True:
        # - Ghi log
        log_state()

        # - Thoát game nếu bắt được sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteriod in asteroids:
            if asteriod.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                input("Press Enter to quit...")  # waits in the terminal
                sys.exit()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # - tính thời gian trôi qua giữa hai khung hình (dùng cho chuyển động mượt)
        dt_ms = clock.tick(frames_rate)
        dt = dt_ms / 1000


if __name__ == "__main__":
    main()
