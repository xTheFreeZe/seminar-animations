from manim import *


class Graph(ThreeDScene):
    def construct(self):
        # Create the 3D axes with default orientation
        axes = ThreeDAxes(
            x_length=10,
            y_length=10,
            z_length=10,
            x_axis_config={"color": RED},
            y_axis_config={"color": GREEN},
            z_axis_config={"color": BLUE},
        )

        axes.scale(0.5)

        axes.shift(RIGHT * 2)

        self.play(Create(axes), run_time=2)

        x_label = MathTex("x").next_to(axes.x_axis.get_end(), RIGHT, buff=0.2)
        y_label = MathTex("y").next_to(axes.y_axis.get_end(), LEFT, buff=0.2)
        z_label = MathTex("z").next_to(axes.z_axis.get_end(), UP, buff=0.2)

        self.play(Write(x_label), Write(y_label), Write(z_label))

        line_one = axes.plot_line_graph(
            lambda t: np.array([-5, -7, 0]) + t * np.array([3, 0, 1]),
            t_range=[-5, 5],
            color=RED,
        )

        self.play(Create(line_one), run_time=2)

        axis_and_lines = VGroup(axes, line_one)

        self.play(axis_and_lines.animate.rotate(angle=PI / 6, axis=UP))
        self.play(axis_and_lines.animate.rotate(angle=-PI / 12, axis=RIGHT))

        self.wait(2)

        self.set_camera_orientation(phi=2 * PI / 5, theta=PI / 5)
        axes = ThreeDAxes(
            x_length=13,
            y_length=13,
            z_length=13,
            x_axis_config={"color": RED},
            y_axis_config={"color": GREEN},
            z_axis_config={"color": BLUE},
        )
        axes.scale(0.5)
        self.play(Create(axes))

        x_label = MathTex("x").next_to(axes.x_axis.get_end(), RIGHT, buff=0.2)
        y_label = MathTex("y").next_to(axes.y_axis.get_end(), LEFT, buff=0.2)
        z_label = MathTex("z").next_to(axes.z_axis.get_end(), UP, buff=0.2)

        self.play(Write(x_label), Write(y_label), Write(z_label))

        self.wait(2)

        line_one = Line3D(
            start=np.array([-5, -7, 0]), end=np.array([3, 0, 1]), color=RED
        )
        line_one.scale(0.5)
        self.play(Create(line_one))

        line_two = Line3D(
            start=np.array([12, 0, 1]), end=np.array([3, 2, 2]), color=GREEN
        )
        line_two.scale(0.5)
        self.play(Create(line_two))

        self.wait(2)
