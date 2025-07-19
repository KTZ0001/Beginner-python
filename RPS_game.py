import  random  #importing random module for the game 
i=0       
# defining the scores  
you=0     
comp=0
for i in range(5):  #usage of for loop, its like a best of 5 match up
    user=int(input("Select your choice from the given options: 1-Rock, 2-Paper or 3-Scissors: "))
    rock=1  #assigning the values for rock paper and scissor
    paper=2
    scissor=3
    computer=random.choice([1,2,3])  #giving the list for random function
    #usage of if elif ladder
    if(user==1 and computer==1):
        print("You both choose rock,its a draw")
    elif(user==1 and computer==2):
        print("You choose rock and computer choose paper, OOPS YOU LOST!")
        comp+=1   #adding 1 to the scoreboard 
    elif(user==1 and computer==3):
        print("You choose rock and computer choose scissor, YEE YOU WON!")
        you+=1
    elif(user==2 and computer==2):
        print("You both choose paper, its a draw")    
    elif(user==2 and computer==1):
        print("You choose paper and computer choose rock,YEE YOU WON")
        you+=1
    elif(user==2 and computer==3):
        print("You choose paper and computer choose scissor,OOPS YOU LOST")
        comp+=1
    elif(user==3 and computer==3):
        print("You both choose scissor, its a draw")
    elif(user==3 and computer==1):
        print("You choose scissor and computer choose rock,OOPS YOU LOST")
        comp+=1
    elif(user==3 and computer==2):
        print("You choose scissor and computer choose paper,YEE YOU WON")
        you+=1
    else:
        print("Please enter a valid choice")

print(f"SCORE:YOUR-{you},COMPUTER-{comp}")  #printing the scoreboard