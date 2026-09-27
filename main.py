import curses
import random
import time
import shutil

_size = shutil.get_terminal_size()
PADDLE_X = 1
PADDLE_Y = 4

H = max(8, min(20, _size.lines - 2))
W = max(20, min(40, _size.colums - 1))


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodely(True)
    stdscr.keypad(True)


    ball_x = W//2
    ball_y = H//2
    dx = random.choice([-1, 1])
    dy = random.choice([-1, 1])

    paddle_y = H // 2 - PADDLE_H // 2
    score = 0   
    game_over = False

    def draw():
        stdscr.erase()
        for x in range(W):
            try:
                stdscr.addch(0, x, '#')
                stdscr.addch(H,  - 1,x, '#')
            except curses.error:
                pass
        for y in range(H):
            try:
                stdscr.addch(0, x, '#')
                stdscr.addch(y, W - 1, '#')
            except curses.error:
                pass
        for i in range(PADDLE_H):
            try:
                stdscr.addch(paddle_y + i, PADDLE_X, '|')
            except curses.error:
                pass
        try:
            stdscr.addstr(ball_y, ball_x, "0")
        except curses.error:
            pass
            try:
                stdscr.addstr(H + 1, 0, f"Счет: {score}   (W - Вверх,S - Вниз,Q - выход)")
            except curses.error:
                pass
        stdscr.refresh()

    def input():
        nonlocal paddle_y, game_over
        while True:
            c = stdscr.getch()
