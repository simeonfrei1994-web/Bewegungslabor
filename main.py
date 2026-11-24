
import py5


def setup():
    py5.size(800, 500)
    py5.window_title("BewegungsLabor – Systemtest")


def draw():
    py5.background(235, 240, 245)

    py5.no_stroke()
    py5.fill(37, 99, 201)
    py5.circle(400, 250, 100)

    py5.fill(30, 45, 60)
    py5.text_size(28)
    py5.text_align(py5.CENTER)
    py5.text("BewegungsLabor", 400, 100)

    py5.text_size(18)
    py5.text("Systemtest erfolgreich!", 400, 380)


py5.run_sketch()

