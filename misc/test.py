# The program must print the lines given in the file main.txt

# The function play(s, n) takes the initial string with cells alive
# and the number of iterations, but must stop if no cells are alive

# The function show(a) takes a list of lists as printed in main.txt
# where the initial string with cells alive are placed from index 0

def main():
    print("Welcome to One-Dimensional Game of Life")
    print()
    for s in "* **", "* ***", "******", "*******":
        a = play(s, len(s) ** 2)
        print("List length", len(a))
        for x in a:
            print(x)
        print()
        show(a)
        print()
    print("Shows Flipflop, Glider, Spider and Face")


# The above lines for the function main() must not be changed

def play(s, n): # Plays n iterations of One-Dimensional Game of Life, with starting string 's'.
    # Converts 's' into list of positions of living cells. Ex: "* *" -> [0,2]
    currentList = []
    for i in range(len(s)):
        if s[i] == "*":
            currentList.append(i)

    finalListArray = [[]] # Initializing return-list containing iterations as lists.
    finalListArray[0] = currentList # Adding list for n=1 to returned list.

    for i in range(n-1): # Running n-1 iterations, since n=1 is already in returned list.
        nextList = []
        # Finding the span of indexes we need to run through to find next iteration.
        startingIndex = currentList[0] - 2
        endingIndex = currentList[len(currentList) - 1] + 2
        # Runs through every index we want to investigate.
        for j in range(startingIndex, endingIndex+1):
            neighborCount = 0
            for k in range(j-2, j+3): # Runs through current j's neighbors. Adds k as neighbor if cell is alive.
                if k in currentList and k != j:
                    neighborCount += 1
            # Rules to define whether the next iteration should have living cell on index j.
            if (neighborCount == 2 or neighborCount == 3) and j not in currentList: # Should cell be born?
                nextList.append(j)
            elif (neighborCount == 2 or neighborCount == 4) and j in currentList: # Should living cell stay alive?
                nextList.append(j)

        if len(nextList) == 0: # If next iteration has no living cells, return result
            return finalListArray

        # Adds a copy of non-empty next iteration to returned list, and continues loop with new iteration as input.
        finalListArray.append(nextList.copy())
        currentList = nextList.copy()

    return finalListArray

def show(a): # Function that displays lists of living cells on specific indexes.
    # Finding min and max indexes to define width of display.
    minIndex = 0
    maxIndex = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] < minIndex:
                minIndex = a[i][j]
            if a[i][j] > maxIndex:
                maxIndex = a[i][j]

    # Runs through all iterations from played game.
    for i in range(len(a)):
        s = ""
        # Runs through indexes of each iteration
        for j in range(minIndex, maxIndex+1):
            # Adds '*' to our string if index contains living cell, and a space if not.
            if j in a[i]:
                s += "*"
            else:
                s += " "
        print(s)

main()
