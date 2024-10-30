from manim import *


class VektorenBild(ThreeDScene):
    def construct(self):

        self.camera.background_color = WHITE

        axes = ThreeDAxes(
            x_length=6,
            y_length=6,
            z_length=6,
            x_axis_config={"color": BLUE},
            y_axis_config={"color": RED},
            z_axis_config={"color": GREEN},
        )

        vektor = Arrow3D([0, 0, 0], [0, 2, 1], color=BLACK)
        dot = Dot(ORIGIN, color="Black")
        x_label = MathTex("x", color=BLACK).next_to(
            axes.x_axis.get_end(), RIGHT, buff=0.2
        )
        y_label = MathTex("y", color=BLACK).next_to(
            axes.y_axis.get_end(), LEFT, buff=0.2
        )
        z_label = MathTex("z", color=BLACK).next_to(axes.z_axis.get_end(), UP, buff=0.2)
        origin_text_coords = np.array([0.8, 0, 0.4])
        origin_text = (
            Text("(0, 0, 0)", color=BLACK).move_to(origin_text_coords).scale(0.5)
        )
        tip_text_coords = np.array([0, 2.2, 1.4])
        tip_text = Text("(0, 2, 1)", color=BLACK).move_to(tip_text_coords).scale(0.5)

        self.add(axes, vektor, dot)
        self.add(x_label, y_label, z_label, origin_text, tip_text)

        self.set_camera_orientation(phi=80 * DEGREES, theta=40 * DEGREES)
        x_label.rotate(PI / 2, axis=RIGHT).rotate(PI * 0.9, axis=OUT)
        y_label.rotate(PI / 2, axis=RIGHT).rotate(PI * 0.9, axis=OUT)
        z_label.rotate(PI / 2, axis=RIGHT).rotate(PI * 0.9, axis=OUT)
        origin_text.rotate(PI / 2, axis=RIGHT).rotate(PI * 0.9, axis=OUT)
        tip_text.rotate(PI / 2, axis=RIGHT).rotate(PI * 0.9, axis=OUT)

        self.wait(6)