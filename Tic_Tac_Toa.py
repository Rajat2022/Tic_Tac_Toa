winner = None
table = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
print("-=" * 20)
print("WELCOME TO GAME 'TIC - TAC - TOE'")
print("-=" * 20)


def display_table():
    print(table[0][0] + " | " + table[0][1] + " | " + table[0][2])
    print(table[1][0] + " | " + table[1][1] + " | " + table[1][2])
    print(table[2][0] + " | " + table[2][1] + " | " + table[2][2])


def check_tie():
    if any("_" in sublist for sublist in table):
        pass
    else:
        print("Game Tie...")
        return


def check_rows():
    row_1 = table[0][0] == table[0][1] == table[0][2] != "_"
    row_2 = table[1][0] == table[1][1] == table[1][2] != "_"
    row_3 = table[2][0] == table[2][1] == table[2][2] != "_"

    if row_1:
        return table[0][0]
    elif row_2:
        return table[1][0]
    elif row_3:
        return table[2][0]

    return


def check_columns():
    column_1 = table[0][0] == table[1][0] == table[2][0] != "_"
    column_2 = table[0][1] == table[1][1] == table[2][1] != "_"
    column_3 = table[0][2] == table[1][2] == table[2][2] != "_"

    if column_1:
        return table[0][0]
    elif column_2:
        return table[0][1]
    elif column_3:
        return table[0][2]

    return


def check_diagonals():
    diagonal_1 = table[0][0] == table[1][1] == table[2][2] != "_"
    diagonal_2 = table[2][0] == table[1][1] == table[0][2] != "_"

    if diagonal_1:
        return table[0][0]
    elif diagonal_2:
        return table[2][0]

    return


def check_winner():
    global winner
    row_winner = check_rows()

    column_winner = check_columns()

    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return


def check_game():
    check_winner()
    check_tie()


# def players(player):
#     print()
#     print(f"{player} play your game.")


def positions(symbols, row, column):
    if [row, column] not in [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]:
        print()
        print("invalid input try again")
        positions(symbols, row, column)

    else:
        if table[row][column] == "_":
            table[row][column] = symbols
            print()
            display_table()

        else:
            print()
            print("invalid position please enter correct position")
            positions(symbols, row, column)


def play_game(symbols, row, column):
    # players(player_name)
    print()
    positions(symbols, row, column)


def player_details(player1, symbol1, player2, symbol2):
    print()
    display_table()
    print()
    check_game()

    if winner == symbol1:
        print(f"{player1} won... the GAME ")
    if winner == symbol2:
        print(f"{player2} won... the Game")

    return winner
