import math
from typing import Any

def f1(n: int):
    if (n <= 1):
        print(n, sep="", end="")
    else:
        f1(n / 2)
        print(f", {n}", sep="", end="")

def opgave1():
    print("Opgave 1:")
    for n in 1,2,3,4,16,30,100:
            print("f1(", n, "): ", sep="", end="")
            f1(n)
            print()

def f2(n: int):
    if n > 100:
        print(n, sep="", end="")
    else:
        f2(2 * n)
        print(f", {n}", sep="", end="")

def opgave2():
    print("Opgave 2:")
    for n in 113, 70, 42, 30, 10:
        print("f2(", n, "): ", sep="", end="")
        f2(n)
        print()

def f3(n: int):
    if n <= 0:
        print("*", sep="", end="")
    elif n % 2 == 0:
        print("(", sep="", end="")
        f3(n-1)
        print(")", sep="", end="")
    else:
        print("[", sep="", end="")
        f3(n-1)
        print("]", sep="", end="")

def opgave3():
    print("Opgave 3:")
    for n in 0, 1, 2, 3, 4, 5:
        print("f3(", n, "): ", sep="", end="")
        f3(n)
        print()

def process(a: list[Any]):
    length = len(a)

    if length <= 1:
        return a
    else:
        b = a[math.floor(length / 2):]
        b.extend(process(a[:math.ceil(length / 2)]))
        return b

def opgave4():
    print("Opgave 4:")
    print(process([1,2,3,4,5,6,7]))

def next_fib(a: list[int]) -> list[int]:
    l = len(a)

    if l <= 1:
        return a
    else:
        a.append(a[l-1] + a[l-2])
        return a

def opgave5():
    print("Opgave 5:")
    a = [0,1]
    for i in range(50):
        a = next_fib(a)
    print(a)

if __name__ == "__main__":
    opgave1()
    opgave2()
    opgave3()
    opgave4()
    opgave5()
