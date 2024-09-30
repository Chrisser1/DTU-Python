def is_number(s):
    try:
        i = int(s)
        return i >= 0
    except ValueError:
        return False

def get_number(prompt):
    s = input(prompt)
    while not is_number(s):
        s = input(prompt)
    return int(s)

def trekant(a, b, c):
    if a == b and b == c:
        print(f"Trekant {a} {b} {c} er ligesidet")
    elif a == b or a == c or c == b:
        print(f"Trekant {a} {b} {c} er ligebenet")
    else:
        print(f"Trekant {a} {b} {c} er hverken ligesidet eller ligebenet")

def main():
    a = get_number("Længde af 1. side? ")
    b = get_number("Længde af 2. side? ")
    c = get_number("Længde af 3. side? ")
    trekant(a, b, c)

main()
