"""
BewegungsLabor – Automatisierte Tests.

Überprüft das physikalische Bewegungsmodell anhand
mathematischer Referenzwerte und besonderer Grenzfälle.
"""

import unittest

from motion import MOTIONS, distance, velocity


class TestMotion(unittest.TestCase):

    def assert_motion(self, t, v0, a, expected_s, expected_v):
        """Vergleicht berechneten Weg und Geschwindigkeit."""

        self.assertAlmostEqual(
            distance(t, v0, a), expected_s
        )
        self.assertAlmostEqual(
            velocity(t, v0, a), expected_v
        )

    def test_start(self):
        """Überprüft die Startwerte aller Bewegungsarten."""

        expected = {
            "uniform": 5.0,
            "accelerated": 0.0,
            "decelerated": 10.0,
        }

        for key, expected_v in expected.items():
            with self.subTest(motion=key):
                motion = MOTIONS[key]

                self.assert_motion(
                    0, motion["v0"], motion["a"],
                    0.0, expected_v
                )

    def test_intermediate_values(self):
        """Überprüft die Werte nach 2 und 5 Sekunden."""

        reference_values = [
            ("uniform", 2, 10.0, 5.0),
            ("uniform", 5, 25.0, 5.0),
            ("accelerated", 2, 2.0, 2.0),
            ("accelerated", 5, 12.5, 5.0),
            ("decelerated", 2, 18.0, 8.0),
            ("decelerated", 5, 37.5, 5.0),
        ]

        for key, t, expected_s, expected_v in reference_values:
            with self.subTest(motion=key, time=t):
                motion = MOTIONS[key]

                self.assert_motion(
                    t, motion["v0"], motion["a"],
                    expected_s, expected_v
                )

    def test_end(self):
        """Alle Bewegungen erreichen nach 10 s genau 50 m."""

        expected = {
            "uniform": 5.0,
            "accelerated": 10.0,
            "decelerated": 0.0,
        }

        for key, expected_v in expected.items():
            with self.subTest(motion=key):
                motion = MOTIONS[key]

                self.assert_motion(
                    10, motion["v0"], motion["a"],
                    50.0, expected_v
                )

    def test_early_stop(self):
        """Ein Objekt bleibt nach dem Abbremsen stehen."""

        # Vor dem Stillstand
        self.assert_motion(2, 6, -2, 8.0, 2.0)

        # Genau beim Stillstand
        self.assert_motion(3, 6, -2, 9.0, 0.0)

        # Nach dem Stillstand
        self.assert_motion(5, 6, -2, 9.0, 0.0)
        self.assert_motion(10, 6, -2, 9.0, 0.0)

    def test_initially_stationary(self):
        """Ein stehendes Objekt bewegt sich nicht rückwärts."""

        self.assert_motion(5, 0, -1, 0.0, 0.0)
        self.assert_motion(5, 0, 0, 0.0, 0.0)

    def test_negative_time(self):
        """Negative Zeit wird als Startzeit behandelt."""

        self.assert_motion(-2, 5, 0, 0.0, 5.0)
        self.assert_motion(-2, 0, 1, 0.0, 0.0)
        self.assert_motion(-2, 10, -1, 0.0, 10.0)

    def test_negative_initial_velocity(self):
        """Negative Anfangsgeschwindigkeiten sind unzulässig."""

        with self.assertRaises(ValueError):
            distance(5, -1, 0)

        with self.assertRaises(ValueError):
            velocity(5, -1, 0)

    def test_extended_duration(self):
        """Das Bewegungsmodell ist nicht auf 10 s begrenzt."""

        self.assert_motion(12, 5, 0, 60.0, 5.0)
        self.assert_motion(12, 0, 1, 72.0, 12.0)
        self.assert_motion(12, 10, -1, 50.0, 0.0)


if __name__ == "__main__":
    unittest.main()
