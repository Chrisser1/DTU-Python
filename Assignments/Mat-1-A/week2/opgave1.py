def a() -> str:
    a: list = {1,2,3}
    b: list = {1,2,3}
    c: list = {1,1,2}
    d: list = {1,2}

    ab: bool = a == b
    cd: bool = c == d
    answer = f"a is equal to b is {ab}, and c is equal to d is {cd}"
    return answer

def b() -> str:
    A={9, 12, 15, 21, 24, 27, 30, 33, 36, 42, 48, 51, 54, 57, 60, 63, 66, 69, 72, 78, 81, 84, 87, 90, 93, 96}
    B={12, 16, 24, 28, 32, 36, 48, 52, 56, 60, 64, 68, 72, 80, 84, 88, 92, 96}

    answer = f"len(A) = {len(A)} \n len(B) = {len(B)}. \n Len means the amount of elements, len(A) would in the mathematical sense be written as |A|"
    return answer

def c() -> str:
    A={9, 12, 15, 21, 24, 27, 30, 33, 36, 42, 48, 51, 54, 57, 60, 63, 66, 69, 72, 78, 81, 84, 87, 90, 93, 96}
    B={12, 16, 24, 28, 32, 36, 48, 52, 56, 60, 64, 68, 72, 80, 84, 88, 92, 96}

    answer = f"A.union(B) = {A.union(B)} \n A.intersection(B) = {A.intersection(B)}"
    return answer

def d() -> str:
    A={9, 12, 15, 21, 24, 27, 30, 33, 36, 42, 48, 51, 54, 57, 60, 63, 66, 69, 72, 78, 81, 84, 87, 90, 93, 96}
    B={12, 16, 24, 28, 32, 36, 48, 52, 56, 60, 64, 68, 72, 80, 84, 88, 92, 96}

    A_union_B = A.union(B)
    A_intersection_B = A.intersection(B)
    answer = f"""
    Left side: \n
    A ∪ B = {A_union_B} \n
    |A ∪ B| = {len(A_union_B)} \n
    \n
    Right side: \n
    |A| = {len(A)} \n
    |B| = {len(B)} \n
    A ∩ B = {A_intersection_B} \n
    |A ∩ B| = {len(A_intersection_B)} \n
    |A| + |B| - |A ∩ B| = {len(A) + len(B) - len(A_intersection_B)}
    """

    return answer

def e():
    A={9, 12, 15, 21, 24, 27, 30, 33, 36, 42, 48, 51, 54, 57, 60, 63, 66, 69, 72, 78, 81, 84, 87, 90, 93, 96}
    B={12, 16, 24, 28, 32, 36, 48, 52, 56, 60, 64, 68, 72, 80, 84, 88, 92, 96}
    C={6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96}

    calculation = ((len(A) + len(B) + len(C)) - len(A.intersection(B)) - len(A.intersection(C)) - len(B.intersection(C)) + len(A.intersection(B).intersection(C)))
    answer = f"""
    |A ∪ B ∪ C| = {len(A.union(B).union(C))}

    |A| = {len(A)}
    |B| = {len(B)}
    |C| = {len(C)}
    |A ∩ B| = {len(A.intersection(B))}
    |A ∩ C| = {len(A.intersection(C))}
    |A ∩ B| = {len(B.intersection(C))}
    |A ∩ B ∩ C| = {len(A.intersection(B).intersection(C))}

    |A ∪ B ∪ C| = |A| + |B| + |C| - |A ∩ B| - |A ∩ C | - |B ∩ C| + |A ∩ B ∩ C| = {calculation}
    """
    return answer

if __name__ == "__main__":
    print("Spørgsmål  a:\n", a(), "\n")
    print("Spørgsmål  b:\n", b(), "\n")
    print("Spørgsmål  c:\n", c(), "\n")
    print("Spørgsmål  d:\n", d(), "\n")
    print("Spørgsmål  e:\n", e(), "\n")
