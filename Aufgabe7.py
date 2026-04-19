import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def plotter():



    def f(x: float) -> float:
        """
        Diese Funktion wertet die eingegebene Funktion an der Stelle x aus.
        """
        return eval(func_input)


    func_input = input("Funktion eingeben (z.B. x**2 - 1): ")               #Funktion eingeben

    a = float(input("a eingeben: "))                                        #Anfangsintervall eingeben
    b = float(input("b eingeben: "))                                        #Endintervall eingeben


    # Prüfen ob Intervall gültig ist
    if f(a) * f(b) >= 0:
        print("Ungültiges Intervall!")
        raise SystemExit()

    exponent = int(input("Genauigkeit eingeben (Exponent für 10^x): "))     #Exponent eingeben
    epsilon = 10 ** exponent                                                #Genauigkeit berechnen

    # Listen für die Animation
    a_werte = []
    b_werte = []
    c_werte = []
    fc_werte = []

    while True:

        c = (a + b) / 2
        fc = f(c)

        # Werte für spätere Animation speichern
        a_werte.append(a)
        b_werte.append(b)
        c_werte.append(c)
        fc_werte.append(abs(fc))

        # richtige Abbruchbedingung
        if abs(fc) < epsilon:                           #wenn der Funktionswert von c kleiner als epsilon ist, dann ist c eine Nullstelle
            print("Nullstelle gefunden:", c)            #Nullstelle gefunden
            print(f"Endintervall: [{a}, {b}]")          #Endintervall ausgeben
            break

        if f(a) * fc < 0:                               #wenn funktion von a und von c zusammen multipliziert negativ ist,
            b = c                                       #dann wird b zu c, sonst wird a zu c
        else:
            a = c


    # ---------------- MATPLOTLIB-TEIL ----------------

    # Bereich für den Funktionsgraphen erstellen
    # Hier werden x-Werte zwischen dem ersten a und b erzeugt
    x = np.linspace(a_werte[0], b_werte[0], 1000)


    y = [f(xi) for xi in x]     # Funktionswerte berechnen


    # Zwei Diagramme nebeneinander erstellen:
    # links: Funktionsgraph + Intervall
    # rechts: Textfeld mit Iterationsinformationen
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    ax1 = axs[0]   # Funktion + Intervall
    ax2 = axs[1]   # Textfeld



    ax2.axis("off")     # Rechtes Diagramm deaktivieren (kein Koordinatensystem sichtbar)

    # Textfeld für Iterationsinformationen erstellen
    # Position: 10% von links, 50% von unten
    text_box = ax2.text(0.1, 0.5, "", fontsize=12)


    ax1.plot(x, y, label="f(x)")        # Funktionsgraph zeichnen

    # x-Achse (Null-Linie) einzeichnen
    ax1.axhline(0, color="black", linewidth=1)

    # Beschriftungen setzen
    ax1.set_title("Intervallhalbierung")
    ax1.set_xlabel("x")
    ax1.set_ylabel("f(x)")


    # Punkt für aktuellen Mittelpunkt c vorbereiten (wird animiert)
    punkt_c, = ax1.plot([], [], "*", markersize=10, color="red")

    # Linie für aktuelles Intervall [a,b]
    intervall_linien, = ax1.plot([], [], "o-", color="green", markersize=3)


    def update(frame):
        """
        Aktualisiert die Animation für jeden Iterationsschritt.

        Parameter:
        frame : int
            Aktuelle Iterationsnummer der Intervallhalbierung.

        Funktion:
        - zeigt aktuelles Intervall [a,b]
        - zeigt aktuellen Mittelpunkt c
        - aktualisiert das Textfeld mit Iterationswerten
        """

        # Aktuelle Werte aus gespeicherten Listen holen
        a_now = a_werte[frame]
        b_now = b_werte[frame]
        c_now = c_werte[frame]
        fc_now = f(c_now)


        # Intervall [a,b] im Graph darstellen
        intervall_linien.set_data([a_now, b_now],[f(a_now), f(b_now)])

        # Mittelpunkt c im Graph darstellen
        punkt_c.set_data([c_now], [fc_now])


        # Textfeld mit aktuellen Iterationsdaten aktualisieren
        text_box.set_text(
            f"Iteration: {frame + 1}\n"
            f"a = {a_now:.9f}\n"
            f"b = {b_now:.9f}\n"
            f"c = {c_now:.9f}\n"
            f"|f(c)| = {abs(fc_now):.6e}"
        )


        
        return punkt_c, intervall_linien, text_box      # Rückgabe der aktualisierten Objekte für matplotlib



    ani = FuncAnimation(                    # Animation starten
        fig,
        update,
        frames=len(c_werte),   # Anzahl Iterationen
        interval=800,          # Zeit zwischen Frames in ms
        repeat=False           # Animation nur einmal abspielen
    )

    plt.show()      # Animation anzeigen


if __name__ == "__main__":
    
    plotter()