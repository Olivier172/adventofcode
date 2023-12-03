#(Your total score is the sum of your scores for each round.) 
#A = rock
#B = paper
#C = scissors
#X means you need to lose, 
# Y means you need to end the round in a draw,
#  and Z means you need to win.
#The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
#plus the score for the outcome of the round (0 if you lost,
#3 if the round was a draw, and 6 if you won).
#returns the score of the rock paper scissor duel
def evaluateScore(opponent, you):
    score=0
    if you == "X": #you need to lose
        score+=0 #loss is 0 points
        if opponent=="A": 
            score+=3 #scissors
            return score
        elif opponent=="B": 
            score+=1 #rock
            return score 
        elif opponent=="C":
            score+=2 #paper
            return score 
    elif you == "Y": #you need to draw
        score+=3 #draw is 3 points
        if opponent=="A": 
            score+=1 #rock
            return score
        elif opponent=="B":
            score+=2 #paper
            return score 
        elif opponent=="C": 
            score+=3 #scissors
            return score 
    elif you == "Z": # you need to win
        score+=6 #win is 6 points
        if opponent=="A": 
            score+=2 #paper
            return score
        elif opponent=="B": 
            score+=3 #scissors
            return score 
        elif opponent=="C": 
            score+=1 #rock
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

#output: 
#your total score is 9975