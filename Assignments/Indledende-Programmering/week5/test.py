def isInRange(number, min_val, max_val) -> bool:
    if min_val is None and max_val is not None:
        return number <= max_val
    if max_val is None and min_val is not None:
        return number >= min_val
    if min_val is None and max_val is None:
        return True
    return min_val <= number <= max_val


def getValidUserInputInt(min_val: int = None, max_val: int = None) -> int:
    if min_val is None and max_val is not None:
        ask_for = f"Please input a number in range (-infinity, {max_val}]: "
    elif max_val is None and min_val is not None:
        ask_for = f"Please input a number in range [{min_val}, infinity): "
    elif max_val is None and min_val is None:
        ask_for = "Please input any number: "
    else:
        ask_for = f"Please input a number in range [{min_val}, {max_val}]: "

    while True:
        try:
            number = int(input(ask_for))
            if isInRange(number, min_val, max_val):
                return number
            else:
                print(f"The number {number} is out of range.")
        except ValueError:
            print("Invalid input, please enter a valid integer.")

if __name__ == "__main__":
    value: int = getValidUserInputInt(min_val=1, max_val=100)
    print(f"Valid input received: {value}")

    values = [123.123,12,312,3,123]

    for i, j in enumerate(values):
        print(f"index = {i}, value = {j}")
