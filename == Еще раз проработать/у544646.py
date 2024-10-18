
recived_boxs = [2, 2, 4, 3, 5, 6, 0, 9, 8, 7, 7] 
pattern = [2, 4, 3, 5, 6, 0,]

res = list(int(i) for i in recived_boxs if i not in pattern)


print(res)