from copy import deepcopy
#objective : Consider your map; how many trees are visible from outside the grid?

#vm visibility map is a boolean map to display which trees are visible from outside the grid
def checkVisibility(forest, vm):
    #check visibility from west 
    for row in range(len(forest)):
        maxSeenFromWest=-1
        for col in range(len(forest[0])):
            if forest[row][col]>maxSeenFromWest:
                maxSeenFromWest=forest[row][col]
                vm[row][col] = True
    
    #check visibility from north 
    for col in range(len(forest[0])):
        maxSeenFromNorth=-1
        for row in range(len(forest)):
            if forest[row][col]>maxSeenFromNorth:
                maxSeenFromNorth=forest[row][col]
                vm[row][col] = True
            
        
    #check visibility from east and East:        
    for row in range(len(forest)-1,-1,-1):
        maxSeenFromEast=-1
        for col in range(len(forest[0])-1,-1,-1):
            if forest[row][col]>maxSeenFromEast:
                maxSeenFromEast=forest[row][col]
                vm[row][col] = True
            
    #check visibility from east and south:        
    for col in range(len(forest[0])-1,-1,-1):
        maxSeenFromSouth=-1
        for row in range(len(forest)-1,-1,-1):
            if forest[row][col]>maxSeenFromSouth:
                maxSeenFromSouth=forest[row][col]
                vm[row][col] = True

def countVisibles(vm):
    count=0
    for row in range(len(vm)):
        for col in range(len(vm[0])):
            if(vm[row][col]):
                count+=1
    return count

def main():
    print("Day8")
    
    file = open("input.txt","r")
    lines = file.readlines()
    forest=[] #2d list
    row=0
    for line in lines:
        line = line.strip()
        forest.append(list())#add row
        for c in line:
            forest[row].append(int(c))
        row+=1
        
    #print(forest)
    visibleMap = deepcopy(forest)
    #init vm
    for row in range(len(forest)):
        for col in range(len(forest[0])):
            visibleMap[row][col]= False
    checkVisibility(forest,visibleMap)
    
    #print(visibleMap)
    #for row in range(len(forest)):
    #    for col in range(len(forest[0])):
    #        print(f" {visibleMap[row][col]} ", end="")
    #    print("")
        
    amount = countVisibles(visibleMap)
    print(f"There are {amount} of visible trees from outside the grid")
    file.close()
    return 0

if __name__ == "__main__":
    main()
    
# output:
# There are 1812 of visible trees from outside the grid