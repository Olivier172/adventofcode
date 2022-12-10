import numpy as np
#Objective Simulate your complete hypothetical series of motions. 
# How many positions does the tail of the rope visit at least once?

def main():
    print("day9")
    file =open("input.txt","r")
    lines = file.readlines()
    head = [0,0] #start position of the head
    tail = [0,0] #start position of the tail
    tailPositions = list() #keep track of 
    for line in lines:
        direction, steps = line.split()
        steps = int(steps)
        
        for step in range(steps):
            print
            if(direction=='U'):
                head[1]+=1
            elif(direction=='D'):
                head[1]-=1
            elif(direction=='L'):
                head[0]-=1
            elif(direction=='R'):
                head[0]+=1
            
            diff = [head[0] - tail[0], head[1] - tail[1]]
            #print(diff)

            #If the head is ever two steps directly up, down, left, or right from the tail,
            #the tail must also move one step in that direction so it remains close enough:  
            if(head[0]==tail[0] or head[1]==tail[1]): #check if tail and head are in the same row or column
                #x distance larger than 2? tail follows 1 position in that direction
                if( abs(diff[0])==2 and abs(diff[1])==0 ):
                    tail[0]+=diff[0]/2 #follow one step in that direction
                #y distance larger than 2? tail follows 1 position in that direction
                elif( abs(diff[0])==0 and abs(diff[1])==2 ):
                    tail[1]+=diff[1]/2 #follow one step in that direction
            else: #check wether they are diagnally still adjacent if not in same row or column
                if( abs(diff[0])==1 and abs(diff[1])==2 ):
                    tail[0]+=diff[0]
                    tail[1]+=diff[1]/2
                elif( abs(diff[0])==2 and abs(diff[1])==1):
                    tail[0]+=diff[0]/2
                    tail[1]+=diff[1]

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
# There are 6098 positions that the tail visited at least once