import random, time

scorePlayer = 0
scoreComp = 0
dictGame = {1: "Stone", 2: "Scissors", 3: "Paper"}

def start():
    print("Welcome to the Game Stone, Scissors, and Paper")
    print("You will play with a Computer")
    print("You can choose:\n"
      "0 : To end the game\n"
      "1 : Stone\n"
      "2 : Scissors\n"
      "3 : Paper")
    print("Well, let's get started")
    play()

def play():
    player = move()
    comp = random.randint(1,3)
    result(player, comp)

def move():
    while True:
        player = int(input("Make a move: "))
        if player < 0 or player > 3 or player == "":
            print("You inserted invalid Arguments, please choose between 0 to 3")
            play()
        if player == 0:
            scores()
        if player in (1, 2, 3):
            return player

def result(player, comp):
    global scorePlayer, scoreComp
    print("1....")
    time.sleep(0.5)
    print("2....")
    time.sleep(0.5)
    print("3....")
    time.sleep(0.5)
    print("Computer threw {0}".format(dictGame[comp]))
    if (player == 1 and comp == 1) or (player == 2 and comp == 2) or (player == 3 and comp == 3):
        print("Draw")
    elif (player == 1 and comp == 2) or (player == 2 and comp == 3) or (player == 3 and comp == 1):
        print("Congrats, you won")
        scorePlayer += 1
    else:
        print("We are sorry, computer won the game")
        scoreComp += 1
    play()

def scores():
    global scorePlayer, scoreComp
    print("your score is: ", scorePlayer)
    print("the computer score is: ", scoreComp)
    exit()

start()