import numpy as np
with open('Day 8_input', 'r') as f:
    lines = [i.rstrip() for i in f.readlines()]

MAX_X = len(lines[0])
MAX_Y = len(lines)

forest = np.zeros((MAX_Y, MAX_X), dtype=int)
for index_i,i in enumerate(lines):
    for index_j, j in enumerate(i):
        forest[index_i][index_j] = int(j)
def visible(row,col,matrix):
    edge = []
    tree = matrix[row,col]
    visible_trees= set()
    edges = len(matrix[0:,0])-1
    if (row == 0 or row == edges) or (col == 0 or col == edges):
        edge.append((row,col))
    else:
        '''visible from left'''
        if tree > np.max(matrix[row, :col],initial=matrix[row,0]):
            visible_trees.add((row,col))
        elif tree > np.max(matrix[row, col+1:],initial=matrix[row,-1]):
            visible_trees.add((row,col))
        elif tree > np.max(matrix[:row,col],initial=matrix[0,col]):
            visible_trees.add((row,col))
        elif tree > np.max(matrix[row+1:,col],initial=matrix[-1,col]):
            visible_trees.add((row,col))
        else:
            pass
    return edge,visible_trees

edge_set = set()
interior_trees_set = set()

for row,tree_row in enumerate(forest):
    for col,tree in enumerate(tree_row):
        edge,visible_tree = visible(row,col,forest)
        #print(edge)
        edge_set.update(edge)
        interior_trees_set.update(visible_tree)

all_visible_trees = len(interior_trees_set)+len(edge_set)
print(f"\nPart one answer: {all_visible_trees}")

def scenic_score_calculator(row,col,matrix):
    count = 0
    scenic_score = 1
    current_tree = matrix[row,col]
    for i in matrix[row+1:,col]:
        if i >= current_tree:
            count +=1
            break
        count+=1
    scenic_score = scenic_score*count
    count = 0
    for i in matrix[:row,col][::-1]:
        if i >= current_tree:
            count +=1
            break
        count+=1
    scenic_score = scenic_score * count
    count = 0
    for i in matrix[row,col+1:]:
        if i >= current_tree:
            count +=1
            break
        count+=1
    scenic_score = scenic_score * count
    count = 0
    for i in matrix[row,:col][::-1]:
        if i>= current_tree:
            count +=1
            break
        count+=1
    scenic_score = scenic_score * count
    return scenic_score
scenic_score_lst = []
for row,tree_row in enumerate(forest):
    for col,tree in enumerate(tree_row):
        scenic_score = scenic_score_calculator(row,col,forest)
        scenic_score_lst.append(scenic_score)

print(f"Part two answer: {max(scenic_score_lst)}")