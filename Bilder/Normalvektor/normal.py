from manim import *


class Normal(ThreeDScene):
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

        normal_vector = Arrow3D([-1, 0, 1], [-1, 0, 2], color=BLACK)
        line = Line(start=(3, 0, 1), end=(-3, 0, 1), color=BLACK)
        n_label_coords = np.array([-1.3, 0, 2.3])
        n_label = MathTex("\\vec{n}", color=BLACK).move_to(n_label_coords)

        x_label = MathTex("x", color=BLACK).next_to(
            axes.x_axis.get_end(), RIGHT, buff=0.2
        )
        y_label = MathTex("y", color=BLACK).next_to(
            axes.y_axis.get_end(), LEFT, buff=0.2
        )
        z_label = MathTex("z", color=BLACK).next_to(axes.z_axis.get_end(), UP, buff=0.2)

        self.add(axes, line, normal_vector)
        self.add(x_label, y_label, z_label, n_label)
        self.set_camera_orientation(phi=80 * DEGREES, theta=40 * DEGREES)

        x_label.rotate(PI / 2, axis=RIGHT).rotate(PI*0.9, axis=OUT)
        y_label.rotate(PI / 2, axis=RIGHT).rotate(PI*0.9, axis=OUT)
        z_label.rotate(PI / 2, axis=RIGHT).rotate(PI*0.9, axis=OUT)
        n_label.rotate(PI / 2, axis=RIGHT).rotate(PI*0.9, axis=OUT)

        self.wait(5)
