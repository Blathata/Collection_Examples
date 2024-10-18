
p = root

v = [p]


while v:
    vn = []
    for x in v:
        print(x.data)
        if x.left:
            vn += [x.left]
        if x.right:
            vn += [x.right]
    v = vn

