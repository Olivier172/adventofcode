
class ProductIdRange:
    
    def __init__(self, firstId: int, lastId: int):
        self._firstId = firstId
        self._lastId = lastId
        
    def __str__(self) -> str:
        return f"Range from {self._firstId} to {self._lastId}"
        
    def GetFirstId(self) -> int:
        return self._firstId
    
    def GetLastId(self) -> int:
        return self._lastId
    
    
def parse_input(fileName: str) -> list[ProductIdRange]:
    file = open(fileName, "r")
    line = file.readline()
    rangeStrings = line.split(",")
    
    ranges = []
    for rangeString in rangeStrings:
        (firstId, lastId) = rangeString.split("-")
        range = ProductIdRange(int(firstId), int(lastId))
        ranges.append(range)
        
    return ranges
    
# for part 1 an invalid product id is a number that consists of a repeating number if we split the orginal number in half
def findInvalidProductIds(productIdRanges: list[ProductIdRange]) -> list[int]:
    invalidProductIds = []
    for productIdRange in productIdRanges:
        productId = productIdRange.GetFirstId()
        while(productId <= productIdRange.GetLastId()):
            productIdString = str(productId)
            
            # only product ids with even lengths can repeat the same digits twice
            if(len(productIdString) % 2 == 0):
                halfLength = int(len(productIdString)/2)
                leftPart = productIdString [:halfLength]
                rightPart = productIdString [halfLength:]
                #print(f"product id {productId} with even length with leftpart: {leftPart} and rightPart {rightPart}")
                if(leftPart == rightPart):
                    #print(f"invalid productId found {productId}")
                    invalidProductIds.append(productId)
                    
            productId += 1
            
    return invalidProductIds
        
    
def main():
    productIdRanges = parse_input("input.txt")
    
    invalidProductIds = findInvalidProductIds(productIdRanges)
    
    invalidProductIdSum = 0
    for invalidProductId in invalidProductIds:
        invalidProductIdSum += invalidProductId
    
    print(f"The sum of all invalid product ids is {invalidProductIdSum}")

main()

# Correct output
# The sum of all invalid product ids is 9188031749