def selection_sort(L):
    #k = len(L)-1
    for k in range(len(L) - 1, 0, -1): # counting down the list of L
        loc_max = 0
        cur_max = L[0] # local max = 10
        for j in range(1, k+1): #From 1 to end of list
            if L[j] > cur_max: # Finds biggest number in that adjusted list 
                cur_max = L[j]
                loc_max = j
        L[k], L[loc_max] = L[loc_max], L[k]

L =  [10, 2, 10.0, 1000, 0, -1]
# cur_max = 10, loc_max = 0
# k = 5
# j = 1
# L[5], L[loc_max] = L[loc_max], L[k]
# so, 
selection_sort(L)
print(L)
        