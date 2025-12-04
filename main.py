from sys import version

import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    print("Hello from asteroids-game!")
    print(f"Starting Asteroids with pygame version: {version}")
    print("Starting Asteroids...")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Khởi tạo pygame, tạo screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    frames_rate = 60.0
    dt = 0  # stand for delta

    # Tạo group
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # Thêm player thích hợp vào group
    Player.containers = (updatable, drawable)

    # Tạo đối tượng Player
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y)

    # Vòng lặp while game:
    while True:
        # - Ghi log
        log_state()
        # - Thoát game nếu bắt được sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # - fill màn hình đen
        screen.fill("black")
        # - Cập nhật vị trí player
        updatable.update(dt)
        # - vẽ player
        for obj in drawable:
            obj.draw(screen)
        # - flip màn hình
        pygame.display.flip()
        # - tính thời gian trôi qua giữa hai khung hình (dùng cho chuyển động mượt)
        dt_ms = clock.tick(frames_rate)
        dt = dt_ms / 1000


if __name__ == "__main__":
    main()
