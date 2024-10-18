s =[[1, 0, 0, 0, 0], 
    [0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 1, 0, 1, 0], 
    [0, 0, 0, 0, 0]
    ]

def is_isolate(*args):
    return sum(args)

def verify(lst_in):
    for v in range(len(s[0])-1):
        for c in range(len(s)-1):
            if is_isolate(s[v][c], s[v][c+1], s[v+1][0], s[v+1][c+1]) > 1:
            # if s[v][c] + s[v][c+1] + s[v+1][0] + s[v+1][c+1] > 1:
                return False
    return True
print(verify(s))
