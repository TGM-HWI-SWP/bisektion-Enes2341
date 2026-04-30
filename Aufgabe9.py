import math  # für sinh() und cosh()

def solve_aufg9():
    def f(x: float) -> float:
        return eval(func_input)  # wertet eingegebene Funktion an Stelle x aus

    func_input = input("Funktion eingeben (z.B. x**2 - 1): ")  # Funktion eingeben
    a = float(input("a eingeben: "))  # Startintervall
    b = float(input("b eingeben: "))  # Endintervall

    if f(a) * f(b) >= 0:  # prüft Vorzeichenwechsel im Intervall
        print("Ungültiges Intervall!")
        raise SystemExit()

    exponent = int(input("Genauigkeit eingeben (Exponent für 10^x): "))  # Genauigkeit festlegen
    epsilon = 10 ** exponent  # berechnet epsilon

    while True:
        c = (a + b) / 2  # Intervallmitte berechnen (Bisektion)
        fc = f(c)  # Funktionswert an Stelle c

        if abs(fc) < epsilon:  # Abbruchbedingung erreicht
            
            print("Krümmungsradius:", c)  # gefundene Nullstelle = Radius
            print(f"Endintervall: [{a}, {b}]")
            
            a = c  # speichert Radius für Längenberechnung
            
            l = 2 * a * math.sinh(100 / (2 * a))  # Seillänge berechnen
            
            print("Die länge der Leitung ist:", l)
            break

        if f(a) * fc < 0:  # Nullstelle liegt im linken Teilintervall
            b = c
        else:
            a = c  # sonst im rechten Teilintervall

#===========================================================

#  x*math.cosh(50/x) - x - 10                   #Formel

#===========================================================
if __name__ == "__main__":
    solve_aufg9()

        

