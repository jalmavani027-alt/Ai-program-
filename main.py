# game :- rock,paper and scissor

# 1 for rock
# -1 for paper
# 0 for scissor

import random

computer = random.choice([1,-1,0])

youstr = input("Enter your choice: ")
youDict = {
    "r": 1,
    "p": -1,
    "s": 0
}
reversedDict = {
    1 : "Rock",
    -1 : "Paper",
    0 : "Scissor"
}
you = youDict[youstr]
print("you chose:", reversedDict[you])
print("This is computer choice: ", reversedDict[computer])

if(computer ==you):
    print("it's draw")

elif(computer ==1 and you ==-1):
    print("You Win")

elif(computer ==1 and you ==0): 
    print("You Lose")

elif(computer ==0 and you ==1):
    print("You Win")

elif(computer ==0 and you ==-1):
    print("You Lose")

elif(computer ==-1 and you ==0):
    print("You Win")

elif(computer ==-1 and you ==1):
    print("You Lose")

else:
    print("Something went wrong")

