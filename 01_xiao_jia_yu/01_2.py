print('----I love work----')
temp = input("guss what I am want?\n")
guess = int(temp)
while guess !=8 :
    temp = input("guess worng please next time \n")
    guess = int(temp)
    if guess == 8:
        print("good you are right!!!")
        print("but not fish")
        break
    else:
        if guess > 8:
            print("too big")
        else:
            print("too small")
print("game over")
