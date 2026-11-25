
"""BewegungsLabor – Grafische Darstellung (statisches Grundlayout)."""

import py5
from motion import SIMULATION_DURATION, TRACK_LENGTH


# Fenster und Layout
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 680
MARGIN = 24
GAP = 16
PADDING = 20
HEADER_HEIGHT = 76
PANEL_RADIUS = 12
BUTTON_RADIUS = 7
LEFT_WIDTH = 784
RIGHT_WIDTH = WINDOW_WIDTH - 2 * MARGIN - GAP - LEFT_WIDTH
LEFT_X = MARGIN
RIGHT_X = LEFT_X + LEFT_WIDTH + GAP
CONTENT_Y = HEADER_HEIGHT + GAP

# Bereiche: (x, y, Breite, Höhe)
HEADER_PANEL = (0, 0, WINDOW_WIDTH, HEADER_HEIGHT)
TRACK_PANEL = (LEFT_X, CONTENT_Y, LEFT_WIDTH, 166)
DIAGRAM_Y = TRACK_PANEL[1] + TRACK_PANEL[3] + GAP
DIAGRAM_PANEL = (LEFT_X, DIAGRAM_Y, LEFT_WIDTH,
                 WINDOW_HEIGHT - MARGIN - DIAGRAM_Y)
SELECTION_PANEL = (RIGHT_X, CONTENT_Y, RIGHT_WIDTH, 196)
CONTROLS_PANEL = (RIGHT_X, SELECTION_PANEL[1] + SELECTION_PANEL[3] + GAP,
                  RIGHT_WIDTH, 100)
MEASUREMENTS_PANEL = (RIGHT_X, CONTROLS_PANEL[1] + CONTROLS_PANEL[3] + GAP,
                      RIGHT_WIDTH, 132)
COMPARISON_Y = MEASUREMENTS_PANEL[1] + MEASUREMENTS_PANEL[3] + GAP
COMPARISON_PANEL = (RIGHT_X, COMPARISON_Y, RIGHT_WIDTH,
                    WINDOW_HEIGHT - MARGIN - COMPARISON_Y)

# Farben (RGB)
COLOR_BACKGROUND = (241, 245, 249)
COLOR_PANEL = (255, 255, 255)
COLOR_HEADER = (23, 44, 67)
COLOR_TEXT = (51, 65, 85)
COLOR_TEXT_SECONDARY = (100, 116, 139)
COLOR_TEXT_LIGHT = (255, 255, 255)
COLOR_HEADER_SUBTITLE = (203, 213, 225)
COLOR_BORDER = (213, 222, 232)
COLOR_GRID = (226, 232, 240)
COLOR_AXIS = COLOR_TEXT
COLOR_TRACK = (203, 213, 225)
COLOR_DISABLED = (226, 232, 240)
COLOR_DISABLED_TEXT = COLOR_TEXT_SECONDARY
COLOR_SELECTED = (237, 244, 252)
COLOR_MEASUREMENT = COLOR_BACKGROUND

MOTION_COLORS = {
    "uniform": (37, 99, 184),
    "accelerated": (22, 129, 107),
    "decelerated": (192, 96, 22),
}
MOTION_LABELS = {
    "uniform": "Gleichförmig",
    "accelerated": "Gleichmässig beschleunigt",
    "decelerated": "Gleichmässig verzögert",
}

# Typografie
FONT_NAME = "Arial"
FONT_NAME_BOLD = "Arial Bold"
FONT_TITLE = 29
FONT_SUBTITLE = 17
FONT_SECTION = 21
FONT_BUTTON = 17
FONT_LABEL = 16
FONT_SMALL = 14
FONT_VALUE = 28
font_regular = None
font_bold = None

# Strecke und Diagramm
TRACK_START_X = TRACK_PANEL[0] + 48
TRACK_END_X = TRACK_PANEL[0] + TRACK_PANEL[2] - 48
TRACK_Y = TRACK_PANEL[1] + 91
OBJECT_DIAMETER = 26
PLOT_LEFT = DIAGRAM_PANEL[0] + 70
PLOT_RIGHT = DIAGRAM_PANEL[0] + DIAGRAM_PANEL[2] - 42
PLOT_TOP = DIAGRAM_PANEL[1] + 75
PLOT_BOTTOM = DIAGRAM_PANEL[1] + DIAGRAM_PANEL[3] - 64
TIME_TICK_STEP = 1
DISTANCE_TICK_STEP = 10

