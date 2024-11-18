def main():
    a = []
    for i in range(0, 5):
        x = [i] * i
        a.append(x)
    for x in a:
        print(x)
    print()
    print("List length", len(a))
main()
