import random

def produce(n):
    return [random.randint(0, 9) for i in range(n)]

def process(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    print(a)

def main():
    for n in range(10):
        process(produce(n))

main()