# Schaltflächen
BUTTON_INSET = 18
BUTTON_GAP = 6
SELECTION_BUTTON_HEIGHT = 40
MOTION_BUTTONS = {}
for index, motion_key in enumerate(MOTION_LABELS):
    MOTION_BUTTONS[motion_key] = (
        SELECTION_PANEL[0] + BUTTON_INSET,
        SELECTION_PANEL[1] + 43 + index * (SELECTION_BUTTON_HEIGHT + BUTTON_GAP),
        SELECTION_PANEL[2] - 2 * BUTTON_INSET,
        SELECTION_BUTTON_HEIGHT,
    )
START_BUTTON = (CONTROLS_PANEL[0] + BUTTON_INSET,
                CONTROLS_PANEL[1] + 44, 190, 39)
RESET_BUTTON = (START_BUTTON[0] + START_BUTTON[2] + 10,
                START_BUTTON[1], CONTROLS_PANEL[2] - 2 * BUTTON_INSET - 200,
                START_BUTTON[3])
COMPARE_BUTTON = (COMPARISON_PANEL[0] + BUTTON_INSET,
                  COMPARISON_PANEL[1] + 38,
                  COMPARISON_PANEL[2] - 2 * BUTTON_INSET, 33)


def init_fonts():
    """Initialisiert die Schriften einmal beim Programmstart."""
    global font_regular, font_bold
    available_fonts = py5.Py5Font.list()
    regular_name = FONT_NAME if FONT_NAME in available_fonts else "SansSerif"
    bold_name = FONT_NAME_BOLD if FONT_NAME_BOLD in available_fonts else "SansSerif.bold"
    font_regular = py5.create_font(regular_name, 32)
    font_bold = py5.create_font(bold_name, 32)


# Wiederverwendbare Zeichenfunktionen

def draw_label(text, x, y, size=FONT_LABEL, color=COLOR_TEXT,
               bold=False, align=py5.LEFT):
    """Zeichnet eine einheitlich formatierte Beschriftung."""
    py5.push_style()
    py5.text_font(font_bold if bold else font_regular, size)
    py5.text_align(align, py5.CENTER)
    py5.fill(*color)
    py5.no_stroke()
    py5.text(text, x, y)
    py5.pop_style()


def draw_box(bounds, fill_color, border_color=None, radius=BUTTON_RADIUS):
    """Zeichnet ein Rechteck mit optionalem Rahmen."""
    x, y, width, height = bounds
    py5.push_style()
    py5.rect_mode(py5.CORNER)
    py5.fill(*fill_color)
    if border_color is None:
        py5.no_stroke()
    else:
        py5.stroke(*border_color)
        py5.stroke_weight(1)
    py5.rect(x, y, width, height, radius)
    py5.pop_style()


def draw_panel(bounds):
    """Zeichnet eine einheitliche Hintergrundfläche."""
    draw_box(bounds, COLOR_PANEL, COLOR_BORDER, PANEL_RADIUS)


def draw_line(x1, y1, x2, y2, color, weight=1):
    """Zeichnet eine Linie mit definierter Farbe und Stärke."""
    py5.push_style()
    py5.stroke(*color)
    py5.stroke_weight(weight)
    py5.line(x1, y1, x2, y2)
    py5.pop_style()


def draw_circle(x, y, diameter, color, border_color=None, border_weight=1):
    """Zeichnet einen Kreis mit optionalem Rahmen."""
    py5.push_style()
    py5.ellipse_mode(py5.CENTER)
    py5.fill(*color)
    if border_color is None:
        py5.no_stroke()
    else:
        py5.stroke(*border_color)
        py5.stroke_weight(border_weight)
    py5.circle(x, y, diameter)
    py5.pop_style()


def draw_section_title(text, bounds):
    x, y, width, height = bounds
    draw_label(text, x + PADDING, y + 25, FONT_SECTION, COLOR_HEADER, bold=True)


def draw_button(label, bounds):
    """Zeichnet eine momentan deaktivierte Schaltfläche."""
    x, y, width, height = bounds
    draw_box(bounds, COLOR_DISABLED, COLOR_BORDER)
    draw_label(label, x + width / 2, y + height / 2,
               FONT_BUTTON, COLOR_DISABLED_TEXT, bold=True, align=py5.CENTER)


# Umrechnung physikalischer Grössen in Bildschirmkoordinaten

def track_to_x(distance_m):
    fraction = distance_m / TRACK_LENGTH
    return TRACK_START_X + fraction * (TRACK_END_X - TRACK_START_X)


def diagram_to_xy(time_s, distance_m):
    x = PLOT_LEFT + time_s / SIMULATION_DURATION * (PLOT_RIGHT - PLOT_LEFT)
    y = PLOT_BOTTOM - distance_m / TRACK_LENGTH * (PLOT_BOTTOM - PLOT_TOP)
    return x, y


