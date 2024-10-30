from manim import *


class KreuzBild(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE

        axes = ThreeDAxes(
            x_length=7,
            y_length=7,
            z_length=7,
            x_axis_config={"color": BLUE},
            y_axis_config={"color": RED},
            z_axis_config={"color": GREEN},
        )

        vektor_eins = Arrow3D([0, 0, 0], [1, 0, 0], color=BLACK)
        vektor_zwei = Arrow3D([0, 0, 0], [0, 1, 0], color=BLACK)
        kreuzprodukt = Arrow3D([0, 0, 0], [0, 0, 1], color=BLUE)

        x_label = MathTex("x", color=BLACK).next_to(
            axes.x_axis.get_end(), RIGHT, buff=0.2
        )
        y_label = MathTex("y", color=BLACK).next_to(
            axes.y_axis.get_end(), LEFT, buff=0.2
        )
        z_label = MathTex("z", color=BLACK).next_to(axes.z_axis.get_end(), UP, buff=0.2)

        x_label.rotate(PI / 2, axis=RIGHT).rotate(PI*0.9, axis=OUT)
        y_label.rotate(PI / 2, axis=RIGHT).rotate(PI*0.9, axis=OUT)
        z_label.rotate(PI / 2, axis=RIGHT).rotate(PI*0.9, axis=OUT)

        self.add(axes)
        self.add(vektor_eins, vektor_zwei, kreuzprodukt)
        self.add(x_label, y_label, z_label)
        self.set_camera_orientation(phi=80 * DEGREES, theta=40 * DEGREES)
        self.wait(6)
