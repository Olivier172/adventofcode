
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
 
# Checks if the number n
def numberContainsRepeatedGroupOfDigits(numberToCheck: int) -> bool:
    numberToCheckString = str(numberToCheck)
    length = len(numberToCheckString)

    # check for every valid groupLength if it is a repeating group of digits in the numberToCheck
    for groupLength in range(1, length // 2 + 1):
        # group length must be a divisor of length in order for the repeated group to be able to match to number to check
        if length % groupLength == 0:
            groupOfDigits = numberToCheckString[:groupLength]
            if groupOfDigits * (length // groupLength) == numberToCheckString:
                return True
    return False
   
# for part 2 a product id that consists of a repeating group of digits is invalid
def findInvalidProductIds(productIdRanges: list[ProductIdRange]) -> list[int]:
    invalidProductIds = []
    for productIdRange in productIdRanges:
        productId = productIdRange.GetFirstId()
        while(productId <= productIdRange.GetLastId()):
            if(numberContainsRepeatedGroupOfDigits(productId)):
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
# The sum of all invalid product ids is 11323661261