def bubble_sort(L):
    swapped = False
    k = len(L)
    while not swapped:
        swapped = False
        for i in range(len(L) - 1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                swapped = True
        k -= 1

        
