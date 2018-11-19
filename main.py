import pygame
from pygame.locals import *
import sys
import random
import copy

(width, height) = (800, 800)
SCREEN_SIZE = (width, height)  # 画面サイズ
global cells
cells = [[0 for i in range(int(width/10))] for j in range(int(height/10))]

# pygameを初期化
pygame.init()
# SCREEN_SIZEの画面を作成
screen = pygame.display.set_mode(SCREEN_SIZE)
# タイトルバーの文字列をセット
pygame.display.set_caption("LifeGame")
screen.fill((0, 0, 0))

# 枠線を表示(塗りなし正方形)
for x in range(int(width/10)):
    for y in range(int(height/10)):
        pygame.draw.rect(screen, (0, 0, 255), ((x * 10, y * 10), (10, 10)), 1)

# 初期セルをランダム生成
for x in range(int(width/10)):
    for y in range(int(height/10)):
        if random.randint(0, 1):
            cells[y][x] = 1

for y in range(int(height / 10)):
    for x in range(int(width / 10)):
        if cells[y][x] == 1:
            pygame.draw.rect(screen, (0, 255, 255), ((x * 10, y * 10), (10, 10)))
        else:
            pygame.draw.rect(screen, (0, 0, 0), ((x * 10, y * 10), (10, 10)))
pygame.display.update()  # 画面を更新
# pygame.time.delay(1000)


# print(cells)
# ゲームループ
while True:
    cellsTemp = copy.deepcopy(cells)
    for y in range(int(height/10)):
        for x in range(int(width/10)):
            living = 0
            if (x == 0) or (y == 0) or (x == int(width/10-1)) or (y == int(width/10-1)):
                cellsTemp[y][x] = 2
                pass
            else:
                if cells[y][x] == 0:  # 死んでるセルに対する処理
                    if cells[y][x-1] == 1:
                        living += 1
                    if cells[y][x+1] == 1:
                        living += 1
                    if cells[y-1][x] == 1:
                        living += 1
                    if cells[y+1][x] == 1:
                        living += 1
                    if cells[y+1][x-1] == 1:
                        living += 1
                    if cells[y-1][x+1] == 1:
                        living += 1
                    if cells[y+1][x+1] == 1:
                        living += 1
                    if cells[y-1][x-1] == 1:
                        living += 1

                    if living == 3:  # 誕生
                        cellsTemp[y][x] = 1
                        # print("誕生")

                else:  # 生きているセルに対する処理
                    if cells[y][x-1] == 1:
                        living += 1
                    if cells[y][x+1] == 1:
                        living += 1
                    if cells[y-1][x] == 1:
                        living += 1
                    if cells[y+1][x] == 1:
                        living += 1
                    if cells[y+1][x-1] == 1:
                        living += 1
                    if cells[y-1][x+1] == 1:
                        living += 1
                    if cells[y+1][x+1] == 1:
                        living += 1
                    if cells[y-1][x-1] == 1:
                        living += 1

                    if living >= 4:
                        cellsTemp[y][x] = 0
                        # print("過密")
                    if living <= 1:
                        cellsTemp[y][x] = 0
                        # print("過疎")

    for y in range(int(height/10)):  # 描画
        for x in range(int(width/10)):
            if cellsTemp[y][x] == 1:    # 生
                pygame.draw.rect(screen, (255, 255, 255), ((x * 10, y * 10), (10, 10)))
            elif cellsTemp[y][x] == 0:  # 死
                pygame.draw.rect(screen, (0, 0, 0), ((x * 10, y * 10), (10, 10)))
            elif cellsTemp[y][x] == 2:  # 枠線(生死判定なし)
                pygame.draw.rect(screen, (150, 150, 0), ((x * 10, y * 10), (10, 10)))
    cells = copy.deepcopy(cellsTemp)

    # 枠線を表示(塗りなし正方形)
    for x in range(int(width / 10)):
        for y in range(int(height / 10)):
            if (x == 0) or (y == 0) or (x == int(width / 10 - 1)) or (y == int(width / 10 - 1)):
                pass
            else:
                pygame.draw.rect(screen, (0, 0, 0), ((x * 10, y * 10), (10, 10)), 1)
    pygame.display.update()  # 画面を更新
    pygame.time.delay(30)
    # イベント処理
    for event in pygame.event.get():
        if event.type == QUIT:  # 終了イベント
            sys.exit()
