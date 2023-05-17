import os
os.environ['AOC_SESSION'] ="53616c7465645f5f1927c134e40c726f6073c90991c6c1297f3a911ae7722cc6e8e768666486c65a1d5429f2e02b2b301e4c7ee33f6e6ea3e16aea11985ae804"
from dataclasses import dataclass
from aocd import get_data
data = get_data(day=9, year=2022).split('\n')
test_data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".split('\n')


@dataclass
class Rope:
    x: int
    y: int

head = Rope(0,0)


def h_move(instruction, head: Rope):

    if instruction == 'U':
        head.y+= 1
    elif instruction == 'D':
        head.y-= 1
    elif instruction == 'R':
        head.x+= 1
    else:
        head.x -= 1

def t_move (head : Rope ,tail = Rope):

    delta_x = abs(head.x - tail.x)
    delta_y = abs(head.y - tail.y)
    if delta_x + delta_y == 2:
        if tail.x == head.x and head.y > tail.y:
            tail.y +=1 
        elif tail.x == head.x and head.y < tail.y:
            tail.y -= 1 
        elif tail.y == head.y and head.x > tail.x:
            tail.x +=  1 
        elif tail.y == head.y and head.x < tail.x:
            tail.x -=  1 
        else:
            pass
    elif delta_x + delta_y > 2:
        if head.y > tail.y and head.x > tail.x:
            tail.y +=1
            tail.x +=1
        elif head.y < tail.y and head.x > tail.x:
            tail.y-=1
            tail.x +=1
        elif head.x < tail.x and head.y > tail.y:
            tail.x-=1
            tail.y +=1
        else:
            tail.x-=1
            tail.y -=1
    else:
        pass
tails = [Rope(0,0) for _ in range(9)]
t_points = []
t_path = []
for i in data:
    direction = i[0]
    distance = int(i[2:])
    for i in range(distance):
        h_move(direction,head)
        t_move(head, tails[0])
        for index, t in enumerate(tails):
            if index == 0:
                continue
            t_move(tails[index-1], t)
            t_points.append((tails[-1].x, tails[-1].y))
    t_path+=t_points

    
print(len(set(t_points)))



