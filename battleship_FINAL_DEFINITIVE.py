logo = """\
         ____        __  __  __          __    _
        / __ )____ _/ /_/ /_/ /__  _____/ /_  (_)___
       / __  / __ `/ __/ __/ / _ \/ ___/ __ \/ / __  )
      / /_/ / /_/ / /_/ /_/ /  __(__  ) / / / / /_/ /
     /_____/\__,_/\__/\__/_/\___/____/_/ /_/_/ .___/
                                            /_/ """
import random
import time


def clear():
    for i in range(240):
        print("")


def board_creation(board):
    for i in range(12):
        board.append(["~"] * 11)


def placing(board_back, playerUI, game_mode):
    ship_length = 2
    print ("\033[31m" + logo + "\033[0m")
    print ("\033[5m" + "        PLAYER {} TURN:".format(playerUI))
    print_board(board_back)
    if game_mode == "multi":
        auto = input("      Do You want auto placement? Y/N     ")
        if auto == "Y" or auto == "y":
            auto = "auto"
    while ship_length < 6:
        ship_length_check = 0
        print ("\033[31m" + logo + "\033[0m")
        print ("\033[5m" + "        PLAYER {} TURN:".format(playerUI))
        print_board(board_back)
        while abs(ship_length_check) + 1 != ship_length:
            print("        PLACE A {} LONG SHIP".format(ship_length))
            try:
                if game_mode == "multi" and auto != "auto":
                    ship_row_start = int(input("        STARTING HORIZONTAL COORDINATE? ")) - 1
                    ship_col_start = int(input("        STARTING VERTICAL COORDINATE? ")) - 1
                    ship_row_end = int(input("        ENDING HORIZONTAL COORDINATE? ")) - 1
                    ship_col_end = int(input("        ENDING VERTICAL COORDINATE? ")) - 1
                    ship_row = ship_row_start
                    ship_col = ship_col_start
                elif game_mode == "single" or auto == "auto":
                    ship_row_start = random.randrange(0, 10)
                    ship_col_start = random.randrange(0, 10)
                    random_num = random.randrange(0, 2)
                    if random_num == 1:
                        ship_row_end = ship_row_start
                        ship_col_end = ship_col_start + ship_length - 1
                    elif random_num == 0:
                        ship_row_end = ship_row_start + ship_length - 1
                        ship_col_end = ship_col_start
                    ship_row = ship_row_start
                    ship_col = ship_col_start
                if (ship_col_start and ship_row_start and ship_col_end and ship_row_end and ship_row and ship_col) in range(10):
                    ship_length_check = (ship_row_start - ship_row_end) + (ship_col_start - ship_col_end)
                    if abs(ship_length_check) + 1 == ship_length:
                        if placing_ships(
                                ship_row_start,
                                ship_col_start,
                                ship_row_end,
                                ship_col_end,
                                ship_row,
                                ship_col,
                                ship_length,
                                board_back) == -2:
                            continue
                        else:
                            ship_length = ship_length + 1
                            break
                    else:
                        print("        WRONG SHIP LENGTH")
                        continue
                else:
                    print("        SHIP OUT OF RANGE")
                    continue
            except ValueError:
                print("        ONLY INTEGERS (1-10) CAN BE GUESSED")
                continue
        clear()
    print_board(board_back)


def placing_ships(
        ship_row_start,
        ship_col_start,
        ship_row_end,
        ship_col_end,
        ship_row,
        ship_col,
        ship_length,
        board_back):
    if ship_row_start == ship_row_end:
        for i in range(ship_length):
            if board_back[ship_row][ship_col] == "~":
                if ship_col < ship_col_end:
                    ship_col = ship_col + 1
                    if i == ship_length - 1:
                        ship_length = draw_row(
                            ship_row_start,
                            ship_col_start,
                            ship_length,
                            board_back,
                            "vertical",
                            ship_col_start,
                            ship_col_end)
                else:
                    ship_col = ship_col - 1
                    if i == ship_length - 1:
                        ship_length = draw_row(
                            ship_row_start,
                            ship_col_start,
                            ship_length,
                            board_back,
                            "vertical",
                            ship_col_start,
                            ship_col_end)
            else:
                print("        YOU ALREADY PLACED A SHIP THERE")
                return -2
    elif ship_col_start == ship_col_end:
        for i in range(ship_length):
            if board_back[ship_row][ship_col] == "~":
                if ship_row < ship_row_end:
                    ship_row = ship_row + 1
                    if i == ship_length - 1:
                        ship_length = draw_row(
                            ship_row_start,
                            ship_col_start,
                            ship_length,
                            board_back,
                            "horizontal",
                            ship_row_start,
                            ship_row_end)
                else:
                    ship_row = ship_row - 1
                    if i == ship_length - 1:
                        ship_length = draw_row(
                            ship_row_start,
                            ship_col_start,
                            ship_length,
                            board_back,
                            "horizontal",
                            ship_row_start,
                            ship_row_end)
            else:
                print("        YOU ALREADY PLACED A SHIP THERE")
                return -2
    else:
        return -2


