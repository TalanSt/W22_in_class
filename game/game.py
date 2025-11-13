from random import randint

print("Welcome to rock paper scissors!")

rand = randint(1, 3)

if(rand == 1): print("Computer chose rock")
if(rand == 2): print("Computer chose paper")
if(rand == 3): print("Computer chose scissors")