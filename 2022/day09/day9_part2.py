import numpy as np
# Objective Simulate your complete series of motions on a larger rope with ten knots. 
# How many positions does the tail of the rope visit at least once?

#print the grid (doesn't work :/)
def printKnots(knots):
    GRID_HEIGHT=21
    GRID_WIDTH=26
    count=9
    tekens=['H','1','2','3','4','5','6','7','8','9']
    reverse=knots[::-1]
    for r in range(GRID_HEIGHT):
        for c in range(GRID_WIDTH):
            count=0
            for knot in reverse: #reverse to make sure lowest number of knot is drawn on top
                x=knot[0]
                y=knot[1]
                if(GRID_HEIGHT-r-1==x and GRID_WIDTH-c-1 ==y):
                    print(tekens[-count], end="")
                else:
                    print(".",end="")
                count+=1
        print("") #newline
    print("") #newline

def resolveTailPosition(head, tail, diff):
    #If the head is ever two steps directly up, down, left, or right from the tail,
    #the tail must also move one step in that direction so it remains close enough:  
    #x distance larger than 2? tail follows 1 position in that direction
    if( abs(diff[0])==2 and abs(diff[1])==0 ):
        tail[0]+=diff[0]//2 #follow one step in that direction
    #y distance larger than 2? tail follows 1 position in that direction
    elif( abs(diff[0])==0 and abs(diff[1])==2 ):
        tail[1]+=diff[1]//2 #follow one step in that direction
    #check wether they are diagnally still adjacent if not in same row or column
    #follow one step in both directions if one of the following conditions is true:
    elif( abs(diff[0])==1 and abs(diff[1])==2 ):
        tail[0]+=diff[0]
        tail[1]+=diff[1]//2
    elif( abs(diff[0])==2 and abs(diff[1])==1):
        tail[0]+=diff[0]//2
        tail[1]+=diff[1]
    elif(abs(diff[0])==2 and abs(diff[1])==2): #new case that is possible if the previous knot had to move diagonally
        tail[0]+=diff[0]//2
        tail[1]+=diff[1]//2

def main():
    print("day9")
    file =open("input.txt","r")
    lines = file.readlines()
    knots= []#ten knots, including head as the first one and tail as the last one
    for i in range(0,10):
        knots.append([0,0])
    tailPositions = list() #keep track of unique tail positions
    for line in lines:
        direction, steps = line.split()
        steps = int(steps)
        
        for step in range(steps):
            if(direction=='U'):
                knots[0][1]+=1
            elif(direction=='D'):
                knots[0][1]-=1
            elif(direction=='L'):
                knots[0][0]-=1
            elif(direction=='R'):
                knots[0][0]+=1
        
            for i in range(len(knots)-1):
                head=knots[i]
                tail=knots[i+1]
                diff = [head[0] - tail[0], head[1] - tail[1]]
                resolveTailPosition(head, tail, diff)
                
            tail=knots[-1]
            element = [tail[0],tail[1]] #copy tail

            if( element not in tailPositions):
                #print(f"new tail position : {element}")
                tailPositions.append(element)                    
     
    #print(tailPositions)
    amountofpositions =  len(tailPositions)#eleminate duplicates and count unique positions of tail
    print(f"There are {amountofpositions} positions that the tail visited at least once")
            
if __name__ == "__main__":
    main()

# output:
# There are 2597 positions that the tail visited at least once