def draw_row(ship_row_start, ship_col_start, ship_length, board_back, direction, start, end):
    ship_row = ship_row_start
    ship_col = ship_col_start
    for i in range(ship_length):
        if direction == "vertical":
            board_back[ship_row][start] = "#"
        elif direction == "horizontal":
            board_back[start][ship_col] = "#"
        if start < end:
            start = start + 1
        else:
            start = start - 1
    return ship_length + 1


def print_board(board):
    print ("")
    for i in range(10):
        board[i][10] = "  " + str(i + 1)
    for i in range(10):
        board[10][i] = ""
    for i in range(10):
        board[10][i] = str(i + 1)
    board[10][10] = ""
    board[11][10] = ""
    for i in range(10):
        board[11][i] = ""
    print ("")
    for row in board:
        temp_row = row[:]
        for i, item in enumerate(temp_row):
            if item == "~":
                temp_row[i] = "\033[0;34m" + item + "\033[0m"
            elif item == "#":
                temp_row[i] = "\033[0;31m" + item + "\033[0m"

        print ("        ", "   ".join(temp_row))
        print ("")


def shooting(board_back, board, game_mode):
    try:
        if game_mode == "multi":
            guess_row = int(input("        GUESS HORIZONTAL COORDINATE: ")) - 1
            guess_col = int(input("        GUESS VERTICAL COORDINATE: ")) - 1
        elif game_mode == "single":
            guess_row = random.randrange(0, 10)
            guess_col = random.randrange(0, 10)
            while board[guess_row][guess_col] != "~":
                guess_row = random.randrange(0, 10)
                guess_col = random.randrange(0, 10)
            difficulty = random.randrange(0, 3)
            if difficulty == 0:
                while board[guess_row][guess_col] != "~" or board_back[guess_row][guess_col] != "#":
                    guess_row = random.randrange(0, 10)
                    guess_col = random.randrange(0, 10)

        if (guess_row < 0 or guess_row > 9) or \
                (guess_col < 0 or guess_col > 9):
            print ("        THAT SPOT IS NOT ON THE BOARD, TRY AGAIN")
            return -2

        elif board[guess_row][guess_col] == "X":
            print ("        YOU GUESSED THAT ONE ALREADY")
            return -2

        elif board[guess_row][guess_col] == "#":
            print ("        YOU GUESSED THAT ONE ALREADY")
            return -2

        elif board_back[guess_row][guess_col] == "#":
            print ("        YOU HIT A BATTLESHIP")
            board[guess_row][guess_col] = "#"
            return -3

        elif board[guess_row][guess_col] == "~":
            print ("        YOU SHOT IN THE OCEAN")
            board[guess_row][guess_col] = "X"
            return -1

    except ValueError:
        print("        ONLY INTEGERS (1-10) CAN BE GUESSED")
        return -2


def battle_phase(board, board_back, player, game_mode):
    print ("\033[31m" + logo + "\033[0m")
    print ("")
    print("\033[5m" + "        TIME TO SHOOT {}!".format(player))
    print_board(board)
    if game_mode == "multi":
        whattodo = shooting(board_back, board, "multi")
    else:
        whattodo = shooting(board_back, board, "single")
    if whattodo == -2:
        return -2
    elif whattodo == -1:
        return -1
    elif whattodo == -3:
        return -3


