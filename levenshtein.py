import numpy as np
def lev_ratio_and_dist(s, t, lev_ratio = False):
    r = len(s)+1
    c = len(t)+1
    dist_mat = np.zeros((r,c),dtype = int)
    for i in range(1, r):
        for k in range(1,c):
            dist_mat[i][0] = i
            dist_mat[0][k] = k
            
    for row in range(1,r):
        for col in range(1,c):
            if s[row-1] == t[col-1]:
               cost = 0
            else:
                if(lev_ratio == True):
                    cost = 2
                else:
                    cost = 1
            dist_mat[row][col] = min(dist_mat[row-1][col]+1,
                                     dist_mat[row][col-1] +1,
                                     dist_mat[row-1][col-1]+cost)
    if lev_ratio == True:
        ratio = ((r+c-2) - dist_mat[row][col])/(r+c-2)
    else:
        ratio = -1

    return (dist_mat[row][col], ratio)

