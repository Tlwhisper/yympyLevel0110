print('----I love work----')
temp = input("guss what I am want?\n")
guess = int(temp)
if guess == 8:
    print("good you are right!!!")
    print("but not fish")
else:
    if guess > 8:
        print("too big")
    else:
        print("too small")
print("game over")