def exit_game():
    clear()
    dotlist = []
    import time
    for i in range(0,9):
        clear()
        output = ("\033[93m" + "               FORMATTING C DRIVE" + "".join(dotlist) + "\033[0m")
        print(output)
        dotlist.extend(".")
        time.sleep(0.4)
    print ("\033[93m" + "               Ooops, something went wrong!" + "\033[0m")
    print ("")
    exit()


def game(game_mode):
    clear()
    board = []
    board_2 = []
    board_back = []
    board_back_2 = []
    board_creation(board)
    board_creation(board_2)
    board_creation(board_back)
    board_creation(board_back_2)

    placing(board_back, 1, "multi")
    clear()
    if game_mode == "multi":
        placing(board_back_2, 2, "multi")
    else:
        placing(board_back_2, 2, "single")

    win_player1 = 0
    win_player2 = 0
    turn = 100
    while win_player1 < 14 and win_player2 < 14:
        clear()
        if turn % 2 == 0:
            whattodo = battle_phase(board, board_back_2, "PLAYER 1", "multi")
            if whattodo == - 2:
                print ("")
                print ("        NEXT TURN IN 2 SECONDS...")
                time.sleep(2)
                continue
            elif whattodo == - 1:
                turn -= 1
                print ("        NEXT TURN IN 2 SECONDS...")
                time.sleep(2)
                continue
            elif whattodo == -3:
                win_player1 += 1
                print ("        NEXT TURN IN 2 SECONDS...")
                time.sleep(2)
                continue

        else:
            if game_mode == "multi":
                whattodo = battle_phase(board_2, board_back, "PLAYER 2", "multi")
            elif game_mode == "single":
                whattodo = battle_phase(board_2, board_back, "PLAYER 2", "single")
            if whattodo == - 2:
                print ("        NEXT TURN IN 2 SECONDS...")
                time.sleep(2)
                continue
            elif whattodo == - 1:
                print ("        NEXT TURN IN 2 SECONDS...")
                time.sleep(2)
                turn -= 1
                continue
            elif whattodo == -3:
                print ("        NEXT TURN IN 2 SECONDS...")
                time.sleep(2)
                win_player2 += 1
                continue

    if win_player1 == 14:
        clear()
        print ("\033[31m" + logo + "\033[0m")
        print_board(board)
        print ("\033[31m" + "               PLAYER 1 WINS!!!" + "\033[0m")
        print("")
    else:
        clear()
        print ("\033[31m" + logo + "\033[0m")
        print_board(board_2)
        print ("\033[31m" + "               PLAYER 2 WINS!!!" + "\033[0m")
        print("")

def credits():
    clear()
    print ("")
    print ("\033[1m" + "\033[31m" + logo + "\033[0m")
    print ("        CREATED BY:")
    print ("")
    print ("            DANIEL FLACH")
    print ("")
    print ("            MATE SZUMMER")
    print ("")
    print ("            DAVID FERENCZ")
    print ("")
    print ("                    CODECOOL")
    print ("                        2017")
    print ("")
    goback = input("        WANT TO GO BACK TO THE MENU? (Y/N): ")
    if goback == "Y" or goback == "y":
        main()
    if goback == "N" or goback == "n":
        exit_game()
    else:
        credits()


def main():
    try:
        clear()
        print ("")
        print ("\033[1m" + "         Welcome to" + "\033[0m")
        print ("\033[1;31m" + logo + "\033[0m")
        print ("\033[1m" + "                         CODECOOL 2017 (c)" + "\033[0m")
        print ("")
        print ("\033[1m" + "            MENU" + "\033[0m")
        print ("")
        print ("        \033[1m(1)\033[0m" + " SINGLEPLAYER")
        print ("")
        print ("        \033[1m(2)\033[0m" + " MULTIPLAYER")
        print ("")
        print ("        \033[1m(3)\033[0m" + " CREDITS")
        print ("")
        print ("        \033[1m(4)\033[0m" + " EXIT")
        print ("")
        menu = (input("\033[1m" + "        (X) " + "\033[5m" + "INPUT: " + "\033[0m"))
        if menu == "1":
            game("single")
        elif menu == "2":
            game("multi")
        elif menu == "3":
            credits()
        elif menu == "4":
            exit_game()
        else:
            exit_game()
    except KeyboardInterrupt:
        inf = 0
        while inf == 0:
            try:
                exit_game()
            except KeyboardInterrupt:
                continue


main()
