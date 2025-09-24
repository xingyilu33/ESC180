"""L = [141, 115, 121]
     
L[2]
L[0]

for e in L:
    print(e)
len(L) # the number ofe lements in L


salaries = [141, 115, 121]
majors = ["Aero", "Biomed", "ECE"]

# Print majors with corresponding salaries
# major[0]: salaries[0]"""

salaries = [141, 115, 121]
majors = ["Aero", "Biomed", "ECE"]

def print_salaries(majors, salaries):
    for i in range(len(majors)): # i = 0, 1, 2
        print(majors[i], ":", salaries[i])

print_salaries(majors, salaries)

#negative indexing

L = [141, 115, 121]
print(L[len(L)-1]) # incidces: -, 1, 2, 3, ...., len(L)-1
print(L[-1]) # the last element of L
print(L[-2]) # the second last element of L