def rotate_90(key):
    n = len(key)
    m = len(key[0])
    result = [[0]*n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            result[j][n-1-i] = key[i][j]

    return result

def check(new_lock):
    n = len(new_lock)//3
    
    for i in range(n,2*n):
        for j in range(n,2*n):
            if new_lock[i][j]!=1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]
    
    for rotation in range(4):
        key = rotate_90(key)
        
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]+=key[i][j]
                if check(new_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    
    return False