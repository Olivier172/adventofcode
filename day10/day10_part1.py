 # objective: Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. 
 # What is the sum of these six signal strengths?

def main():
    print("day10")
    file = open("input.txt","r")
    lines = file.readlines()
    cycle=0
    X=1
    sum=0
    for line in lines:   
        cycle+=1 #every instuction a cycle happens
        if((cycle-20)%40 == 0):
            sum+= cycle*X
            print(f"Cycle {cycle}, sum {sum}")

        if(line.startswith("addx")):
            cycle+=1
            if((cycle-20)%40 == 0): #check during cycle
                sum+= cycle*X
                print(f"Cycle {cycle}, sum {sum}")
            amount = int(line.split()[1])
            X+=amount #afer cycle value of register X increases
            #print(X)
        elif(line.startswith("noop")):
            continue

    print(f"The sum of these six signal strenghts is {sum}")

if __name__ == "__main__":
    main()

# output:
# Cycle 20, sum 420
# Cycle 60, sum 1440
# Cycle 100, sum 1840
# Cycle 140, sum 4780
# Cycle 180, sum 8560
# Cycle 220, sum 13180
# The sum of these six signal strenghts is 13180
