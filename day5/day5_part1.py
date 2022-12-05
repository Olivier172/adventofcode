# objective: After the rearrangement procedure completes, what crate ends up on top of each stack?
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
            elements = line.split()
            for e in elements:
                if(e.isalpha()):
                    elements.remove(e)
            amount=int(elements[0])
            src=int(elements[1])-1 #-1 to make sure stack 1 is at index 0
            dst=int(elements[2])-1

            for i in range(amount):
                case = stacks[src][-1]
                stacks[src].pop(-1) #remove top element
                stacks[dst].append(case) #place top element on new stack

        
            

    
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
# stack 1:['S', 'F']
# stack 2:['N', 'S', 'G', 'P', 'V', 'P', 'H', 'D', 'Z', 'V', 'R', 'J', 'G', 'H', 'C']
# stack 3:['H', 'Z', 'N', 'Z', 'C', 'V', 'P', 'B', 'S', 'M', 'L', 'W', 'V']
# stack 4:['G', 'D', 'W', 'V', 'M', 'P', 'L', 'R']
# stack 5:['N', 'R', 'L']
# stack 6:['B', 'J', 'G', 'J', 'V', 'Q', 'F', 'F', 'G', 'Z', 'T', 'M']
# stack 7:['V']
# stack 8:['Q']
# stack 9:['P']
# After the rearrangement procedure completes, these crates end up on top of each stack : FCVRLMVQP
