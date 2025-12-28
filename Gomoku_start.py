"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 16, 2025
"""

def is_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != " ":
                return False
    return True


def is_bounded(board, y_end, x_end, length, d_y, d_x):
    # first we should try and form what we think the actual sequence looks like (reverse the process)
    # then we should check the ends:
    # if there are two openings, then OPEN
    # if one opening, then SEMI OPEN
    # if no openings, then CLOSED
    # we also need to be aware of the borders
    end_check = [(y_end + d_y), (x_end + d_x)]
    start_check = [y_end - (d_y * length), x_end - (d_x * length)]

    end_open = is_space_in_board(end_check[0], end_check[1], board) and board[end_check[0]][end_check[1]] == " "
    start_open = is_space_in_board(start_check[0], start_check[1], board) and board[start_check[0]][start_check[1]] == " "

    if start_open and end_open:
        return "OPEN"
    elif start_open or end_open:
        return "SEMIOPEN"
    else:
        return "CLOSED"


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    length_counter = 0
    open_seq_count = 0
    semi_open_seq_count = 0
    
    while is_space_in_board(y_start, x_start, board):
        if board[y_start][x_start] == col:
            while is_space_in_board(y_start, x_start, board) and board[y_start][x_start] == col:
                length_counter += 1
                y_start += d_y
                x_start += d_x
            if length_counter == length:
                if is_bounded(board, y_start-d_y, x_start-d_x, length_counter, d_y, d_x) == "OPEN":
                    open_seq_count += 1

                elif is_bounded(board, y_start-d_y, x_start-d_x, length_counter, d_y, d_x) == "SEMIOPEN":
                    semi_open_seq_count += 1
            
            length_counter = 0
        
        y_start += d_y
        x_start += d_x

    return open_seq_count, semi_open_seq_count

    # Start a loop
    # Start at y_start and x_start
    # if colour != colour:
    # y_start + d_y and x_start + d_x
    # if colour == colour:
    # Start a Length counter = 1
    # move in direction d_y, d_x
    # If the next stone is colour col
    # add one to length.
    # check when it stops
    # Check if length = length:
    # Check if is_bounded = open
    # open_seq_count += 1
    # Check if is_bounded = semi
    # semi_open_seq_count += 1
    # new y_start and x_start is ending spot

def detect_row_closed(board, col, y_start, x_start, length, d_y, d_x):
    length_counter = 0
    closed_seq_count = 0
    
    while is_space_in_board(y_start, x_start, board):
        if board[y_start][x_start] == col:
            while is_space_in_board(y_start, x_start, board) and board[y_start][x_start] == col:
                length_counter += 1
                y_start += d_y
                x_start += d_x
            if length_counter == length:
                if is_bounded(board, y_start-d_y, x_start-d_x, length_counter, d_y, d_x) == "CLOSED":
                    closed_seq_count += 1
            
            length_counter = 0
        
        y_start += d_y
        x_start += d_x

    return closed_seq_count

def detect_rows_closed(board, col, length):
    closed_seq_count = 0
    for i in range(len(board)): #row by row
        closed_additions = detect_row_closed(board, col, i, 0, length, 0, 1)
        closed_seq_count += closed_additions

    for i in range(len(board)): #column by column
        closed_additions = detect_row_closed(board, col, 0, i, length, 1, 0)
        closed_seq_count += closed_additions

    for i in range(len(board)): #0,0 diagonals (down and right) down the columns
        closed_additions = detect_row_closed(board, col, 0, i, length, 1, 1)
        closed_seq_count += closed_additions

    for i in range(1, len(board)): #1,0 diagonals (down and right) down the rows
        closed_additions = detect_row_closed(board, col, i, 0, length, 1, 1)
        closed_seq_count += closed_additions

    for i in range(len(board)): #0,0 diagonals up to the right
        closed_additions = detect_row_closed(board, col, len(board)-(i+1), 0, length, -1, 1)
        closed_seq_count += closed_additions
            
    for i in range(len(board)-1): #0,0 diagonals up to the right
        closed_additions = detect_row_closed(board, col, len(board)-1, i+1, length, -1, 1)
        closed_seq_count += closed_additions

    return closed_seq_count

def detect_rows(board, col, length):
    # have to go down each row, go down each column, and do all of the diagonals
    # start a for loop all the way to the end of the board
    # start at 0,0 --> do detect row all the way down --> it returns open_seq_count and semi_open_seq_count so we add htem
    # then start at 1,0 -- > detect row all the way down
    # general case: start at i, 0 --> detect row all the way down 
    open_seq_count, semi_open_seq_count = 0, 0
    for i in range(len(board)): #row by row
       open_additions, semi_additions = detect_row(board, col, i, 0, length, 0, 1)
       open_seq_count += open_additions
       semi_open_seq_count += semi_additions

    for i in range(len(board)): #column by column
        open_additions, semi_additions = detect_row(board, col, 0, i, length, 1, 0)
        open_seq_count += open_additions
        semi_open_seq_count += semi_additions

    for i in range(len(board)): #0,0 diagonals (down and right) down the columns
        open_additions, semi_additions = detect_row(board, col, 0, i, length, 1, 1)
        open_seq_count += open_additions
        semi_open_seq_count += semi_additions

    for i in range(1, len(board)): #1,0 diagonals (down and right) down the rows
        open_additions, semi_additions = detect_row(board, col, i, 0, length, 1, 1)
        open_seq_count += open_additions
        semi_open_seq_count += semi_additions

    for i in range(len(board)): #0,0 diagonals up to the right
        open_additions, semi_additions = detect_row(board, col, len(board)-(i+1), 0, length, -1, 1)
        open_seq_count += open_additions
        semi_open_seq_count += semi_additions
        
    for i in range(len(board)-1): #0,0 diagonals up to the right
        open_additions, semi_additions = detect_row(board, col, len(board)-1, i+1, length, -1, 1)
        open_seq_count += open_additions
        semi_open_seq_count += semi_additions   

    return open_seq_count, semi_open_seq_count

def search_max(board):
    # same as tictactoe
    # for i in range(whatever)
    # make every possible move
    # find best one
    # return best one
    move_y = move_x = None
    best = -99999999999999999999999999999999999999999
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == " ":
                board[i][j] = "b"
                points = score(board)
                if best < points:
                    best = points
                    move_y, move_x = i, j
                board[i][j] = " "

    return move_y, move_x

def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def is_win(board):
   
   #Have to consider different conditions:
    # White won:
    white_open, white_semi = detect_rows(board, "w", 5)
    white_closed = detect_rows_closed(board, "w", 5)
    black_open, black_semi = detect_rows(board, "b", 5)
    black_closed = detect_rows_closed(board, "b", 5)
    if white_open >= 1 or white_semi >= 1 or white_closed>= 1:
        return "White won"
    if black_open >= 1 or black_semi >= 1 or black_closed >=1:
        return "Black won"
    
    else:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == " ":
                    return "Continue playing"

    return "Draw" 
    # White has 5 in a row
    #detect_rows(board, "w", , 5)
    # Black won:
    # Black has 5 in a row
    # detect rows same
    # Draw:
    # There are no playable moves
    # Continue Playing:
    # Return this at the end if nothing else in the past has stuck yet

    #For draw:
    # check every space on the board.
    # If 


def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board



def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))


def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res





        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res


def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x

def is_sequence_complete(board, col, y_start, x_start, length, d_y, d_x):

    # make sure that it's actually the length
    # make sure that it's the right colour
    # make sure that it starts at the right spot
    # make sure that there's no overflow off the board
    # check extra spacing so length is actually length
    # check if outside of board cuz then we don't care

    for i in range(length):
        if not is_space_in_board(y_start, x_start, board):
            return False
        if board[y_start][x_start] != col:
            return False
        y_start += d_y
        x_start += d_x
        #check the end
    if is_space_in_board(y_start, x_start, board):
        if board[y_start][x_start] == col:
            return False
        #check the start
    y_starting = y_start-((length+1)*d_y) # is the length+1 necessary here?
    x_starting = x_start-((length+1)*d_x)

    if is_space_in_board(y_starting, x_starting, board):
        if board[y_starting][x_starting] == col:
            return False

    return True


def is_space_in_board(y, x, board):
    if 0 <= x < len(board[0]):
        if 0 <= y < len(board):
            return True

    return False


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0




if __name__ == '__main__':
    # ---------- tiny helpers ----------
    def show(result, name):
        print(f"{name}: {'PASS' if result else 'FAIL'}")

    def fresh(sz=8):
        return make_empty_board(sz)

    # ---------- tests for is_empty ----------
    def t_is_empty():
        b = fresh(5)
        show(is_empty(b) is True, "is_empty on fresh board")
        b[2][3] = "b"
        show(is_empty(b) is False, "is_empty after one stone")

    # ---------- tests for is_bounded ----------
    def t_is_bounded():
        # OPEN: vertical "bbb" with empty both ends
        b = fresh(8)
        put_seq_on_board(b, 2, 4, 1, 0, 3, "b")         # y=2..4, x=4
        res = is_bounded(b, 4, 4, 3, 1, 0)
        show(res == "OPEN", "is_bounded OPEN middle")

        # CLOSED at border: vertical "www" touching top
        b = fresh(8)
        put_seq_on_board(b, 0, 3, 1, 0, 3, "w")         # starts at top edge
        res = is_bounded(b, 2, 3, 3, 1, 0)
        show(res == "CLOSED", "is_bounded CLOSED at border")

        # SEMIOPEN: horizontal "www" with one side blocked by other color
        b = fresh(8)
        put_seq_on_board(b, 5, 2, 0, 1, 3, "w")         # (5,2..4)
        b[5][1] = "b"                                   # block before
        res = is_bounded(b, 5, 4, 3, 0, 1)
        show(res == "SEMIOPEN", "is_bounded SEMIOPEN one side blocked")

        # CLOSED: both sides blocked
        b = fresh(8)
        put_seq_on_board(b, 3, 3, 0, 1, 2, "w")         # (3,3..4)
        b[3][2] = "b"; b[3][5] = "b"
        res = is_bounded(b, 3, 4, 2, 0, 1)
        show(res == "CLOSED", "is_bounded CLOSED both sides blocked")

    # ---------- tests for detect_row ----------
    def t_detect_row():
        # Exact length only, start on an edge as per spec
        # One open run of length 3 along a row from the left edge
        b = fresh(8)
        put_seq_on_board(b, 3, 2, 0, 1, 3, "w")         # (3,2..4)
        open_c, semi_c = detect_row(b, "w", 3, 0, 3, 0, 1)  # scan row 3 left-to-right
        show((open_c, semi_c) == (1, 0), "detect_row one open length-3")

        # A 4-long should not be counted when looking for 3
        b = fresh(8)
        put_seq_on_board(b, 1, 1, 0, 1, 4, "w")
        open_c, semi_c = detect_row(b, "w", 1, 0, 3, 0, 1)
        show((open_c, semi_c) == (0, 0), "detect_row exact length only")

        # Edge makes sequences closed under your is_bounded
        b = fresh(8)
        put_seq_on_board(b, 0, 5, 1, 0, 3, "b")         # touches top edge
        open_c, semi_c = detect_row(b, "b", 0, 5, 3, 1, 0)
        show((open_c, semi_c) == (0, 0), "detect_row closed at edge not counted open/semi")

    # ---------- tests for detect_rows ----------
    def t_detect_rows():
        b = fresh(8)
        # One horizontal open 3
        put_seq_on_board(b, 2, 2, 0, 1, 3, "w")
        # One vertical semi-open 3: block one side with black
        put_seq_on_board(b, 4, 5, 1, 0, 3, "w")         # (4,5..6,5)
        b[7][5] = "b"                                   # block bottom
        open_c, semi_c = detect_rows(b, "w", 3)
        show(open_c >= 1, "detect_rows finds at least one open 3")
        show(semi_c >= 1, "detect_rows finds at least one semi-open 3")

        b2 = fresh(5)
        show(detect_rows(b2, "b", 2) == (0, 0), "detect_rows zero on empty board")

    # ---------- tests for score ----------
    def t_score():
        # Black five is max
        b = fresh(10)
        put_seq_on_board(b, 5, 2, 0, 1, 5, "b")
        show(score(b) == 100000, "score max on black five")

        # White five is min
        b = fresh(10)
        put_seq_on_board(b, 0, 0, 1, 1, 5, "w")
        show(score(b) == -100000, "score min on white five")

        # Blocking a white open four should improve score
        b = fresh(8)
        put_seq_on_board(b, 3, 1, 0, 1, 4, "w")         # white threat
        s1 = score(b)
        b[3][5] = "b"                                   # block after end
        s2 = score(b)
        show(s2 > s1, "score improves after blocking white threat")

    # ---------- tests for search_max ----------
    def t_search_max():
        # Create a unique winning spot by using the border
        b = fresh(8)
        put_seq_on_board(b, 4, 0, 0, 1, 4, "b")         # (4,0..3)
        # Only (4,4) completes five
        y, x = search_max(b)
        show((y, x) == (4, 4), "search_max chooses immediate win")

        # Board must be unchanged
        unchanged = all(
            b[4][j] == ("b" if 0 <= j <= 3 else " ")
            for j in range(8)
        )
        show(unchanged, "search_max does not modify board")

        # Should block a white open four at either end
        b = fresh(8)
        put_seq_on_board(b, 3, 2, 0, 1, 4, "w")         # (3,2..5)
        y, x = search_max(b)
        show((y, x) in {(3, 1), (3, 6)}, "search_max blocks white open four")

    # ---------- tests for is_win ----------
    def t_is_win():
        # Black win
        b = fresh(10)
        put_seq_on_board(b, 5, 1, 0, 1, 5, "b")
        show(is_win(b) == "Black won", "is_win black win")

        # White win
        b = fresh(10)
        put_seq_on_board(b, 0, 0, 1, 1, 5, "w")
        show(is_win(b) == "White won", "is_win white win")

        # Draw on a full small board with no five
        b = [
            list("bwb"),
            list("wbw"),
            list("bwb"),
        ]
        show(is_win(b) == "Draw", "is_win draw on full board")

        # Continue playing
        b = fresh(5)
        b[0][0] = "b"
        show(is_win(b) == "Continue playing", "is_win continue")

    # ---------- optional sanity checks for I/O functions ----------
    def t_print_and_analysis():
        b = fresh(3)
        b[0][1] = "b"; b[2][2] = "w"
        print("Grid preview below should show one b and one w:")
        print_board(b)
        print("Analysis preview:")
        analysis(b)

    # ---------- run all ----------
    print("Running assignment tests...\n")
    t_is_empty()
    t_is_bounded()
    t_detect_row()
    t_detect_rows()
    t_score()
    t_search_max()
    t_is_win()
    # You can comment this out if you want quieter output
    # t_print_and_analysis()
    print("\nDone.")

