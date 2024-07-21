class OthelloGame:
    def __init__(self):
        self.grid = [['-' for _ in range(8)] for _ in range(8)]
        self.grid[3][3] = 'W'
        self.grid[3][4] = 'B'
        self.grid[4][3] = 'B'
        self.grid[4][4] = 'W'
        self.humanPlayer = True
        self.computerPlayer = False
        self.humanPlayerPieceCount = 30
        self.computerPlayerPieceCount = 30
        self.whitePiecesOnBoard = 2
        self.blackPiecesOnBoard = 2
        self.difficulty = 0

    def display(self):
        self.addValidMovesToTheBoard()
        for i in range(8):
            print(i + 1, end=" ")
            for j in range(8):
                print(self.grid[i][j], end=' ')
            print()

    def isThereAValidMove(self):
        for i in range(8):
            for j in range(8):
                if self.grid[i][j] == '*':
                    return True

        return False

    def switchTurns(self):

        if self.humanPlayer:
            self.humanPlayer = False
            self.computerPlayer = True
        else:
            self.humanPlayer = True
            self.computerPlayer = False

    def addValidMovesToTheBoard(self):
        for i in range(8):
            for j in range(8):
                if self.grid[i][j] == '*':
                    self.grid[i][j] = '-'

        if self.humanPlayer:
            for i in range(8):
                for j in range(8):
                    if self.grid[i][j] == 'B':
                        # check the column from below the piece
                        foundWhite = False
                        for k in range(i + 1, 8):
                            if self.grid[k][j] == 'B':
                                break
                            elif self.grid[k][j] == 'W':
                                foundWhite = True
                            else:
                                if foundWhite:
                                    self.grid[k][j] = '*'
                                    break
                                else:
                                    break

                        # check the column from above the piece
                        foundWhite = False
                        for k in range(i - 1, -1, -1):
                            if self.grid[k][j] == 'B':
                                break
                            elif self.grid[k][j] == 'W':
                                foundWhite = True
                            else:
                                if foundWhite:
                                    self.grid[k][j] = '*'
                                    break
                                else:
                                    break

                        # check the row from the right of the piece
                        foundWhite = False
                        for c in range(j + 1, 8):
                            if self.grid[i][c] == 'B':
                                break
                            elif self.grid[i][c] == 'W':
                                foundWhite = True
                            else:
                                if foundWhite:
                                    self.grid[i][c] = '*'
                                    break
                                else:
                                    break

                        # check the row from the left of the piece
                        foundWhite = False
                        for c in range(j - 1, -1, -1):
                            if self.grid[i][c] == 'B':
                                break
                            elif self.grid[i][c] == 'W':
                                foundWhite = True
                            else:
                                if foundWhite:
                                    self.grid[i][c] = '*'
                                    break
                                else:
                                    break
        else:
            for i in range(8):
                for j in range(8):
                    if self.grid[i][j] == 'W':
                        # check the row from below the piece
                        foundBlack = False
                        for k in range(i + 1, 8):
                            if self.grid[k][j] == 'W':
                                break
                            elif self.grid[k][j] == 'B':
                                foundBlack = True
                            else:
                                if foundBlack:
                                    self.grid[k][j] = '*'
                                    break
                                else:
                                    break

                        # check the row from above the piece
                        foundBlack = False
                        for k in range(i - 1, -1, -1):
                            if self.grid[k][j] == 'W':
                                break
                            elif self.grid[k][j] == 'B':
                                foundBlack = True
                            else:
                                if foundBlack:
                                    self.grid[k][j] = '*'
                                    break
                                else:
                                    break

                        # check the column from the right of the piece
                        foundBlack = False
                        for c in range(j + 1, 8):
                            if self.grid[i][c] == 'W':
                                break
                            elif self.grid[i][c] == 'B':
                                foundBlack = True
                            else:
                                if foundBlack:
                                    self.grid[i][c] = '*'
                                    break
                                else:
                                    break

                        # check the column from the left of the piece
                        foundBlack = False
                        for c in range(j - 1, -1, -1):
                            if self.grid[i][c] == 'W':
                                break
                            elif self.grid[i][c] == 'B':
                                foundBlack = True
                            else:
                                if foundBlack:
                                    self.grid[i][c] = '*'
                                    break
                                else:
                                    break

    def humanPlay(self, row, column):
        if self.humanPlayerPieceCount > 0:
            if self.grid[row - 1][column - 1] == '*':
                # check for white pieces above
                foundWhite = False
                for i in range(row - 2, -1, -1):
                    if self.grid[i][column - 1] == 'W':
                        foundWhite = True
                    elif self.grid[i][column - 1] == 'B' and foundWhite:
                        for j in range(row - 1, i, -1):
                            self.grid[j][column - 1] = 'B'
                            self.blackPiecesOnBoard += 1
                            self.whitePiecesOnBoard -= 1
                        self.whitePiecesOnBoard += 1
                        break
                    else:
                        break

                # check for white pieces below
                foundWhite = False
                for i in range(row, 8):
                    if self.grid[i][column - 1] == 'W':
                        foundWhite = True
                    elif self.grid[i][column - 1] == 'B' and foundWhite:
                        for j in range(row - 1, i):
                            self.grid[j][column - 1] = 'B'
                            self.blackPiecesOnBoard += 1
                            self.whitePiecesOnBoard -= 1
                        self.whitePiecesOnBoard += 1
                        break
                    else:
                        break

                # check for white pieces on the right of the piece
                foundWhite = False
                for i in range(column, 8):
                    if self.grid[row - 1][i] == 'W':
                        foundWhite = True
                    elif self.grid[row - 1][i] == 'B' and foundWhite:
                        for j in range(column - 1, i):
                            self.grid[row - 1][j] = 'B'
                            self.blackPiecesOnBoard += 1
                            self.whitePiecesOnBoard -= 1
                        self.whitePiecesOnBoard += 1
                        break
                    else:
                        break

                # check for white pieces on the left of the piece
                foundWhite = False
                for i in range(column - 2, -1, -1):
                    if self.grid[row - 1][i] == 'W':
                        foundWhite = True
                    elif self.grid[row - 1][i] == 'B' and foundWhite:
                        for j in range(column - 1, i, -1):
                            self.grid[row - 1][j] = 'B'
                            self.blackPiecesOnBoard += 1
                            self.whitePiecesOnBoard -= 1
                        self.whitePiecesOnBoard += 1
                        break
                    else:
                        break

                self.humanPlayerPieceCount -= 1
            else:
                print("invalid move")
                return False
        else:
            if self.computerPlayerPieceCount == 0:
                if self.blackPiecesOnBoard > self.whitePiecesOnBoard:
                    print("human won")
                elif self.blackPiecesOnBoard < self.whitePiecesOnBoard:
                    print("computer won")
                else:
                    print("the game is a draw")
                return True
            else:
                self.switchTurns()
                return False

        self.switchTurns()
        return False

    def calcScore(self, row, column):
        # check for black pieces above
        foundBlack = False
        for i in range(row - 1, -1, -1):
            if self.grid[i][column] == 'B':
                foundBlack = True
            elif self.grid[i][column] == 'W' and foundBlack:
                return row - i - 1

        # check for black pieces below
        foundBlack = False
        for i in range(row + 1, 8):
            if self.grid[i][column] == 'B':
                foundBlack = True
            elif self.grid[i][column] == 'W' and foundBlack:
                return i - row - 1

        # check for white pieces on the right of the piece
        foundBlack = False
        for i in range(column + 1, 8):
            if self.grid[row][i] == 'W':
                foundBlack = True
            elif self.grid[row][i] == 'B' and foundBlack:
                return i - column - 1

        # check for white pieces on the left of the piece
        foundBlack = False
        for i in range(column - 1, -1, -1):
            if self.grid[row][i] == 'W':
                foundBlack = True
            elif self.grid[row][i] == 'B' and foundBlack:
                return column - i - 1

        return 0

    def find_A_Valid_Move_Level1(self):
        lowestScore = float('inf')
        rowOfLowestScore = 0
        columnOfLowestScore = 0
        for i in range(8):
            for j in range(8):
                if self.grid[i][j] == '*':
                    score = self.calcScore(i, j)
                    if score < lowestScore:
                        lowestScore = score
                        rowOfLowestScore = i
                        columnOfLowestScore = j
        return rowOfLowestScore, columnOfLowestScore

    def find_A_Valid_Move_Level3(self):
        scores = []
        for i in range(8):
            for j in range(8):
                if self.grid[i][j] == '*':
                    score = self.calcScore(i, j)
                    scores.append((score, (i, j)))

        # Sort the scores based on the first int in each pair
        scores.sort(key=lambda x: x[0])

        # Return the pair at the middle index of the sorted scores
        middle_index = len(scores) // 2
        return scores[middle_index][1]

    def find_A_Valid_Move_Level5(self):
        highestScore = float('-inf')
        rowOfHighestScore = 0
        columnOfHighestScore = 0
        for i in range(8):
            for j in range(8):
                if self.grid[i][j] == '*':
                    score = self.calcScore(i, j)
                    if score > highestScore:
                        highestScore = score
                        rowOfHighestScore = i
                        columnOfHighestScore = j
        return rowOfHighestScore, columnOfHighestScore

    def computerPlay(self):
        if self.computerPlayerPieceCount > 0:
            move = ()
            if self.difficulty == 1:
                move = self.find_A_Valid_Move_Level1()
            elif self.difficulty == 3:
                move = self.find_A_Valid_Move_Level3()
            else:
                move = self.find_A_Valid_Move_Level5()

            row, column = move

            # check for black pieces above
            foundBlack = False
            for i in range(row - 1, -1, -1):
                if self.grid[i][column] == 'B':
                    foundBlack = True
                elif self.grid[i][column] == 'W' and foundBlack:
                    for j in range(row, i, -1):
                        self.grid[j][column] = 'W'
                        self.whitePiecesOnBoard += 1
                        self.blackPiecesOnBoard -= 1
                    self.blackPiecesOnBoard += 1
                    break

            # check for black pieces below
            foundBlack = False
            for i in range(row + 1, 8):
                if self.grid[i][column] == 'B':
                    foundBlack = True
                elif self.grid[i][column] == 'W' and foundBlack:
                    for j in range(row, i):
                        self.grid[j][column] = 'W'
                        self.whitePiecesOnBoard += 1
                        self.blackPiecesOnBoard -= 1
                    self.blackPiecesOnBoard += 1
                    break

            # check for black pieces on the right of the piece
            foundBlack = False
            for i in range(column + 1, 8):
                if self.grid[row][i] == 'B':
                    foundBlack = True
                elif self.grid[row][i] == 'W' and foundBlack:
                    for j in range(column, i):
                        self.grid[row][j] = 'W'
                        self.whitePiecesOnBoard += 1
                        self.blackPiecesOnBoard -= 1
                    self.blackPiecesOnBoard += 1
                    break

            # check for black pieces on the left of the piece
            foundBlack = False
            for i in range(column - 1, -1, -1):
                if self.grid[row][i] == 'B':
                    foundBlack = True
                elif self.grid[row][i] == 'W' and foundBlack:
                    for j in range(column, i, -1):
                        self.grid[row][j] = 'W'
                        self.whitePiecesOnBoard += 1
                        self.blackPiecesOnBoard -= 1
                    self.blackPiecesOnBoard += 1
                    break

            self.computerPlayerPieceCount -= 1
        else:
            if self.humanPlayerPieceCount == 0:
                if self.blackPiecesOnBoard > self.whitePiecesOnBoard:
                    print("human won")
                    return True
                elif self.blackPiecesOnBoard < self.whitePiecesOnBoard:
                    print("computer won")
                    return True
                else:
                    print("the game is a draw")
                    return True
            else:
                self.switchTurns()
                return False

        self.switchTurns()
        return False


