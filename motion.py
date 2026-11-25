"""
BewegungsLabor – Physikalisches Bewegungsmodell.

Enthält die Bewegungsparameter und die physikalischen
Berechnungen der Simulation.
"""

# Gemeinsame Simulationsparameter (SI-Einheiten)
SIMULATION_DURATION = 10.0  # Sekunden
TRACK_LENGTH = 50.0         # Meter
START_POSITION = 0.0        # Meter


# Zentrale Datenstruktur der drei Bewegungsarten
MOTIONS = {
    "uniform": {
        "name": "Gleichförmige Bewegung",
        "v0": 5.0,
        "a": 0.0,
    },
    "accelerated": {
        "name": "Gleichmässig beschleunigte Bewegung",
        "v0": 0.0,
        "a": 1.0,
    },
    "decelerated": {
        "name": "Gleichmässig verzögerte Bewegung",
        "v0": 10.0,
        "a": -1.0,
    },
}


def effective_time(t, v0, a):
    """Begrenzt die Bewegungszeit bei einem Stillstand."""

    if v0 < 0:
        raise ValueError("Anfangsgeschwindigkeit darf nicht negativ sein.")

    # Negative Zeitwerte verhindern
    t = max(0.0, t)

    # Bei Verzögerung die Zeit bis zum Stillstand begrenzen
    if a < 0:
        stop_time = -v0 / a
        t = min(t, stop_time)

    return t


def distance(t, v0, a):
    """Berechnet den zurückgelegten Weg in Metern."""

    t = effective_time(t, v0, a)

    return v0 * t + 0.5 * a * t ** 2


def velocity(t, v0, a):
    """Berechnet die momentane Geschwindigkeit in m/s."""

    t = effective_time(t, v0, a)

    return max(0.0, v0 + a * t)
