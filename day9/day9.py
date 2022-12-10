import numpy as np
#Objective Simulate your complete hypothetical series of motions. 
# How many positions does the tail of the rope visit at least once?

def main():
    print("day9")
    file =open("input.txt","r")
    lines = file.readlines()
    head = np.array([0,0]) #start position of the head
    tail = np.array([0,0]) #start position of the tail
    tailPositions = list() #keep track of 
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
            
            diff = head - tail
            #print(diff)

            #x distance larger than 2? tail follows 1 position in that direction
            if( np.equal(abs(diff),np.array([2,0])).all() ):
                print(tail)
            
            #y distance larger than 2? tail follows 1 position in that direction
            if( np.equal(abs(diff),np.array([0,2])).all() ):
                tail[1]+=diff[1]/2

            if( np.equal(abs(diff),np.array([1,2])).all() or np.equal(abs(diff),np.array([2,1])).all() ):
                tail[0]+=diff[0]/2
                tail[1]+=diff[1]/2
                print(tail)

            element = np.copy(tail)
            tailPositions.append(element)
            
            
    print(tailPositions)
    amountofpositions =  len(set(tuple(i) for i in tailPositions))#eleminate duplicates and count unique positions of tail
    print(f"There are {amountofpositions} positions that the tail visited at least once")
            
                
        
    
if __name__ == "__main__":
    main()