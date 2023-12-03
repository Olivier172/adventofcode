
def main():
    file = open("input.txt","r")
    lines = file.readlines()
    elfs=[]
    sum=0
    for line in lines:
        if(line.strip().isnumeric()):
            number = int(line.strip())
            sum+= number
        else: #if empty line, numbers for this elf are done and we can save the sum
            #print(sum)
            elfs.append(sum)
            sum=0
    elfs.sort(reverse=True)
    print("Answer to question 1")
    print(elfs[0])
    print("Answer to question 2")
    print(elfs[0]+elfs[1]+elfs[2])

    return 0
main()

#output :
#Answer to question 1
#70116
#Answer to question 2
#206582