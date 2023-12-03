# objective: After the rearrangement procedure completes, what crate ends up on top of each stack?
# but this time the cranemove 9001 can move mutliple crates at once
AMOUNT_OF_STACKS = 9


def main():
    print("day5")
    file = open("input.txt")
    lines = file.readlines()
    #step1 :Constructing a 2d list (a lists of lists)
    stacks=list()
    for i in range(0,AMOUNT_OF_STACKS):
        stacks.append(list())
    readStacks=1
    for line in lines:
        #step2:
        #reading the stacks at the beginning, end in a newline and after that the reangement procedures are specified in the input
        if( line == "\n") :
            readStacks=0 #put flag down to stop reading in stacks
            for i in range(0,AMOUNT_OF_STACKS):
                stacks[i].reverse() #reverse the lists if we are done reading the input, so the top element is the last element in the list
            #print the stacks at the beginning
            print("The stacks at the beginning before any rearrangements")
            for i in range(0,AMOUNT_OF_STACKS):
                print(f"stack {i+1}:" + str(stacks[i]))
            print("")
            continue
            
        #as long as the readStacks flag is enabled, continue to read in stacks    
        if(readStacks):
            stack_index=0
            for c in range(1,(AMOUNT_OF_STACKS)*4,4):
                #lets make sure we don't try to read out of bounds
                if(c > len(line)-1):
                    continue
                char = line[c]
                if char.isalpha(): #if there was a lette here, add it to the stack
                    stacks[stack_index].append(char) #add it to the list of this stack
                stack_index+=1
        else:
            #step3:
            #performing the rearrangement procedures to the stacks
            elements = line.split() #example: move,4,from,2,to,1
            for e in elements:
                if(e.isalpha()):
                    elements.remove(e)
            #example: 4,2,1
            amount=int(elements[0])
            src=int(elements[1])-1 #-1 to make sure stack 1 is at index 0
            dst=int(elements[2])-1

            cases = stacks[src][-1:-(amount+1):-1] #take the amount of cases from top to bottem of stack src
            cases=cases[::-1] # reverse the order to bottem to top (in order of the current stack)
            for i in range(amount):
                stacks[src].pop(-1) #remove cases from src stack
            stacks[dst].extend(cases) #place cases on top of dst stack
    
    #step4:printing the results
    #print the stacks:
    print("Stacks at the end (after all the rearrengements)")
    for i in range(0,AMOUNT_OF_STACKS):
        print(f"stack {i+1}:" + str(stacks[i]))
    cratesAtTheTop=""
    for i in range(0,AMOUNT_OF_STACKS):
        cratesAtTheTop+=stacks[i][-1] #appending the last crate of each stack
    print("After the rearrangement procedure completes, these crates end up on top of each stack : " + cratesAtTheTop)
    
main()

# output:
# The stacks at the beginning before any rearrangements
# stack 1:['G', 'F', 'V', 'H', 'P', 'S']
# stack 2:['G', 'J', 'F', 'B', 'V', 'D', 'Z', 'M']
# stack 3:['G', 'M', 'L', 'J', 'N']
# stack 4:['N', 'G', 'Z', 'V', 'D', 'W', 'P']
# stack 5:['V', 'R', 'C', 'B']
# stack 6:['V', 'R', 'S', 'M', 'P', 'W', 'L', 'Z']
# stack 7:['T', 'H', 'P']
# stack 8:['Q', 'R', 'S', 'N', 'C', 'H', 'Z', 'V']
# stack 9:['F', 'L', 'G', 'P', 'V', 'Q', 'J']

# Stacks at the end (after all the rearrengements)
# stack 1:['V', 'R']
# stack 2:['V', 'N', 'Z', 'P', 'V', 'H', 'B', 'L', 'G', 'V', 'S', 'H', 'J', 'F', 'W']
# stack 3:['N', 'G', 'P', 'P', 'R', 'M', 'N', 'G', 'Z', 'V', 'D', 'F', 'L']
# stack 4:['C', 'S', 'Z', 'H', 'C', 'Z', 'J', 'W']
# stack 5:['V', 'M', 'G']
# stack 6:['M', 'Q', 'B', 'Q', 'V', 'R', 'P', 'L', 'T', 'P', 'S', 'J']
# stack 7:['G']
# stack 8:['F']
# stack 9:['D']
# After the rearrangement procedure completes, these crates end up on top of each stack : RWLWGJGFD

