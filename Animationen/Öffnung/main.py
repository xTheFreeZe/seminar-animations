from manim import *


class WelcomeScene(ThreeDScene):
    def construct(self):
        welcome_text = Text("Seminarvideo Marwin Eder ft13a", font_size=30)
        self.play(Write(welcome_text), run_time=2)

        self.wait(2)
        theme_text = Text("Abstand zweier windschiefer Geraden", font_size=25)
        self.play(ReplacementTransform(welcome_text, theme_text), run_time=2)
        self.wait(2)

        self.play(theme_text.animate.shift(UP * 3, LEFT * 4))
        self.play(theme_text.animate.scale(0.5))
        self.wait(2)

        axes = ThreeDAxes(
            x_length=10,
            y_length=10,
            z_length=10,
            x_axis_config={"color": RED},
            y_axis_config={"color": GREEN},
            z_axis_config={"color": BLUE},
        )

        line_one_equation = MathTex(
            r"g:\vec{x} = \begin{pmatrix} -5 \\ -7 \\ 0 \end{pmatrix}"
            r" + t \begin{pmatrix} 3 \\ 0 \\ 1 \end{pmatrix}",
            font_size=25,
        )
        line_one_equation.shift(LEFT * 4, UP)

        self.play(Write(line_one_equation), run_time=2)
        self.wait(2)

        line_two_equation = MathTex(
            r"h:\vec{x} = \begin{pmatrix} 12 \\ 0 \\ 1 \end{pmatrix}"
            r" + s \begin{pmatrix} 3 \\ 2 \\ 2 \end{pmatrix}",
            font_size=25,
        )
        line_two_equation.shift(LEFT * 4, DOWN)

        self.play(Write(line_two_equation), run_time=2)
        self.wait(2)

        # Skaliere das Koordinatensystem um die Hälfte
        axes.scale(0.5)
        axes.shift(RIGHT * 2)

        # Definiere die Punkte und die Linien
        # Linie g von (-5, -7, 0) nach (1, -7, 2)
        g_start = np.array([-5, -7, 0]) * 0.5
        g_end = np.array([1, -7, 2]) * 0.5
        line_g = Line3D(
            axes.coords_to_point(*g_start), axes.coords_to_point(*g_end), color=RED
        )

        # Linie h von (12, 0, 1) nach (18, 4, 5)
        h_start = np.array([12, 0, 1]) * 0.5
        h_end = np.array([18, 4, 5]) * 0.5
        line_h = Line3D(
            axes.coords_to_point(*h_start), axes.coords_to_point(*h_end), color=GREEN
        )

        # Gruppiere Achsen und Linien, damit sie zusammen rotieren
        axis_and_lines = VGroup(axes, line_g, line_h)

        # Zeige das Koordinatensystem und die Linien gleichzeitig an
        self.play(Create(axis_and_lines), run_time=2)

        # Rotationen für das Koordinatensystem
        self.play(axis_and_lines.animate.rotate(angle=PI / 6, axis=UP))
        self.play(axis_and_lines.animate.rotate(angle=-PI / 12, axis=RIGHT))

        # Achsen-Beschriftungen
        x_label = MathTex("x").next_to(axes.x_axis.get_end(), RIGHT, buff=0.2)
        y_label = MathTex("y").next_to(axes.y_axis.get_end(), LEFT, buff=0.2)
        z_label = MathTex("z").next_to(axes.z_axis.get_end(), UP, buff=0.2)

        self.play(Write(x_label), Write(y_label), Write(z_label))

        self.wait(2)
