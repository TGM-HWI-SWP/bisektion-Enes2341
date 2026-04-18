

def f(x: float, func_input: str) -> float:
    """
    Diese Funktion berechnet den Funktionswert f(x)
    für die vom Benutzer eingegebene Funktion.

    Beispiel:
    Eingabe: x**2 - 25
    Ausgabe: f(x) = x**2 - 25 an der Stelle x
    """
    return eval(func_input)

def solver2() -> None:

    """
    Diese Funktion bestimmt eine Nullstelle einer Funktion
    mit der Methode der Regula falsi.

    Ablauf:
    1. Funktion eingeben
    2. Startintervall [a, b] eingeben
    3. Prüfen ob Intervall gültig ist
    4. Genauigkeit epsilon bestimmen
    5. Iterativ neue Näherung berechnen
    6. Nullstelle ausgeben
    """

    try:

        print("=== Nullstellen-Solver mit Regula falsi ===")

        # Funktion vom Benutzer eingeben
        func_input = input("Funktion eingeben (z.B. x**2 - 25): ")

        # Startintervall eingeben
        a = float(input("a eingeben: "))
        b = float(input("b eingeben: "))

        # Prüfen ob das Intervall gültig ist
        # Voraussetzung: f(a) * f(b) < 0
        if f(a, func_input) * f(b, func_input) >= 0:
            print("Ungültiges Intervall!")
            return

        # Genauigkeit eingeben (z.B. -4 → epsilon = 10^-4)
        exponent = int(input("Exponent für Genauigkeit eingeben (z.B.10**-4): "))
        epsilon = 10 ** exponent

        # Iteration beginnt
        while True:

            # Funktionswerte berechnen
            fa = f(a, func_input)
            fb = f(b, func_input)

            # Regula-falsi-Formel zur Berechnung der neuen Näherung
            c = b - fb * (b - a) / (fb - fa)

            # Funktionswert an neuer Stelle berechnen
            fc = f(c, func_input)

            # Abbruchbedingung:
            # Wenn Funktionswert nahe genug bei 0 ist → Nullstelle gefunden
            if abs(fc) < epsilon:
                print("Nullstelle gefunden:", c)
                print(f"Endintervall: [{a}, {b}]")
                break

            # Entscheiden welches Teilintervall weiter verwendet wird
            if fa * fc < 0:
                b = c
            else:
                a = c

    except ValueError:
        print("Fehler bei der Eingabe!")

    except Exception as e:
        print("Unbekannter Fehler:", e)



if __name__ == "__main__":
    
    solver2()