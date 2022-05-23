from random import randrange

lists = []
innerList = []
board = []
randNum = randrange(1, 3)
print(randNum)
playerOne = ""
playerTwo = ""
oneToPlay = False
userWon = False
isDraw = True
nameEntered = False
oneScore = 0
twoScore = 0
winnings = [
    ["2-3", "4-7", "5-9"],
    ["1-3", "5-8"],
    ["6-9", "1-2", "7-5"],
    ["1-7", "5-6"],
    ["1-9", "3-7", "2-8", "4-6"],
    ["4-5", "3-9"],
    ["1-4", "3-5", "8-9"],
    ["2-5", "7-9"],
    ["3-6", "1-5", "7-8"]
]


def resetBoard():
    for i in range(len(board)):
        board[i] = "-"


def main():
    global userWon
    fillArray()
    print(" welcome to tic tac toe")
    rounds = int(input("how many rounds are y'all gonna be playing today?"))
    if rounds >= 1:
        while rounds >= 1:
            gamePlay()
            rounds -= 1
            resetBoard()
            displayBoard()
            userWon = False
    else:
        print("sorry rounds cant be less then 1 ")
        main()
    print("what a game final score at the end of the rounds is ", playerOne, " ", oneScore, " : ", twoScore, " ",
          playerTwo)


# def fillarray():
# for i in range(3):
#  innerList.clear()
# for j in range(3):
#  if ((j + 1) % 2 == 0):
#        innerList.append("x")
#    else:
#         innerList.append("o")

#   lists.append(innerList)
# for i in range(len(lists)):
#   print(lists[i], "\n")
def fillArray():
    for i in range(9):
        board.append('-')


def displayBoard():
    for i in range(3):
        if i == 0:
            print("| " + board[i] + " |", "| " + board[i + 1] + " |", "| " + board[i + 2] + " |")
        elif i == 1:
            print("| " + board[i + 2] + " |", "| " + board[i + 3] + " |", "| " + board[i + 4] + " |")
        else:
            print("| " + board[i + 4] + " |", "| " + board[i + 5] + " |", "| " + board[i + 6] + " |")
        print("\n")


def switchUsers(rand):
    global oneToPlay
    global randNum
    if oneToPlay:

        turn = rand
        randNum += 1
        oneToPlay = False

    else:

        turn = rand
        randNum -= 1
        oneToPlay = True

    return turn


def switch(randy):
    global randNum
    if (randy == 1):

        randNum += 1
        print(randy)
    else:

        randNum -= 1
        print(randy)


def gamePlay():
    global randNum
    global oneToPlay
    global isDraw
    global oneScore
    global twoScore
    global playerOne, playerTwo, nameEntered
    if not nameEntered:
        print("hello welcome to tic tac toe")
        playerOne = str(input("player one  please enter your name"))
        print("welcome " + playerOne, "\n")
        playerTwo = str(input("player one  please enter your name"))
        print("welcome " + playerTwo, "\n")
    if randNum == 1:
        print("congrats " + playerOne + " you get to play first")
        oneToPlay = True
    else:
        print("congrats " + playerTwo + " you get to play first")
        oneToPlay = False
    displayBoard()
    count = 0
    while count <= 8:
        turn = switchUsers(randNum)
        if turn == 1:
            play = int(input(playerOne + " play"))
            if checkInput(play):
                randNum -= 1
                oneToPlay = True
                print("oops sorry  invalid input ", playerOne + "please play again")
                count -= 1
            else:
                if board[play - 1] != "-":
                    print("oops sorry position filled", playerTwo + "please play again")
                    randNum -= 1
                    oneToPlay = True
                    count -= 1
                else:
                    board[play - 1] = "x"
                    checkWinnings(play - 1)
        else:
            play = int(input(playerTwo + " play"))
            if checkInput(play):
                randNum += 1
                oneToPlay = False
                print("oops sorry  invalid input ", playerTwo + "please play again")
                count -= 1
            else:
                if board[play - 1] != "-":
                    print("oops sorry position filled  ", playerTwo + "please play again")
                    randNum += 1
                    oneToPlay = False
                    count -= 1
                else:
                    board[play - 1] = "o"
                    checkWinnings(play - 1)
        count += 1
        displayBoard()
        if userWon:
            isDraw = False
            if randNum == 1:
                print(playerTwo + " congrats you have won the game")
                twoScore += 1
            else:
                print(playerOne + " congrats you have won the game")
                oneScore += 1
            break
        print(len(board))

    if isDraw:
        print("ooh what a battle game ended in a draw")
    nameEntered = True


def checkWinnings(index):
    global userWon
    for i in range(len(winnings[index])):
        ind = winnings[index][i].split("-")
        if board[index] == "x" and board[int(ind[0]) - 1] == "x" and board[int(ind[1]) - 1] == "x" or board[
            index] == "o" and \
                board[int(ind[0]) - 1] == "o" and board[int(ind[1]) - 1] == "o":
            userWon = True
            break


def checkInput(userInput):
    if userInput < 1 or userInput > 9:
        print("invalid user input")
        return True
    else:
        return False

print("git hello world")

main()
