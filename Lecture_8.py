# how many zeros at the end of n!

# n! = 1x2x3...xn

def fact(n):
    res = 1
    for i in range(2, n+1):
        res = res * i
    return res

def trailing_zeros(n):
    """returns how many zeros there are at the end of n!"""
    fact_n = fact(n)

    # keep diving fact_n by 10 while fact_n is divisble by 10
    # keep track of how many iterations it took to make fact_n not divisble by 10 (i.e., no 0 at the end)

    count = 0
    while fact_n % 10 == 0:
        fact_n = fact_n // 10
        count = count + 1

    return count

        # count: the number of times that we divided fact_n by 10

print(trailing_zeros(100000))
