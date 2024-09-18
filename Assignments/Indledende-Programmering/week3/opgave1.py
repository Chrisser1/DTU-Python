import math

def printStuff():
    SECOND_LINE = "|| "+ str(math.pi) +" ||"
    print("/" * len(SECOND_LINE))
    print(SECOND_LINE)
    print("\\" * len(SECOND_LINE))

if __name__ == "__main__":
    printStuff()
