from manim import *


class Normal(ThreeDScene):
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

        normal_vector = Arrow3D([2, 1, 0], [2, 2, 0], color=BLACK)
        line = Line(start=LEFT * 3, end=RIGHT * 3, color=BLACK).move_to(UP)
        n_label_coords = np.array([2.3, 2.3, 0])
        n_label = MathTex("\\vec{n}", color=BLACK).move_to(n_label_coords)

        x_label = MathTex("y", color=BLACK).next_to(
            axes.x_axis.get_end(), RIGHT, buff=0.2
        )
        y_label = MathTex("z", color=BLACK).next_to(
            axes.y_axis.get_end(), LEFT, buff=0.2
        )
        z_label = MathTex("x", color=BLACK).next_to(axes.z_axis.get_end(), UP, buff=0.2)

        self.play(Create(axes), run_time=2)
        self.play(Create(line))
        self.play(Create(normal_vector))

        group = VGroup()
        group.add(axes, line, normal_vector, x_label, y_label, z_label, n_label)

        self.play(group.animate.rotate(angle=PI / 6, axis=UP))
        self.play(group.animate.rotate(angle=-PI / 12, axis=LEFT))

        self.wait(2)
