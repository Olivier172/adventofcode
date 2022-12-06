# Objective part1: 
# How many characters need to be processed before the first start-of-packet marker is detected?
# objective part2:
# A start-of-message marker is just like a start-of-packet marker, 
# except it consists of 14 distinct characters rather than 4.
# How many characters need to be processed before the first start-of-message marker is detected?

#find out how many chars need to be processed to find the first start of packet marker
#length gives how many chars the packet marker is 
def findSOP(datastream,length):
    amountOfChars =0
    for i in range(0,len(datastream)):
        packet = datastream[i:i+length]
        if(len(set(packet)) == len(packet)):
            #print("All elements are unique.")
            return i+length
        else:
             #print("All elements are not unique.")
             pass
    return -1


    return amountOfChars

def main():
    file=open("input.txt","r")
    datastream = file.readline()
    
    #part1
    length=4 #packet is 4 long
    amountOfChars = findSOP(datastream,length)
    print(f"There are {amountOfChars} chars that need to be processed before the first start-of-packet marker is detected")
    
    #part2
    length=14
    amountOfChars = findSOP(datastream,length)
    print(f"There are {amountOfChars} chars that need to be processed before the first start-of-message marker is detected")
    return 0

main()

# output:
# There are 1578 chars that need to be processed before the first start-of-packet marker is detected
# There are 2178 chars that need to be processed before the first start-of-message marker is detected