# Grafische Bereiche

def draw_header():
    draw_box(HEADER_PANEL, COLOR_HEADER, radius=0)
    draw_label("BewegungsLabor", MARGIN, 25, FONT_TITLE, COLOR_TEXT_LIGHT, bold=True)
    draw_label("Drei Bewegungsarten im Weg-Zeit-Diagramm", MARGIN, 53,
               FONT_SUBTITLE, COLOR_HEADER_SUBTITLE)
    draw_label("NATUR UND TECHNIK", WINDOW_WIDTH - MARGIN, 25,
               FONT_LABEL, COLOR_TEXT_LIGHT, bold=True, align=py5.RIGHT)
    draw_label("Layoutentwurf · Bedienung inaktiv", WINDOW_WIDTH - MARGIN, 51,
               FONT_SMALL, COLOR_HEADER_SUBTITLE, align=py5.RIGHT)


def draw_track():
    """Zeichnet die Strecke und ein statisches Objekt am Start."""
    draw_panel(TRACK_PANEL)
    draw_section_title("Bewegungsstrecke", TRACK_PANEL)
    draw_label(f"Gesamtstrecke: {TRACK_LENGTH:g} m",
               TRACK_PANEL[0] + TRACK_PANEL[2] - PADDING, TRACK_PANEL[1] + 25,
               FONT_SMALL, COLOR_TEXT_SECONDARY, align=py5.RIGHT)
    draw_line(TRACK_START_X, TRACK_Y, TRACK_END_X, TRACK_Y, COLOR_TRACK, 8)
    for distance_m in range(0, int(TRACK_LENGTH) + 1, DISTANCE_TICK_STEP):
        x = track_to_x(distance_m)
        draw_line(x, TRACK_Y + 14, x, TRACK_Y + 22, COLOR_AXIS, 2)
        draw_label(f"{distance_m} m", x, TRACK_Y + 37, FONT_LABEL, align=py5.CENTER)
    draw_label("Start", TRACK_START_X, TRACK_Y - 30, FONT_SMALL, bold=True, align=py5.CENTER)
    draw_label("Ziel", TRACK_END_X, TRACK_Y - 30, FONT_SMALL, bold=True, align=py5.CENTER)
    draw_circle(track_to_x(0), TRACK_Y, OBJECT_DIAMETER,
                MOTION_COLORS["uniform"], COLOR_PANEL, 3)


def draw_diagram():
    """Zeichnet ein leeres Weg-Zeit-Diagramm mit fester Skalierung."""
    draw_panel(DIAGRAM_PANEL)
    draw_section_title("Weg-Zeit-Diagramm", DIAGRAM_PANEL)
    draw_label(f"0–{SIMULATION_DURATION:g} s · 0–{TRACK_LENGTH:g} m",
               DIAGRAM_PANEL[0] + DIAGRAM_PANEL[2] - PADDING, DIAGRAM_PANEL[1] + 25,
               FONT_SMALL, COLOR_TEXT_SECONDARY, align=py5.RIGHT)

    for time_s in range(0, int(SIMULATION_DURATION) + 1, TIME_TICK_STEP):
        x, _ = diagram_to_xy(time_s, 0)
        draw_line(x, PLOT_TOP, x, PLOT_BOTTOM, COLOR_GRID)
        draw_label(str(time_s), x, PLOT_BOTTOM + 18, FONT_SMALL, align=py5.CENTER)
    for distance_m in range(0, int(TRACK_LENGTH) + 1, DISTANCE_TICK_STEP):
        _, y = diagram_to_xy(0, distance_m)
        draw_line(PLOT_LEFT, y, PLOT_RIGHT, y, COLOR_GRID)
        draw_label(str(distance_m), PLOT_LEFT - 13, y, FONT_SMALL, align=py5.RIGHT)

    # Achsen und Pfeilspitzen
    draw_line(PLOT_LEFT, PLOT_TOP - 8, PLOT_LEFT, PLOT_BOTTOM, COLOR_AXIS, 2)
    draw_line(PLOT_LEFT, PLOT_BOTTOM, PLOT_RIGHT + 8, PLOT_BOTTOM, COLOR_AXIS, 2)
    draw_line(PLOT_LEFT - 4, PLOT_TOP, PLOT_LEFT, PLOT_TOP - 8, COLOR_AXIS, 2)
    draw_line(PLOT_LEFT + 4, PLOT_TOP, PLOT_LEFT, PLOT_TOP - 8, COLOR_AXIS, 2)
    draw_line(PLOT_RIGHT, PLOT_BOTTOM - 4, PLOT_RIGHT + 8, PLOT_BOTTOM, COLOR_AXIS, 2)
    draw_line(PLOT_RIGHT, PLOT_BOTTOM + 4, PLOT_RIGHT + 8, PLOT_BOTTOM, COLOR_AXIS, 2)
    draw_label("Weg s (m)", DIAGRAM_PANEL[0] + PADDING, PLOT_TOP - 17, FONT_LABEL, bold=True)
    draw_label("Zeit t (s)", (PLOT_LEFT + PLOT_RIGHT) / 2, PLOT_BOTTOM + 44,
               FONT_LABEL, bold=True, align=py5.CENTER)

    center_x = (PLOT_LEFT + PLOT_RIGHT) / 2
    center_y = (PLOT_TOP + PLOT_BOTTOM) / 2
    draw_label("Hier entsteht das Weg-Zeit-Diagramm.", center_x, center_y - 12,
               19, COLOR_TEXT_SECONDARY, align=py5.CENTER)
    draw_label("Noch kein Bewegungsversuch durchgeführt.", center_x, center_y + 14,
               FONT_SMALL, COLOR_TEXT_SECONDARY, align=py5.CENTER)


