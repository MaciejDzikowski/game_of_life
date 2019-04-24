"""
Game of Life

0, 1 or 4 alive neighbours - cell dies
3 or 2 alive neighbours - cell comes alive
"""

import random
import time

n = int(input('Set width of board: '))
m = int(input('Set height of board: '))

def create_board(n, m):
    plansza = []
    for i in range(m):
        plansza.append([])
        for j in range(n):
            plansza[-1].append(random.choice(['♢','♦']))
    plansza[0][0] = '♢'
    plansza[-1][-1] = '♢'
    return plansza

plansza = create_board(n, m)
for i in plansza:
    print(i)

def game():
    s = 0
    plansza2 = [i[:] for i in plansza]
    planszax = [i[:] for i in plansza]
    while sum(planszax[k].count('♢') for k in range(len(planszax))) != n * m:
        for i in range(len(plansza2)):
            for j in range(len(plansza2[i])):
                if plansza2[i][j] == '♦':
                    if i != m - 1:
                        if plansza2[i + 1][j] == '♦':
                            s += 1
                    if i != 0:
                        if plansza2[i - 1][j] == '♦':
                            s += 1
                    if j != n - 1:
                        if plansza2[i][j + 1] == '♦':
                            s += 1
                    if j != 0:
                        if plansza2[i][j - 1] == '♦':
                            s += 1
                if plansza2[i][j] == '♢':
                    if i != m - 1:
                        if plansza2[i + 1][j] == '♦':
                            s += 1
                    if i != 0:
                        if plansza2[i - 1][j] == '♦':
                            s += 1
                    if j != n - 1:
                        if plansza2[i][j + 1] == '♦':
                            s += 1
                    if j != 0:
                        if plansza2[i][j - 1] == '♦':
                            s += 1
                if s == 4 or s == 1 or s == 0:
                    planszax[i][j] = '♢'
                elif s == 2 or s == 3:
                    planszax[i][j] = '♦'
                s = 0
        time.sleep(0.5)
        print(2 * '\n')
        for l in planszax:
            print(l)

        plansza2 = [c[:] for c in planszax]

game()