def f(x: float, func_input: str) -> float:
    """
    Diese Funktion wertet die eingegebene Funktion an der Stelle x aus.
    """
    return eval(func_input)


def solver():

    func_input = input("Funktion eingeben (z.B. x**2 - 1): ")

    a = float(input("a eingeben: "))
    b = float(input("b eingeben: "))

    # Prüfen ob Intervall gültig ist
    if f(a, func_input) * f(b, func_input) >= 0:
        print("Ungültiges Intervall!")
        raise SystemExit()

    exponent = int(input("Genauigkeit eingeben (Exponent für 10^x): "))
    epsilon = 10 ** exponent

    while True:

        c = (a + b) / 2
        fc = f(c, func_input)

        if abs(fc) < epsilon:
            print("Nullstelle gefunden:", c)
            print(f"Endintervall: [{a}, {b}]")
            break

        if f(a, func_input) * fc < 0:
            b = c
        else:
            a = c


if __name__ == "__main__":
    solver()