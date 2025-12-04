from sys import version

import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    # print("Hello from asteroids-game!")
    # print(f"Starting Asteroids with pygame version: {version}")
    print("Starting Asteroids...")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    # Game properties
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    frames_rate = 60.0
    dt = 0  # stand for delta

    # Game loop start
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt_ms = clock.tick(frames_rate)
        dt = dt_ms / 1000
        # print(f">>> Check delta result: {dt}")


if __name__ == "__main__":
    main()
