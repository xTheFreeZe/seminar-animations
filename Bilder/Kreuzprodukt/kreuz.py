from manim import *


class KreuzBild(ThreeDScene):
    def construct(self):

        # Change background color to white
        self.camera.background_color = WHITE

        axes = ThreeDAxes(
            x_length=7,
            y_length=7,
            z_length=7,
            x_axis_config={"color": RED},
            y_axis_config={"color": GREEN},
            z_axis_config={"color": BLUE},
        )

        # Die Koordinaten sind aus irgendeinem Grund gefickt
        # z = [-, x, -]
        # x = [-, -, x]
        # y = [x, -, -]

        vektor_eins = Arrow3D([0, 0, 0], [0, 0, 1], color=BLACK)
        vektor_zwei = Arrow3D([0, 0, 0], [1, 1, 0], color=BLACK)
        kreuzprodukt = Arrow3D([0, 0, 0], [-1, 1, 0], color=BLUE)

        x_label = MathTex("y", color=BLACK).next_to(
            axes.x_axis.get_end(), RIGHT, buff=0.2
        )
        y_label = MathTex("z", color=BLACK).next_to(
            axes.y_axis.get_end(), LEFT, buff=0.2
        )
        z_label = MathTex("x", color=BLACK).next_to(axes.z_axis.get_end(), UP, buff=0.2)

        axis_and_lines = VGroup(
            axes, vektor_eins, vektor_zwei, x_label, y_label, z_label
        )

        self.add(axes)

        self.add(vektor_eins, vektor_zwei, kreuzprodukt)

        self.play(axis_and_lines.animate.rotate(angle=PI / 6, axis=UP))
        self.play(axis_and_lines.animate.rotate(angle=-PI / 12, axis=LEFT))
        self.wait(6)
