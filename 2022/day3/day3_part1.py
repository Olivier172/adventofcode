#return the common char in 2 strings
def compareStrings(s1,s2):
    for char in s1:
        if char in s2:
            return char
        
def main():
    print("Day3")
    file = open("input.txt","r")
    lines = file.readlines()
    sum=0
    for line in lines:
        line=line.strip()#remove newline chars
        length= len(line)
        comp1=line[0:int(length/2)]
        comp2=line[int(length/2):length]
        char = compareStrings(comp1,comp2)
        if(char.isupper()): # Uppercase item types A through Z have priorities 27 through 52.
            priority = ord(char) - ord('A') +27
        else:# Lowercase item types a through z have priorities 1 through 26.
            priority = ord(char) - ord('a') +1
        #print(priority)
        sum+=priority
    print(f"The sum of the priorities of those item types is {sum}")
        

main()

# The goal:
# Find the item type that appears in both compartments of each rucksack. 
# What is the sum of the priorities of those item types?

# output
# The sum of the priorities of those item types is 8202