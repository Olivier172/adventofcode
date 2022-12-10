 # objective: Render the image given by your program. 
 # What eight capital letters appear on your CRT?

import numpy as np
SCREEN_WIDTH = 40
SCREEN_HEIGHT = 6

def main():
    print("day10")
    file = open("input.txt","r")
    lines = file.readlines()
    cycle=0
    X=1
    CRTscreen = np.zeros((SCREEN_HEIGHT,SCREEN_WIDTH),dtype=int)
    for line in lines: 
        # every cycle a pixel is drawn, 
        # since the rows are 40 wide we can determine the position of the pixel we are drawing as follows: 
        row = cycle//40 
        col = cycle%40 
        #print(f"row {row} col {col} cycle {cycle}")
        # is the position of the sprite currently in the pixel we are drawing? 
        # (sprite is 3 pixels wide, so if middle of sprite is at col-1 and col+1 it is also at the pixel we are currently drawing) 
        if(X in [col-1,col,col+1]): 
            CRTscreen[row][col]=1 #if yes, light this pixel up
        cycle+=1 #every instuction a cycle happens
        
        if(line.startswith("addx")): 
            row = cycle//40 
            col = cycle%40 
            #print(f"row {row} col {col} cycle {cycle}")
            if(X in [col-1,col,col+1]):
                CRTscreen[row][col]=1
            cycle+=1 #the add operation takes 2 cycles
            amount = int(line.split()[1])
            X+=amount #afer cycle value of register X increases
        elif(line.startswith("noop")):
            continue

    for i in range(len(CRTscreen)):
        for j in range(len(CRTscreen[0])):
            if(CRTscreen[i][j]):
                print("#",end="")
            else:
                print(".",end="")
        print("")

if __name__ == "__main__":
    main()

# output:
####.####.####..##..#..#...##..##..###..
#.......#.#....#..#.#..#....#.#..#.#..#.
###....#..###..#....####....#.#..#.###..
#.....#...#....#....#..#....#.####.#..#.
#....#....#....#..#.#..#.#..#.#..#.#..#.
####.####.#.....##..#..#..##..#..#.###..