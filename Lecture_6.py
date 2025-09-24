"""
def is_prime(n):
    if n  == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2): # try i = 3, 5, 7, 9, since divisible by 4 is also just divisble by 2
        if n % 1 == 0: # is n divisible by i?
            return False
        
# if n = a*b
# then it can't be the case that a > sqrt(n) and b > sqrt(n)
# (beause then n = a*b > sqrt(n))^2 = n, but that can't be. QED)
# if you can factorize n, tone of the factors will be < = sqrt (n)
        

if __name__ == '__main__':
    # n % i == 0 if i is a division of n
    # (when computing n divide by i, n % i is the remainder)
    # n is prime if it has no divisors other than itself and 1
    print(is_prime(5))

    """
# while <cond>:
    # <block>


i = 0
n = 5
while i < n:
    print(i) # print 0, 1, 2, 3, 5
    i = i + 1 # i = 1, i = 2, i = 3, i = 4, i = 5
# start with i = 0, increment i by 1 every time, stop when it stops being the case that i < 5