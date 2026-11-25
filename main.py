
"""
BewegungsLabor
Drei Bewegungsarten im Weg-Zeit-Diagramm

main.py übernimmt die Programmsteuerung,
Zeitmessung, Zustandsverwaltung und Benutzerinteraktion.
"""

import py5
import visualization as vis


def settings():
    """Legt die Fenstergrösse fest."""
    py5.size(vis.WINDOW_WIDTH, vis.WINDOW_HEIGHT)


def setup():
    """Initialisiert die Applikation."""
    py5.window_title("BewegungsLabor")
    vis.init_fonts()
    py5.frame_rate(30)


def draw():
    """Zeichnet die Benutzeroberfläche."""
    vis.draw_layout()


if __name__ == "__main__":
    py5.run_sketch()
