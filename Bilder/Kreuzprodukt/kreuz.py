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

        # y = [1]
        # z 

        vektor_eins = Arrow3D([0, 0, 0], [1, 0, 0], color=BLACK)
        vektor_zwei = Arrow3D([0, 0, 0], [0, 1, 0], color=BLACK)
        kreuzprodukt = Arrow3D([0, 0, 0], [0, 0, 1], color=BLACK)

        tip_text = (
            Text("(1, 0, 0)", color=BLACK)
            .next_to(vektor_eins.get_end(), RIGHT)
            .scale(0.5)
        )
        tip_text_zwei = (
            Text("(0, 1, 0)", color=BLACK)
            .next_to(vektor_zwei.get_end(), RIGHT)
            .scale(0.5)
        )
        tip_text_kreuz = (
            Text("(0, 0, 1)", color=BLACK)
            .next_to(kreuzprodukt.get_end(), RIGHT)
            .scale(0.5)
        )

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

        # self.play(Create(vektor_eins), Create(vektor_zwei), Create(dot), run_time=1)
        # play everything
        self.play(
            Create(axes),
            Create(vektor_eins),
            Create(vektor_zwei),
            Create(kreuzprodukt),
            Create(tip_text),
            Create(tip_text_zwei),
            Create(tip_text_kreuz),
            run_time=2,
        )
        self.play(axis_and_lines.animate.rotate(angle=PI / 6, axis=UP))
        self.play(axis_and_lines.animate.rotate(angle=-PI / 12, axis=LEFT))
        self.wait(6)
