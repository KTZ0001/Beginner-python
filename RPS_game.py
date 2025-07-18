import  random 
user=int(input("Select your choice from the given options: 1-Rock, 2-Paper or 3-Scissors"))
rock=1
paper=2
scissor=3
computer=random.choice([1,2,3])
if(user==1 and computer==1):
    print("You both choose rock,its a draw")
elif(user==1 and computer==2):
    print("You choose rock and computer choose paper, OOPS YOU LOST!")
elif(user==1 and computer==3):
    print("You choose rock and computer choose scissor, YEE YOU WON!")
elif(user==2 and computer==2):
    print("You both choose paper, its a draw")    
elif(user==2 and computer==1):
    print("You choose paper and computer choose rock,YEE YOU WON")
elif(user==2 and computer==3):
    print("You choose paper and computer choose scissor,OOPS YOU LOST")
elif(user==3 and computer==3):
    print("You both choose scissor, its a draw")
elif(user==3 and computer==1):
    print("You choose scissor and computer choose rock,OOPS YOU LOST")
elif(user==3 and computer==2):
    print("You choose scissor and computer choose paper,YEE YOU WON")
else:
    print("Please enter a valid choice")