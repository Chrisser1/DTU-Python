def drawTopOrBottom(width: int):
    print("+" + ("-" * width) + "+")

def drawMiddle(height: int, width: int):
    length: int = (int) (height / 2)
    for i in range(length + 2):
        spaces = (" " * i)
        dots = "*" * (width - i * 2)
        print("|" + spaces + "\\" + dots + "/" + spaces + "|")

    for i in reversed(range(length + 2)):
        spaces = (" " * i)
        dots = "*" * (width - i * 2)
        print("|" + spaces + "/" + dots + "\\" + spaces + "|")

def printHourglass(size):
    drawTopOrBottom(width=size)
    drawMiddle(height=size - 4, width=size - 2)
    drawTopOrBottom(width=size)

if __name__ == "__main__":
    printHourglass(100)
