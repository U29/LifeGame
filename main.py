"""LifeGame"""

import pygame
from pygame.locals import *
import sys
import random
import copy

(WIDTH, HEIGHT) = (400, 400)
SCREEN_SIZE = (WIDTH, HEIGHT)  # 画面サイズ

# ゲーム内変数・関数の設定
CELLS = [[0 for i in range(int(WIDTH/10))] for j in range(int(HEIGHT/10))]

def cell_check(check_x, check_y):
    """ To check cell dead or alive for next turn """
    living = 0
    if CELLS[check_y][check_x-1] == 1:
        living += 1
    if CELLS[check_y][check_x+1] == 1:
        living += 1
    if CELLS[check_y-1][check_x] == 1:
        living += 1
    if CELLS[check_y+1][check_x] == 1:
        living += 1
    if CELLS[check_y+1][check_x-1] == 1:
        living += 1
    if CELLS[check_y-1][check_x+1] == 1:
        living += 1
    if CELLS[check_y+1][check_x+1] == 1:
        living += 1
    if CELLS[check_y-1][check_x-1] == 1:
        living += 1
    return living

# pygameを初期化
pygame.init()
# SCREEN_SIZEの画面を作成
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
# タイトルバーの文字列をセット
pygame.display.set_caption("LifeGame")
SCREEN.fill((0, 0, 0))

# 枠線を表示(塗りなし正方形)
for x in range(int(WIDTH/10)):
    for y in range(int(HEIGHT/10)):
        pygame.draw.rect(SCREEN, (0, 0, 255), ((x * 10, y * 10), (10, 10)), 1)

# 初期セルをランダム生成
for x in range(int(WIDTH/10)):
    for y in range(int(HEIGHT/10)):
        if random.randint(0, 1):
            CELLS[y][x] = 1

for y in range(int(HEIGHT / 10)):
    for x in range(int(WIDTH / 10)):
        if CELLS[y][x] == 1:
            pygame.draw.rect(SCREEN, (0, 255, 255), ((x * 10, y * 10), (10, 10)))
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), ((x * 10, y * 10), (10, 10)))
pygame.display.update()  # 画面を更新
# pygame.time.delay(1000)

# ゲームループ
while True:
    CELLS_TEMP = copy.deepcopy(CELLS)
    for y in range(int(HEIGHT/10)):
        for x in range(int(WIDTH/10)):
            if (x == 0) or (y == 0) or (x == int(WIDTH/10-1)) or (y == int(WIDTH/10-1)):
                CELLS_TEMP[y][x] = 2
            else:
                if CELLS[y][x] == 0:  # 死んでるセルに対する処理
                    if cell_check(x, y) == 3:  # 誕生
                        CELLS_TEMP[y][x] = 1
                        # print("誕生")

                else:  # 生きているセルに対する処理
                    if cell_check(x, y) >= 4:
                        CELLS_TEMP[y][x] = 0
                        # print("過密")
                    if cell_check(x, y) <= 1:
                        CELLS_TEMP[y][x] = 0
                        # print("過疎")

    for y in range(int(HEIGHT/10)):  # 描画
        for x in range(int(WIDTH/10)):
            if CELLS_TEMP[y][x] == 1:    # 生
                pygame.draw.rect(SCREEN, (255, 255, 255), ((x * 10, y * 10), (10, 10)))
            elif CELLS_TEMP[y][x] == 0:  # 死
                pygame.draw.rect(SCREEN, (0, 0, 0), ((x * 10, y * 10), (10, 10)))
            elif CELLS_TEMP[y][x] == 2:  # 枠線(生死判定なし)
                pygame.draw.rect(SCREEN, (150, 150, 0), ((x * 10, y * 10), (10, 10)))
    CELLS = copy.deepcopy(CELLS_TEMP)

    # 枠線を表示(塗りなし正方形)
    for x in range(int(WIDTH / 10)):
        for y in range(int(HEIGHT / 10)):
            if (x == 0) or (y == 0) or (x == int(WIDTH / 10 - 1)) or (y == int(WIDTH / 10 - 1)):
                pass
            else:
                pygame.draw.rect(SCREEN, (0, 0, 0), ((x * 10, y * 10), (10, 10)), 1)
    pygame.display.update()  # 画面を更新
    pygame.time.delay(30)
    # イベント処理
    for event in pygame.event.get():
        if event.type == QUIT:  # 終了イベント
            sys.exit()
