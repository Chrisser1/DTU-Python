if __name__ == "__main__":
    a = 6
    m = 7

    x = 1
    y = 1
    while True:
        if a * x > m * y:
            if a * x == m * y + 1:
                break
            else:
                y += 1
        else:
            if x > 10000:
                break
            x += 1

    print(f"x = {x}, y = {y} in ax = ym + 1 -> {a * x} = {y * m + 1}")
