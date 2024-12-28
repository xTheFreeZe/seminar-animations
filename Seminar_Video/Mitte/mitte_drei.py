from manim import *


class Mitte_drei(ThreeDScene):
    def construct(self):
        self.fps = 30

        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            z_length=6,
            x_axis_config={"color": BLUE},
            y_axis_config={"color": RED},
            z_axis_config={"color": GREEN},
        )

        x_label = MathTex("x", color=WHITE).next_to(axes.get_x_axis().get_end())
        y_label = MathTex("y", color=WHITE).next_to(axes.get_y_axis().get_end())
        z_label = MathTex("z", color=WHITE).next_to(axes.get_z_axis().get_end())

        self.set_camera_orientation(phi=80 * DEGREES, theta=20 * DEGREES)
        self.play(Create(axes))
        self.add_fixed_orientation_mobjects(x_label, y_label, z_label)
        self.play(Create(x_label), Create(y_label), Create(z_label))

        # Geraden von: file:///C:/Users/marwi/OneDrive/Dokumente/Seminararbeit/Volumen_Spat/Abstand_Spat_Methode.pdf

        # Line g: r_g(lambda) = (1, 2, 0) + lambda * (1, 4, 0)
        line_g = ParametricFunction(
            lambda t: axes.coords_to_point(1 + t, 2 + 4 * t, 0),
            t_range=[-1, 0.3],
            color=BLUE,
        ).set_opacity(0)

        # Line h: r_h(phi) = (-2, -1, 2) + phi * (-7, 3, -1)
        line_h = ParametricFunction(
            lambda t: axes.coords_to_point(-2 - 7 * t, -1 + 3 * t, 2 - t),
            t_range=[-0.5, 1],
            color=GREEN,
        ).set_opacity(0)

        group = VGroup(line_g, line_h, axes, x_label, y_label, z_label)
        self.play(group.animate.shift(3 * UP))

        line_g_eq = MathTex(
            r"r_g(\lambda) = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix} + \lambda \begin{pmatrix} 1 \\ 4 \\ 0 \end{pmatrix}",
            color=BLUE,
            font_size=25,
        ).shift(2 * UP + 4 * LEFT)
        line_h_eq = MathTex(
            r"r_h(\phi) = \begin{pmatrix} -2 \\ -1 \\ 2 \end{pmatrix} + \phi \begin{pmatrix} -7 \\ 3 \\ -1 \end{pmatrix}",
            color=GREEN,
            font_size=25,
        ).shift(4 * LEFT)

        self.add_fixed_in_frame_mobjects(line_g_eq)
        self.play(
            Write(line_g_eq), Create(line_g), line_g.animate.set_opacity(1), run_time=2
        )

        self.wait(2)
        self.add_fixed_in_frame_mobjects(line_h_eq)
        self.play(
            Write(line_h_eq), Create(line_h), line_h.animate.set_opacity(1), run_time=2
        )

        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.wait(4)
