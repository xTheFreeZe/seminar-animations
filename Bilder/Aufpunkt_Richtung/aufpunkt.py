from manim import *


class Aufpunkt(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE

        axes = ThreeDAxes(
            x_length=7,
            y_length=7,
            z_length=7,
            x_axis_config={"color": RED},
            y_axis_config={"color": GREEN},
            z_axis_config={"color": BLUE},
        )

        # Aufpunkt = 1,1,1
        # Richtungsvektor = 2,1,0

        aufpunkt = np.array([1, 1, 1])  # Aufpunkt
        richtungsvektor = np.array([2, 1, 0])  # Richtungsvektor (2, 1, 0)
        
        # Linie basierend auf Aufpunkt und Richtungsvektor (die Gerade)
        line = Arrow3D(start=aufpunkt - richtungsvektor, end=aufpunkt + richtungsvektor, color=BLACK)

        equation = MathTex(
            r"g:\vec{x} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}"
            r" + t \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix}",
            color=BLACK,
            font_size=25,
        ).move_to(LEFT * 3 + UP * 2)

        self.add(axes, equation, line)

        group = VGroup()
        group.add(axes, equation, line)

        self.play(group.animate.rotate(angle=PI / 6, axis=UP))
        self.play(group.animate.rotate(angle=-PI / 8, axis=LEFT))

        self.wait(2)