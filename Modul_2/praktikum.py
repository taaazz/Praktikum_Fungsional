import random

position = lambda start, input, a, b: start + (-input.count(a) + input.count(b))
theInput = lambda what: int(input(what))

def initializeBoard(width, height, playerCol, playerRow, goalCol, goalRow):
    board = [['-' for _ in range(width)] for _ in range(height)]
    board[playerCol][playerRow] = 'A'
    board[goalCol][goalRow] = 'O'
    return board

def randomPos(width, height):
    while True:
        row = random.randint(0, width - 1)
        col = random.randint(0, height - 1)
        yield row, col

def newPosition(board, input, startCol, startRow):
    newBoard = [row[:] for row in board]
    newBoard[startCol][startRow] = '-'
    newCol = position(startCol, input, "w", "s")
    newRow = position(startRow, input, "a", "d")
    if newBoard[newCol][newRow] == 'O':
        newBoard[newCol][newRow] = 'A'
        return newBoard, True
    else:
        newBoard[newCol][newRow] = 'A'
        return newBoard, False



def main():
    width = theInput("\nBoard Width : ")
    height = theInput("Board Height : ")
    randomGen = randomPos(width, height)
    reset = 0
    try:
        while reset < 3:
            playerRow, playerCol = next(randomGen)
            goalRow, goalCol = next(randomGen)
            theBoard = initializeBoard(width, height, playerCol, playerRow, goalCol, goalRow)
            for w in theBoard:
                print(' '.join(w))
            if reset < 3:
                pilih = input("New Position y/n = ")
                if pilih == "y":
                    reset += 1
                    if reset >= 3:
                        updatedBoard = [row[:] for row in theBoard]
                elif pilih == "n":
                    updatedBoard = [row[:] for row in theBoard]
                    break
    except StopIteration:
        print("Maximum random positions reached")

    print("\nLet's Play\n")
    for w in updatedBoard:
        print(' '.join(w))
    while True:
        pilih = input("What is your move = ")
        updatedBoard, win = newPosition(updatedBoard, pilih, playerCol, playerRow)
        for w in updatedBoard:
            print(' '.join(w))
        if win:
            print("\nYou Win\n")
            break
        else:
            print("\nYou Lose\n")
            break

main()
