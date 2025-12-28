"""# solving the n! trailing zeros problem
# building the password

# n! = 1x2x....xn
# want the number of trailing zeros
# n! = 0^k * x, find k

def num_factors(n, k):
    return the number of times that n has a factor of k
    count = 0
    while n % k == 0:
        n = n // k
        count = count + 1
    return count

def trailing_zeros(n):
    count_factors5 = 0
    for i in range(1, n+1):
        count_factors5 = count_factors5 + num_factors(i, 5)


def trailing_zeros_faster(n):
    count_factors5 = 0
    skip_by = 5
    while skip_by <= n:
        count_factors5 += n // skip_by   
        skip_by *= 5
    return count_factors5     

# 1 x 2 x 3 x 4 x 5...x 10 x 15 x ... 25 x ... 625 x ...
#                 1     1      1       2        4
#                                      1        2
#                                               1
#                                               1


if __name__ == '__main__':
    print(trailing_zeros(15))
    # print(num_factors(4, 5)) # 0
    # print(num_factors(5, 5)) # 1
    # print(num_factors(3 * 17 * 5 * 100, 5)) # 100"""

def check_password(username, password):
    if username not in usernames:
        return False # login failed
    return passwords[usernames.index(username)] == password

    #if username.index(usernames) == passwords.index(username.index(usernames)):
        #return True

def login(username, password):
    global failed_attempts
    if failed_attempts >= 3:
        print("You have been locked out")
        return False

    if check_password(username, password):
        failed_attempts = 0
        print("You have successfully logged in")
        return True
    
    else:
        failed_attempts += 1
        print("Please try again")
        return False
    
def initialize():
    global usernames, passwords, failed_attempts
    usernames = ["guerzhoy", "carrick", "yip",]
    passwords = ["sjfd*@#$!", "DIVERGING!!!", "UOFT#1"]
    failed_attempts = 0



if __name__ == '__main__':
# the passwords for usernames[i] is passwords[i]
    initialize()
    login("guerzhoy", "sjfd*@#$!") # True
    login("yip", "UOFT#2") # False
    login("yip", "waterloo#200") # False
    login("yip", "COFFEE") # False
    login("yip", "UOFT#1") # false even if UOFT#1 is correct password because too many tries