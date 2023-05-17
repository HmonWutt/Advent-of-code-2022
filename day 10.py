import numpy as np
import pandas as pd
test = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''.split('\n')
#print(test)

# test_data_1 = [j for j in test]
# x_length = len(test_data_1)
# y_length = len(test_data_1[0])
alphabet_lst = [i for i in 'SabcdefghijklmnopqrstuvwxyzE']
#print(alphabet_lst)
# print(alphabet_lst.index('E'))
# graph = np.zeros((x_length, y_length))
# for index_i,i in enumerate(test_data):
#     for index_j, j in enumerate(i):
#         graph[index_i][index_j] = alphabet_lst.index(j)
# print(graph)
unvisited = []
visited = []
tmp = []
unvisited_lst = []

for x,i in enumerate(test):
    for y,j in enumerate(i):
        tmp.append(alphabet_lst.index(j))
        unvisited_lst.append((x,y))
        if len(tmp)>=5:
            unvisited.append(tmp)
            tmp = []
#print(unvisited)
#print(unvisited_lst)
x_length = len(unvisited)
y_length = len(unvisited[0])

def find_neighbour(x,y,graph):
    neighbour_lst = [(1,0),(-1,0),(0,1),(0,-1)]

    visited = []
    while unvisited:

        for xx,yy in neighbour_lst:
            current_x = x
            current_y = y
            current_node = graph[current_x][current_y]
            neighbour_x = current_x+xx
            neighbour_y = current_y+yy
            #neighbour_node= graph[neighbour_x][neighbour_y]
            #print(abs(graph[neighbour_x][neighbour_y]-current_node))
            #print(0<=neighbour_x<=x_length , 0<=neighbour_y<=y_length )
            if abs(graph[neighbour_x][neighbour_y]-current_node)<=1 and \
                    0<=neighbour_x<=x_length and 0<=neighbour_y<=y_length and \
                    (neighbour_x,neighbour_y) not in visited:
                visited.append((neighbour_x,neighbour_y))
                current_x = neighbour_x
                current_y = neighbour_y
                print((current_x,current_y))
    print(visited)
print(find_neighbour(0,0,unvisited))

