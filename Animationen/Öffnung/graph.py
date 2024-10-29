from manim import *


class Graph(ThreeDScene):
    def construct(self):
        # Create the 3D axes with default orientation
        axes = ThreeDAxes(
            x_length=7,
            y_length=7,
            z_length=7,
            x_axis_config={"color": RED},
            y_axis_config={"color": GREEN},
            z_axis_config={"color": BLUE},
        )

        x_label = MathTex("y", color=WHITE).next_to(
            axes.x_axis.get_end(), RIGHT, buff=0.2
        )
        y_label = MathTex("z", color=WHITE).next_to(
            axes.y_axis.get_end(), LEFT, buff=0.2
        )
        z_label = MathTex("x", color=WHITE).next_to(axes.z_axis.get_end(), UP, buff=0.2)

        self.add(axes, x_label, y_label, z_label)

        g1 = axes.plot_parametric_curve(
            lambda t: np.array([1 + t, 2 + t, 1]),  # (1, 2, 1) + t * (1, 1, 0)
            t_range=[-7, 7],
            color=BLUE,
        )
        g2 = axes.plot_parametric_curve(
            lambda s: np.array([3, 1 + s, s]),  # (3, 1, 0) + s * (0, 1, 1)
            t_range=[-7, 7],
            color=GREEN,
        )

        self.add(g1, g2)

        group = VGroup()
        group.add(g1, g2, axes, x_label, y_label, z_label)

        self.play(group.animate.rotate(angle=PI / 6, axis=UP))
        self.play(group.animate.rotate(angle=-PI / 8, axis=LEFT))
        self.wait(2)

        #TODO: Add a 360° rotation to pronounce the lines even more :)

        self.wait(2)

        g1_label_text = MathTex(
            r"g:\vec{x} = \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}"
            r" + t \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}",
            color=BLUE,
            font_size=25,
        )

        g2_label_text = MathTex(
            r"h:\vec{x} = \begin{pmatrix} 3 \\ 1 \\ 0 \end{pmatrix}"
            r" + s \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}",
            color=GREEN,
            font_size=25,
        )

        g1_label_text.shift(UP * 2, LEFT * 5)
        g2_label_text.shift(LEFT * 5)
        self.play(Write(g1_label_text), Write(g2_label_text), run_time=2)

        self.wait(2)