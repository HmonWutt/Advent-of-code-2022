grid = []

for i in range(200): #15 for to visualise test data
    grid.append(['.' for i in range(200)]) #40 to visualise test data


tmp = open("data.txt", "r").readlines()
tmp_2 = [(i.strip()).split('\n') for i in tmp]
data = []
for i in tmp_2:
    [tmp_3] = [j.split('->') for j in i]
    data.append(tmp_3)
num = 490

def make_row_col(ipt,num):
    tmp = ipt.split(",")
    tmp_col = int(tmp[0])-num
    tmp_row = int(tmp[1])
    return tmp_row,tmp_col

for eachrow in data:
    for end,start in enumerate(eachrow[:-1]):

        start_row,start_col = make_row_col(start,490)
    
        end_row,end_col = make_row_col(eachrow[end+1],490)
        if start_row == end_row:

            if start_col == end_col:
                continue
            if start_col > end_col:
                for col in range(end_col,start_col+1):
                    if grid[start_row][col] != '#':
                        #print(f"row:{start_row},column: {col}")
                        grid[start_row][col] = '#'

            else:
                for col in range(start_col,end_col+1):
                   
                    if grid[start_row][col] != '#':
                        #print(f"row:{start_row},column: {col}")
                        grid[start_row][col] = '#'

        if start_col == end_col:
            if start_row == end_row:
                continue
            if start_row > end_row:
                for row in range(end_row,start_row+1):
                    
                    if grid[row][start_col] != '#':
                        #print(f"row:{row},column: {start_col}")
                        grid[row][start_col] = '#'
            

            else:
                for row in range(start_row,end_row+1):
                    
                    if grid[row][start_col] != '#':
                        #print(f"row:{row},column: {start_col}")
                        grid[row][start_col] = '#'
lowest_row = 0
for each_pair in data:    
    for col_row in each_pair:
        colrow = col_row.split(',')
        row = int(colrow[1])
        if row > lowest_row:
            lowest_row = row
print(f'lowest row:{lowest_row}')


row = 0
col = 10
#grid[row][col] = '+'
count = 0
def position_sand (row,col): 

    while (0<col <200): ###REMEMBER to change this when changing grid dimensions
        if row >= lowest_row:
            print('Overflow!',row,col)
            return 0
        
           
        if grid[row+1][col] == '.':  
            return position_sand(row+1,col)
    

        if grid[row+1][col-1] == '.':
            return position_sand(row+1,col-1)

        if grid[row+1][col+1] == '.':
            return position_sand(row+1,col+1)
        
        else:
            grid[row][col] = 'o'
            return 1
    
        
       
    
            
for i in range(500):
    position_sand(0,10)
    #print(f'return:{position_sand(0,10)}')
    

    if position_sand(0,10) == 0:
        #print(f'return:{position_sand(0,10)}')
        break
    
    else:
        pass
        #print('not yet')
        
for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 'o':
                    count+=1
                    #print(f"count: {count}")         
print(f'Part one answer: {count}')

################################### Part Two #######################################
grid_2 = []
for i in range(2000): #15 for to visulise test data
    grid_2.append(['.' for i in range(2000)]) #32 for test
for eachrow in data:
    for end,start in enumerate(eachrow[:-1]):

        start_row,start_col = make_row_col(start,250)   ##480 for test
    
        end_row,end_col = make_row_col(eachrow[end+1],250)
        if start_row == end_row:

            if start_col == end_col:
                continue
            if start_col > end_col:
                for col in range(end_col,start_col+1):
                    if grid_2[start_row+1][col] != '#':
                        #print(f"row:{start_row},column: {col}")
                        grid_2[start_row+1][col] = '#'

            else:
                for col in range(start_col,end_col+1):
                   
                    if grid_2[start_row+1][col] != '#':
                        #print(f"row:{start_row},column: {col}")
                        grid_2[start_row+1][col] = '#'

        if start_col == end_col:
            if start_row == end_row:
                continue
            if start_row > end_row:
                for row in range(end_row+1,start_row+2):
                    
                    if grid_2[row][start_col] != '#':
                        #print(f"row:{row},column: {start_col}")
                        grid_2[row][start_col] = '#'
            

            else:
                for row in range(start_row+1,end_row+2):
                    
                    if grid_2[row][start_col] != '#':
                        #print(f"row:{row},column: {start_col}")
                        grid_2[row][start_col] = '#'
floor = lowest_row+2


floor = floor+1 #move the row one unit lower###

grid_2[0][250] = '+'   ####grid_2[0][150] if the len of row 32
#print(grid_2)
for col in range(len(grid_2[0])):
    grid_2[floor][col] = '#'


def fill_sand (row,col): 

    while (0<col <2000): ###40 for test ###1000 for data
        if grid_2[1][250] =='o': 
            print('Blocked the source!',row,col)
            return 0
        
           
        if grid_2[row+1][col] == '.':  
            return fill_sand(row+1,col)
    

        if grid_2[row+1][col-1] == '.':
            return fill_sand(row+1,col-1)

        if grid_2[row+1][col+1] == '.':
            return fill_sand(row+1,col+1)
        
        else:
            grid_2[row][col] = 'o'
           
            return 1
    
        
count_2 = 0     
    
            
for i in range(50000):
    #fill_sand(0,150)
    #print(f'return:{fill_sand(0,250)}')
    

    if fill_sand(0,250) == 0:

        break
    
    else:
        continue
        #print('not yet')
      

count_2=0        
for row in range(len(grid_2)):
            for col in range(len(grid_2[0])):
                if grid_2[row][col] == 'o':
                    count_2+=1
                    #print(f"count: {count}")         
print(f'Part two answer: {count_2}')

#print(grid_2)


