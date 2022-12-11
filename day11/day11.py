
class Monkey():

    def __init__(self, items:list, Tdiv:int, Mtrue:int, Mfalse:int, opAdd:int=0, opMult:int=1 ):
        self.items = items
        self.opAdd = opAdd
        self.opMult = opMult
        self.Tdiv = Tdiv
        self.Mtrue = Mtrue
        self.Mfalse = Mfalse
        self.inspections = 0
        self.monkeys=[]

    def __str__(self) -> str:
        res = f"Monkey with: \n\titems {self.items} \n\toperation new = old*{self.opMult} + {self.opAdd}\n\tMtrue {self.Mtrue} \n\tMfalse {self.Mfalse} \n\ttDiv {self.Tdiv} \n\tinspections {self.inspections}"
        return res

    def setMonkeys(self,monkeys:list):
        self.monkeys=monkeys

    def getInspections(self):
        return self.inspections


    def operation(self, item:int) -> int:
        if(self.opMult==-1):
            item*=item #old squared
        else:
            item = item*self.opMult + self.opAdd #operation
        item= item//3 #monkey gets bored with item
        return item

    def test(self, item) -> bool:
        return (item%self.Tdiv==0)

    def addItem(self, item):
        self.items.append(item)

    def takeTurn(self):
        for item in self.items:
            self.inspections+=1 #monkey expects a new item
            self.items.remove(item) #throw to other monkey based on test below
            item=self.operation(item)
            print(self.test(item))
            if(self.test(item)):
                self.monkeys[self.Mtrue].addItem(item)
            else: 
                self.monkeys[self.Mfalse].addItem(item)
            
def main():
    print("day11")
    monkeys = list()
    startitems = []
    Tdiv = 0
    MTrue = 0
    MFalse = 0 
    opAdd = 0
    opMult = 0
    file = open("input.txt","r")
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if(line.startswith("Monkey")):
            continue
        elif(line.startswith("Starting items:")):
            line = line.removeprefix("Starting items:")
            line = line.strip()
            startitems = [int(x) for x in line.split(", ")]
        elif(line.startswith("Operation: new = old * ")):
            line = line.removeprefix("Operation: new = old * ")
            line = line.strip()
            if(line=="old"):
                opAdd=0
                opMult=-1 #special value to indicate old squared
            else:
                opAdd=0
                opMult=int(line)
        elif(line.startswith("Operation: new = old + ")):
            line = line.removeprefix("Operation: new = old + ")
            line = line.strip()
            opAdd=int(line)
            opMult=1 #special value to indicate old squared
        elif(line.startswith("Test: divisible by ")):
            line = line.removeprefix("Test: divisible by ")
            line = line.strip()
            Tdiv = int(line)
        elif(line.startswith("If true: throw to monkey ")):
            line = line.removeprefix("If true: throw to monkey ")
            line = line.strip()
            MTrue = int(line)
        elif(line.startswith("If false: throw to monkey ")):
            line = line.removeprefix("If false: throw to monkey ")
            line = line.strip()
            MFalse= int(line)
            #one monkey is fully descriped, make object and add to list
            monkey = Monkey(startitems,Tdiv,MTrue,MFalse,opAdd,opMult)
            monkeys.append(monkey)
    
    for monkey in monkeys:
        print(monkey)
        monkey.setMonkeys(monkeys)
    
    print(f"len monkeys {len(monkeys)}")
    for round in range(20):
        for monkey in monkeys:
            monkey.takeTurn()

    inspections = list()
    i=0
    for monkey in monkeys:
        print(f"Monkey {i}: {monkey.getInspections()} inspections")
        inspections.append(monkey.getInspections())
        i+=1
    
    inspections.sort(reverse=True)
    print(f"The level of monkey busisess {inspections[0] * inspections[1]}")

    return 0

if __name__ == "__main__":
    main()