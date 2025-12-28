def next_prime(p):
    ''' the prime number that comes after the prime number p '''
    q = p + 1
    while True:
        if is_prime(q):
            return q
        q += 1

def check_next_prime(n):
    ''' Print Correct if n is the next prime
    print Incorrect, game over, if it's not and the game is just over, print Game is over otherwise'''

    global prev_prime, game_over

    if game_over:
        print("Game is over")
        return
    if n == next_prime(prev_prime):
        print("Correct")
        prev_prime = n
    else:
        print("Incorrect, game over")
        game_over = True


check_next_prime(2) # print "Correct"
check_next_prime(3) # print "Correct"
check_next_prime(4) # print "Correct"
check_next_prime(5) # print "Correct"
