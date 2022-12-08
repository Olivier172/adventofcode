from copy import deepcopy
#objective : Consider each tree on your map. What is the highest scenic score possible for any tree?

def sceneryScore(forest,x,y):
    up=0
    down=0
    left=0
    right=0
    height=forest[x][y]
    #print(f"Height at {x},{y} is {height}")
    #look up
    for row in range(x-1,-1,-1):
        up+=1
        if(forest[row][y] >= height):
            break
            
    #look down
    for row in range(x+1,len(forest)):
        down+=1
        if(forest[row][y] >= height):
            break
            
            
    #look left
    for col in range(y-1,-1,-1):
        left+=1
        if(forest[x][col] >= height):
            break
            
    #look right
    for col in range(y+1,len(forest[0])):
        right+=1
        if(forest[x][col] >= height):
            break
            
    ss = up*down*left*right
    #print(f"up {up} down {down} left {left} right {right}")
    return ss

def findHighestSceneryScore(forest):
    maxss=0
    for row in range(len(forest)):
        for col in range(len(forest[0])):
            ss=sceneryScore(forest, row, col)
            if(ss>maxss):
                #print(ss)
                maxss=ss
    return maxss
    
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
    maxss=findHighestSceneryScore(forest)
    print(f"the highest scenic score possible for any tree is {maxss}")
    file.close()
    return 0

if __name__ == "__main__":
    main()
    
# output:
# the highest scenic score possible for any tree is 315495