# Write a Python program to find three numbers from an array such that the sum of three numbers 
# equal to zero. Input : [-1,0,1,2,-1,-4] Output : [[-1, -1, 2], [-1, 0, 1]] Note : Find the unique 
# triplets in the array.

arr = [-1,0,1,2,-1,-4]

def sum_zero(arr):
    z= 0
    y = []
    sorted_y1 = ()
    for idx_i, i in enumerate(arr):

        for idx_j, j in enumerate(arr):
            if (idx_i != idx_j):
                z = i + j
                
                for idx_k, k in enumerate(arr):
                    if (idx_k != idx_j) and (idx_k != idx_i):
                        x = z + k
                        if x == 0:
                            sorted_y1 = tuple(sorted((i, j, k)))
                            if sorted_y1 not in y:
                                y.append(sorted_y1)
    return y

print(sum_zero(arr))