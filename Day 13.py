import numpy as np
import string
import ast

from bs4 import element

with open('Day 13 input','r')as f:
    g = [i.rstrip() for i in f.readlines()]


lst = []
tmp = []
for i in g:
    tmp.append(i)
    if i == '':
        tmp.remove('')
        lst.append(tmp)
        tmp = []

def compare(el1,el2):
    if isinstance(el1,list) and isinstance(el2, int) :
        if len(el1) == 0:
            return 1
        return compare(el1, [el2])

    if isinstance(el2,list) and isinstance(el1, int) :
        if len(el2) == 0:
            return -1
        return compare([el1], el2)

    if isinstance(el1, int) and isinstance(el2,int):
        if el1 < el2 :
            return 1
        elif el1 == el2:
            return 0
        else:
            return -1

    if isinstance(el1,list) and isinstance(el2,list):
        res = 0
        i= 0
        while i < (min(len(el1),len(el2))):
            #print(len(el1),len(el2))
            res = compare(el1[i], el2[i])
            if res == -1:
                return -1
            if res == 1:
                return 1
            i+=1
        if i==(min(len(el1),len(el2))):
            if len(el1)>len(el2):
                return -1
            if len(el2)> len(el1):
                return 1
            return 0

    assert False

ans = 0
for ind,i in enumerate(lst):
    #print(i)
    ind+=1
    el1 = eval(i[0])
    el2 = eval(i[1])
    result = compare(el1,el2)
    # print(f'first{i[0]}')
    # print(f'second{i[1]}')
    # print(ind, result)
    if result!= -1:
        ans+=ind

print(f"Part one answer: {ans}")

"""Part two"""
data_two = []
with open("Day 13 test", "r") as file:
    for line in file:
        if not line.isspace():
            data_two.append(eval(line))

first_divider = [[2]]
second_divider = [[6]]
data_two_copy = data_two.copy()
data_two_copy.append(first_divider)
data_two_copy.append(second_divider)
lst = [1,5,6,7,2]
comparator = 0
replacement = 0
def sorter(lst):
    for i in range(len(lst)):
        j = i
        while compare(lst[j-1],lst[j]) == -1 and j-1 >= 0:
            lst[j], lst[j-1] = lst[j-1],lst[j]
            j-=1
    return lst


new_data = sorter(data_two_copy)
for i in new_data:
    print(str(i)+'\n')

index_lst = []
for ind,i in enumerate(new_data):
    if i == [[2]] or i == [[6]]:
        index_lst.append(ind+1)
        if len(index_lst) >1:
            print(f"Part two answer using 'sorter' function: {(index_lst[0]) * (index_lst[1])}")

def the_other_sorter(lst):
    if len(lst) <=1:
        return lst
    greater_than_divider = []
    less_than_divider = []
    divider = lst.pop()
    for i in range(len(lst)):
        if compare(lst[i], divider) == -1:
            greater_than_divider.append(lst[i])
        less_than_divider.append(lst[i])
    return the_other_sorter(less_than_divider) + [divider] + the_other_sorter(greater_than_divider)

part_two = the_other_sorter(data_two_copy)

index_lst_2 = []
for ind,i in enumerate(new_data):
    if i == [[2]] or i == [[6]]:
        index_lst_2.append(ind+1)
        if len(index_lst_2) >1:
            print(f"Part two answer using 'the_other_sorter' function: {(index_lst_2[0]) * (index_lst_2[1])}")





