# Objective:
# Find all of the directories with a total size of at most 100000. 
# What is the sum of the total sizes of those directories?

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

def main():
    print("Day7")
    root = buildTree()
    print(root)
    print(f"size of root is {root.getSize()}")
    sum = root.getSolution()
    print(f"the sum of the total sizes of those directories is {sum}")

if __name__ == "__main__":
    main()