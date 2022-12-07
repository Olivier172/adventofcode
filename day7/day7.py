# Objective:
# Find all of the directories with a total size of at most 100000. 
# What is the sum of the total sizes of those directories?

class Dir(object):
    
    def __init__(self, name='/',parent=None):
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

    def getChild(self, name):
        for child in self.getChildren():
            if isinstance(child,Dir) and child.getName() == name:
                return child
        return None #not found, shouldn't happen
    
    def addChild(self,child):
        self.children.append(child)

    def totalSize(self) -> int:
        sum=0
        for child in self.getChildren():
            print(isinstance(child,Dir))
            if isinstance(child,Dir):
                sum += child.totalSize()
            else:
                sum += child.getSize()
                print("size of file in totalsize " +str(child.getSize()) )
        return sum
    

class File(object):

    def __init__(self, name , size):
        self.name = name
        self.size = size

    def getSize(self):
        return self.size


def buildTree():
    file = open("input.txt","r")
    lines = file.readlines()
    root = Dir()
    parent = root
    lastCommand = [] #bv cd hsswswtq
    for line in lines:
        elements = line.split()
        if elements[0] == "$": #elements = ["$" "command"] and command is ls or cd
            print("command" + str(elements))
            lastCommand = elements[1::]
            print("last command "+ str(lastCommand))
            continue

        if lastCommand[0]=="ls": #lastCommand = ["ls" "something"]
            if elements[0] == "dir": #Dir
                print("Dir " + str(elements))
                parent.addChild(Dir(elements[1],parent))
            else: #file
                print("file " + str(elements))
                parent.addChild(File(elements[1],int(elements[0])))
        
        if lastCommand[0]=="cd": #lastCommand = ["cd" "dirname"]
            if lastCommand[1]== "..":
                parent = parent.getParent()
            elif lastCommand[1] == "/":
                parent = root
            else: #cd to a child
                parent = parent.getChild(lastCommand[1])
                


    return root

def sumDirSizes(root:Dir, maxsize) -> int:
    
    total=0 #sum of all dirsize under maxsize
    Dirs = root.getChildren()
    for child in Dirs:
        sumChild=0
        if isinstance(child,Dir):
            ts = child.totalSize()
            sumChild = ts
            Dirs.append(child) #add this to the list of dirs to evaluate
            #print("dir added to list " + child.getName() + " with ts " + str(ts) )
        else:
            sumChild = child.getSize()

        if sumChild <maxsize:
            total+=sumChild
            #print("total increased :" + str(total))

    return total


def main():
    print("Day7")
    root = buildTree()
    print(root)
    sum = sumDirSizes(root,100000)
    print(f"the sum of the total sizes of those directories is {sum}")

if __name__ == "__main__":
    main()