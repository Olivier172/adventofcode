#(Your total score is the sum of your scores for each round.) 
#A,X  = rock
#B,Y  = paper
#C,Z  = scissors
#The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
#plus the score for the outcome of the round (0 if you lost,
#3 if the round was a draw, and 6 if you won).
#returns the score of the rock paper scissor duel
def evaluateScore(opponent, you):
    score=0
    if you == "X":
        score+=1
        if opponent=="A": #draw
            score+=3 
            return score
        elif opponent=="B": #loss
            return score 
        elif opponent=="C":#win
            score+=6
            return score 
    elif you == "Y":
        score+=2
        if opponent=="A": #win
            score+=6
            return score
        elif opponent=="B": #draw
            score+=3
            return score 
        elif opponent=="C": #loss
            return score 
    elif you == "Z":
        score+=3
        if opponent=="A": #loss
            return score
        elif opponent=="B": #win
            score+=6
            return score 
        elif opponent=="C": #draw
            score+=3
            return score 
    else:
        print("Something went wrong with your input")



def main():
    print("day2")

    file = open("input.txt","r")
    lines = file.readlines()
    totalscore=0
    for line in lines:
        #on every line we find the choice of your openent and your choice seperated by a space
        line=line.strip() #remove newline character
        opponent_choice , your_choice = line.split(" ") #split line up into opponent input and your input 
        #print(f"opponent choice {opponent_choice} your choice {your_choice}")
        totalscore+=evaluateScore(opponent_choice,your_choice)
    print(f"your total score is {totalscore}")

    return 0

main()

#output : 
#your total score is 12276