#Objective Simulate your complete hypothetical series of motions. 
# How many positions does the tail of the rope visit at least once?

def main():
    print("day9")
    file =open("input.txt","r")
    lines = file.readlines()
    head = [0,0] #start position of the head
    tail = [0,0] #start position of the tail
    tailPositions = set()
    for line in lines:
        direction, steps = line.split()
        steps = int(steps)
        
        for step in range(steps):
            if(direction=='U'):
                head[1]+=1
            elif(direction=='D'):
                head[1]-=1
            elif(direction=='L'):
                head[0]-=1
            elif(direction=='R'):
                head[0]+=1
            
            #x distance larger than 2? tail follows 1 position in that direction
            diff=head[0]-tail[0]
            if(abs(diff) == 2):
                tail[0]+=(diff/2)
            
            #y distance larger than 2? tail follows 1 position in that direction
            diff=head[1]-tail[1]
            if(head[1]-tail[1]==2):
                tail[1]+=(diff/2)
                
            tailPositions.add(tail) # save talk position
            
    amountofpositions = len(tailPositions)
    print("There are {amountofpositions} positions that the tail visitied at least once")
            
                
        
    
if __name__ == "__main__":
    main()