# a, b = 45, 120 # a = 45, b = 120
# b, a = a, b # a = 120, b = 45
# temp = a # temp = 120
# a = b # a = 45
# b = temp # b = 120
# a = a + b # a == old_a + old_b , b == old_b
# b = a - b # a == old_a + oldb, b = old_a
# a = a - b # a == old_b, b == old_a 

# def adding(x):
#     x = x + 5
#     return x

# test = 1
# y = adding(test)
# print(y)

for i in range(1, 100):
    if 11 <= i <= 13:
        print("I'm telling you for the", i, "-th time.", "ENGSCI ROCKS")
    elif i % 3 == 0 and (i != 6 and i != 9):
        print("I'm telling you for the", i, "-rd time.", "ENGSCI ROCKS")
    elif i % 10 == 1:
        print("I'm telling you for the", i, "-nd time.", "ENGSCI ROCKS")
    elif i % 10 == 2:
        print("I'm telling you for the", i, "-st time.", "ENGSCI ROCKS")
    else:
        print("I'm telling you for the", i, "-th time.", "ENGSCI ROCKS")