def main():
    obj = OthelloGame()
    print("Choose Difficulty, Easy 1, Medium 3, Hard 5: ")
    difficulty = int(input())
    obj.difficulty = difficulty
    while True:
        if obj.humanPlayer:
            obj.display()
            if obj.isThereAValidMove():
                print("Black's score:", obj.blackPiecesOnBoard)
                print("White's score:", obj.whitePiecesOnBoard)
                print("Black pieces left:", obj.humanPlayerPieceCount)
                print("White pieces left:", obj.computerPlayerPieceCount)
                print("Black's turn")
                print("Enter the row and column of the place where you want to play: ")
                row, column = map(int, input().split())
                check = obj.humanPlay(row, column)
                if check:
                    print("Game Ended")
                    break
            else:
                print("no moves for black")
                obj.switchTurns()
                obj.display()
                if not obj.isThereAValidMove():
                    if obj.blackPiecesOnBoard > obj.whitePiecesOnBoard:
                        print("human player won")
                    elif obj.blackPiecesOnBoard < obj.whitePiecesOnBoard:
                        print("computer Player won")
                    else:
                        print("The Game Is A Draw")
                    break
                print("Black's score:", obj.blackPiecesOnBoard)
                print("White's score:", obj.whitePiecesOnBoard)
                print("Black pieces left:", obj.humanPlayerPieceCount)
                print("White pieces left:", obj.computerPlayerPieceCount)
                print("white's turn")
                check = obj.computerPlay()
                if check:
                    print("Game Ended")
                    break
        else:
            obj.display()
            if obj.isThereAValidMove():
                print("Black's score:", obj.blackPiecesOnBoard)
                print("White's score:", obj.whitePiecesOnBoard)
                print("Black pieces left:", obj.humanPlayerPieceCount)
                print("White pieces left:", obj.computerPlayerPieceCount)
                print("white's turn")
                check = obj.computerPlay()
                if check:
                    print("Game Ended")
                    break
            else:
                print("no moves for white")
                obj.switchTurns()
                obj.display()
                if not obj.isThereAValidMove():
                    if obj.blackPiecesOnBoard > obj.whitePiecesOnBoard:
                        print("human player won")
                    elif obj.blackPiecesOnBoard < obj.whitePiecesOnBoard:
                        print("computer Player won")
                    else:
                        print("The Game Is A Draw")
                    break
                print("Black's score:", obj.blackPiecesOnBoard)
                print("White's score:", obj.whitePiecesOnBoard)
                print("black's turn")
                print("Enter the row and column of the place where you want to play: ")
                row, column = map(int, input().split())
                check = obj.humanPlay(row, column)
                if check:
                    print("Game Ended")
                    break


if __name__ == "__main__":
    main()
