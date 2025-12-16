
class Dial:
    
    def __init__(self, initialDialPosition: int):
        self._dialPosition = initialDialPosition
        self._countDialPositionAtZero = 0

    def RotateDial(self, direction: str, amount: int):
        # determine new dial position step by step to count every time it reaches position zero
        # even if that happens during a rotation
        for i in range(amount):
            if (direction == "L"):
                self._dialPosition = self._dialPosition - 1
                if(self._dialPosition < 0):
                    self._dialPosition = 99
            else:
                self._dialPosition = self._dialPosition + 1
                if(self._dialPosition > 99):
                    self._dialPosition = 0
            # check position zero after every click
            if(self._dialPosition == 0):  
                self._countDialPositionAtZero += 1 # count zero position
                #print(f"dial in position 0 (count _countDialPositionAtZero = {self._countDialPositionAtZero})")
                
        return
                      
    def GetCountDialPositionAtZero(self) -> int:
        return self._countDialPositionAtZero

    

def parse_input(fileName: str) -> list:
    file = open(fileName, "r")
    dial_rotations = file.readlines()
    return dial_rotations

def main():
    # retrieve list of dial rotations from input file
    dial_rotations = parse_input("input.txt")
    
    # create dial at initial position 50
    dial = Dial(50)
    
    # apply rotations
    for rotation in dial_rotations:
        direction = rotation[0]
        amount = int(rotation[1:])
        dial.RotateDial(direction, amount)
        
    CountDialPositionAtZero = dial.GetCountDialPositionAtZero()
    
    print(f"The dial has been at position zero {CountDialPositionAtZero} times.")
    
main()

# correct output:
# The dial has been at position zero 5657 times.