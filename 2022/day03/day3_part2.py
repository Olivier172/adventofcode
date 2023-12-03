#return the common char in 2 strings
def compareStrings(s1,s2,s3):
    for char in s1:
        if char in s2:
            if char in s3:
                return char
        
def main():
    print("Day3")
    file = open("input.txt","r")
    lines = file.readlines()
    sum=0
    for i in range(0,len(lines),3):
        #the rugsacks of a three elf group:
        line1 = lines[i].strip()
        line2 = lines[i+1].strip()
        line3 = lines[i+2].strip()
        char = compareStrings(line1,line2,line3)
        if(char.isupper()): # Uppercase item types A through Z have priorities 27 through 52.
            priority = ord(char) - ord('A') +27
        else:# Lowercase item types a through z have priorities 1 through 26.
            priority = ord(char) - ord('a') +1
        #print(priority)
        sum+=priority
    print(f"The sum of the priorities of the badges of the three elf groups is {sum}")
        

main()

# The goal:
# Find the item type that corresponds to the badges of each three-Elf group. 
# What is the sum of the priorities of those item types?

# output
# The sum of the priorities of the badges of the three elf groups is 2864