def draw_motion_selection():
    draw_panel(SELECTION_PANEL)
    draw_section_title("1 · Bewegungsart", SELECTION_PANEL)
    for motion_key, bounds in MOTION_BUTTONS.items():
        x, y, width, height = bounds
        color = MOTION_COLORS[motion_key]
        selected = motion_key == "uniform"  # Nur statische Vorauswahl
        background = COLOR_SELECTED if selected else COLOR_PANEL
        border = color if selected else COLOR_BORDER
        draw_box(bounds, background, border)
        draw_circle(x + 19, y + height / 2, 14, color)
        draw_label(MOTION_LABELS[motion_key], x + 36, y + height / 2, FONT_LABEL,
                   COLOR_HEADER if selected else COLOR_TEXT, bold=selected)
        radio_x = x + width - 19
        radio_y = y + height / 2
        draw_circle(radio_x, radio_y, 16, background, border, 1.5)
        if selected:
            draw_circle(radio_x, radio_y, 8, color)


def draw_controls():
    draw_panel(CONTROLS_PANEL)
    draw_section_title("2 · Simulation", CONTROLS_PANEL)
    draw_button("Start", START_BUTTON)
    draw_button("Reset", RESET_BUTTON)


def draw_measurements():
    draw_panel(MEASUREMENTS_PANEL)
    draw_section_title("Live-Messwerte", MEASUREMENTS_PANEL)
    measurements = [("Zeit", "s"), ("Weg", "m"), ("Geschw.", "m/s")]
    tile_gap = 8
    tile_width = (MEASUREMENTS_PANEL[2] - 2 * BUTTON_INSET - 2 * tile_gap) / 3
    tile_height = 70
    tile_y = MEASUREMENTS_PANEL[1] + 45
    for index, (label, unit) in enumerate(measurements):
        tile_x = MEASUREMENTS_PANEL[0] + BUTTON_INSET + index * (tile_width + tile_gap)
        center_x = tile_x + tile_width / 2
        draw_box((tile_x, tile_y, tile_width, tile_height), COLOR_MEASUREMENT)
        draw_label(label, center_x, tile_y + 13, FONT_SMALL, align=py5.CENTER)
        draw_label("–", center_x, tile_y + 36, FONT_VALUE, COLOR_HEADER,
                   bold=True, align=py5.CENTER)
        draw_label(unit, center_x, tile_y + 57, FONT_SMALL,
                   COLOR_TEXT_SECONDARY, align=py5.CENTER)


def draw_comparison():
    draw_panel(COMPARISON_PANEL)
    x, y, width, height = COMPARISON_PANEL
    draw_label("3 · Vergleich", x + PADDING, y + 21, 19, COLOR_HEADER, bold=True)
    draw_label("0/3 Versuche", x + width - PADDING, y + 21,
               FONT_SMALL, COLOR_TEXT_SECONDARY, align=py5.RIGHT)
    draw_button("Bewegungen vergleichen", COMPARE_BUTTON)


def draw_layout():
    """Zeichnet die vollständige Benutzeroberfläche."""
    py5.background(*COLOR_BACKGROUND)
    draw_header()
    draw_track()
    draw_diagram()
    draw_motion_selection()
    draw_controls()
    draw_measurements()
    draw_comparison()
