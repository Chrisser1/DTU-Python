def del_a():
    from math import sqrt # Denne regel sørger for at man kan bruge kvadratrod-funktionen sqrt senere

    Re = 3
    Im = -2
    mod = sqrt(Re**2+Im**2)
    print(mod)

def del_b():
    from math import cos, sin, pi #Sørger for man kan bruge funktionerne cos og sin samt cirkelkonstanten pi
    mod = 4
    Arg = pi/3
    Re=mod*cos(Arg)
    Im=mod*sin(Arg)

    print(f"Realdel er {Re} og Imaginærdel er {Im}")

    print(Re==2)

if __name__ == "__main__":
    del_a()
    del_b
