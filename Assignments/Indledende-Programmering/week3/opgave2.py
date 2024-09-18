def printPersonAndStair(stair_number: int, total_stairs: int):
    spaces_before: str = ((total_stairs - stair_number - 1) * 5) * " "
    spaces_after: str = ((stair_number + 1) * 5) * " "

    print(spaces_before + " " * 2 + "o" + " " * 2 + "*" * 6 + " " * (stair_number * 5) + "*")
    print(spaces_before + " /|\\ " + "*" + spaces_after + "*")
    print(spaces_before + " / \\ " + "*" + spaces_after + "*")

def printStairs(total_stairs: int):
    for i in range(total_stairs):
        printPersonAndStair(i, total_stairs)
    print("*" * ((total_stairs + 1) * 5) + "**")

if __name__ == "__main__":
    printStairs(5)
