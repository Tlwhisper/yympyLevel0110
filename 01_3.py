import random
secret = random.randint(1,10)
print('----I love work----')
temp = input("guss what I am want?\n")
guess = int(temp)
while guess !=secret :
    temp = input("guess worng please next time \n")
    guess = int(temp)
    if guess == secret:
        print("good you are right!!!")
        print("but not fish")
        break
    else:
        if guess > secret:
            print("too big")
        else:
            print("too small")
print("game over")
