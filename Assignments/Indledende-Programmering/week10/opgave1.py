a: list[int] = []
a.append(1)
a.append(2)
a.append(3)
a.insert(1,4)
a[0] = 5
a.insert(0,0)
a.insert(1,1)
for i, v in enumerate(a):
    print(f"{i}:{v} ", sep="", end="")
