def get_adjusted_grade(grade):
    grade = grade - 5
    return grade

if __name__ == "__main__":
    grade = 95 # global grade is 95
    print(get_adjusted_grade(grade))
    print("New grade outside the function:", grade)


# Swapping vlaues of variables

# Task:

a = 5
b = 6

# want a to have the old value of b, and b to have the old value of a

temp = a # temp == 5, a == 6, b = 6
a = b    # temp == 5, a == 6, b = 6 
b = temp # temp == 5, a == 6, b = 5

# Python - specific technique: multiple assignment

a, b = 5, 6 # the same as a = 5 and b =6 at the same time
a, b = b, a

# Just for fun:
# How to swap the value of two ints
# without a temporary variable and without multiple assignment 

a = a + b
b = a