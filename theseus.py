#Maze-Solving Problem for Archangel
#Authored by Alex Whelan

import random

def createmaze():
    line1 = list(input('Please enter maze line 1:\n'))
    line2 = list(input('Please enter maze line 2:\n'))
    line3 = list(input('Please enter maze line 3:\n'))
    line4 = list(input('Please enter maze line 4:\n'))
    line5 = list(input('Please enter maze line 5:\n'))
    maze = [line1, line2, line3, line4, line5]
    return maze

def Theseus(maze):
    maze_solve = False
    while maze_solve == False: 
        
        for i in range(len(maze)):
            try: location = [i, maze[i].index('S')]
            except ValueError:
                pass
    
        if location[0] == 0 or location[1] == 0 or location[0] == len(maze) or location[1] == len(maze[0]):
            maze_solve = True
            print('Maze solved.')
            return maze
            break
        else:
            left = [location[0], location[1]-1]
            right = [location[0], location[1]+1]
            up = [location[0]-1, location[1]]
            down = [location[0]+1, location[1]]
            
            whats_left = maze[left[0]][left[1]]
            whats_right = maze[right[0]][right[1]]
            whats_up = maze[up[0]][up[1]]
            whats_down = maze[down[0]][down[1]]
            
            directions = [['left', 'right', 'up', 'down'], [whats_left, whats_right, whats_up, whats_down]]
            choices = []
    
            for i in range(len(directions[1])):
                if directions[1][i] == 'O':
                    choices.append(directions[0][i])
                    
            try: maze_step = random.choice(choices)
            except IndexError:             
                for i in range(len(directions[1])):
                    if directions[1][i] == '1':
                        choices.append(directions[0][i])
                        maze_step = random.choice(choices)
             
            
            if maze_step == 'left':
                maze[left[0]][left[1]] = 'S'
            elif maze_step == 'right':
                maze[right[0]][right[1]] = 'S'
            elif maze_step == 'up':
                maze[up[0]][up[1]] = 'S'
            else:
                maze[down[0]][down[1]] = 'S'
                
            maze[location[0]][location[1]] = '1'
            
            print('Step taken.')
            for i in range(len(maze)):
                print(maze[i])
            
                
           