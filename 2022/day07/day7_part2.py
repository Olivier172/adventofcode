# Objective:
# Find the smallest directory that, if deleted, 
# would free up enough space on the filesystem to run the update. 
# What is the total size of that directory?
TOTAL_SPACE = 70000000
REAQUIRED_SPACE = 30000000
class Dir(object):
    
    def __init__(self, name, parent=None):
        self.children = []
        self.name = name
        self.parent = parent

    def __str__(self):
        res = "Dir node with name : " + self.getName() 
        return res

    def getName(self):
        return self.name
    
    def getParent(self):
        return self.parent

    def getChildren(self):
        return self.children

    def getChild(self, name:str):
        for child in self.getChildren():
            if isinstance(child,Dir) and child.getName() == name:
                return child
        return None #not found, shouldn't happen
    
    def addChild(self,child):
        self.getChildren().append(child)

    def getSize(self) -> int:
        sum=0
        for child in self.getChildren():
            sum += child.getSize()
        return sum
    
    def getSolution(self) -> int:
        values = []
        for child in self.getChildren():
                if(isinstance(child, Dir)):
                    values.append(child.getSolution())
        total = sum(values)
        if(self.getSize() > 100000):
            return total
        else:
            return total + self.getSize()
        
    #returns the minimum size of the subdir to delete that is at least minsize
    #searches all subdirs of this dir, so also recursivly calls the subdirs in subdirs 
    def getMinsizeDirToDelete(self, minsize:int) -> int:
        values = [] #holds all minimum sizes of subdirs in this dir
        for child in self.getChildren():
            if(isinstance(child, Dir)):
                if(child.getSize()>minsize):
                    values.append(child.getSize())
                values.append(child.getMinsizeDirToDelete(minsize))
        if(len(values)>0): 
            minimum = min(values)
            return minimum
        else:
            #this means that none of the subdirs has a size greater than minsize, so we return a large number
            #so that the recursive calls can continue but this number will not be the smallest in total
            return TOTAL_SPACE 

class File(object):

    def __init__(self, name:str , size:int):
        self.name = name
        self.size = size
    
    def __str__(self):
        res = "file with name " + self.name + " and size " + str(self.size)
        return res

    def getSize(self):
        return self.size


def buildTree():
    with open("input.txt","r") as f:
        lines = [line.strip() for line in f.readlines()]
    root = Dir('/')
    cdir = root
    for line in lines:
        elements = line.split()
        #print(elements)
        if elements[1]=="cd":
            if elements[2]== "/":
                cdir = root
            elif elements[2] == "..":
                cdir = cdir.getParent()
            else: #cd to a child
                cdir = cdir.getChild(elements[2])
        elif elements[1]=="ls":
            continue
        else:
            if elements[0] == 'dir': #Dir
                cdir.addChild(Dir(elements[1],cdir))
            else: #file
                cdir.addChild(File(elements[1],int(elements[0])))               
    return root

def getSmallestDirToDelete(root:Dir) -> int:
        res =0
        occupied = root.getSize()
        available = TOTAL_SPACE - occupied
        minimumToFreeUp = REAQUIRED_SPACE - available
        print(f"There is {available} space available and {REAQUIRED_SPACE} needed, that means we still need to free up at least {minimumToFreeUp}")
        res = root.getMinsizeDirToDelete(minimumToFreeUp)
        return res

def main():
    print("Day7")
    root = buildTree()
    min = getSmallestDirToDelete(root)
    print(f"The smallest dir size to delete is {min}")

if __name__ == "__main__":
    main()
    
# output:
# There is 21270855 space available and 30000000 needed, that means we still need to free up at least 8729145
# The smallest dir size to delete is 9608311