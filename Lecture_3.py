my_input = int(input("Prompt: "))
x = my_input + 1
print(x)
print("hello test \ test")
print("ESC", 180) #prints string and then an integer with a space inbetween


def  f(x): # x is a parameter: local variable
    x = 2
    y = 5 # y is definted inside the function
    x=2
    print(x) # 2

x = 42 # global x
f(x)
print(x) # 42

# the local x (in a function) overshadows the global x.
# a parameter cannot be global

def add_course():
    global num_courses
    num_courses = num_courses + 1

def drop_course():
    global num_courses
    num_courses = num_courses - 1

def print_acorn_transcript():
    print("Number of courses", num_courses)
    if num_courses == -2:
        print("WELCOME TO INDY")


if __name__ == '__main__': # what does this do?
    num_courses = 0
    add_course()
    print(num_courses)
    drop_course()
    print_acorn_transcript()
