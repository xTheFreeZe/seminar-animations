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

        self.set_camera_orientation(phi=80 * DEGREES, theta=30 * DEGREES)
        self.play(Create(axes))
        self.add_fixed_orientation_mobjects(x_label, y_label, z_label)
        self.play(Create(x_label), Create(y_label), Create(z_label))

        # Geraden von: file:///C:/Users/marwi/OneDrive/Dokumente/Seminararbeit/Volumen_Spat/Abstand_Spat_Methode.pdf

        # Line g: r_g(lambda) = (1, 2, 0) + lambda * (1, 4, 0)
        line_g = ParametricFunction(
            lambda t: axes.coords_to_point(1 + t, 2 + 4 * t, 0),
            t_range=[-1.5, 0.5],
            color=BLUE,
        ).set_opacity(0)

        # Line h: r_h(phi) = (-2, -1, 2) + mu * (-7, 3, -1)
        line_h = ParametricFunction(
            lambda t: axes.coords_to_point(-2 - 7 * t, -1 + 3 * t, 2 - t),
            t_range=[-0.5, 1],
            color=GREEN,
        ).set_opacity(0)

        group = VGroup(line_g, line_h, axes, x_label, y_label, z_label)
        self.play(group.animate.shift(3 * UP))

        line_g_eq = MathTex(
            r"g: \vec{x} = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix} + \lambda \begin{pmatrix} 1 \\ 4 \\ 0 \end{pmatrix}",
            color=BLUE,
            font_size=25,
        ).shift(2 * UP + 4 * LEFT)
        line_h_eq = MathTex(
            r"h: \vec{x} = \begin{pmatrix} -2 \\ -1 \\ 2 \end{pmatrix} + \mu \begin{pmatrix} -7 \\ 3 \\ -1 \end{pmatrix}",
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
        self.wait(2)

        # Die Geraden als Punkte schreiben
        # P_g(1+Lambda | 2+4*Lambda | 0)
        # P_h(-2-7*Mu | -1+3*Mu | 2-Mu)
        line_as_point_g = (
            MathTex(
                r"P_g = (1 + \lambda \mid 2 + 4\lambda \mid 0)",
                color=BLUE,
                font_size=25,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN * 2)
        )

        line_as_point_h = (
            MathTex(
                r"P_h = (-2 - 7\mu \mid -1 + 3\mu \mid 2 - \mu)",
                color=GREEN,
                font_size=25,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN * 4)
        )

        self.add_fixed_in_frame_mobjects(line_as_point_g)
        self.play(
            line_g_eq.animate.to_corner(UP + LEFT).shift(DOWN), Write(line_as_point_g)
        )

        self.add_fixed_in_frame_mobjects(line_as_point_h)
        self.play(
            line_h_eq.animate.to_corner(UP + LEFT).shift(DOWN * 3),
            Write(line_as_point_h),
        )

        self.wait(2)

        # Die Punkte als Vektor schreiben
        connection_vec = (
            MathTex(
                r"\vec{ {P_gP_h} } = \begin{pmatrix} -2 - 7\mu - (1 + \lambda) \\ -1 + 3\mu - (2 + 4\lambda) \\ 2 - \mu - 0 \end{pmatrix} = \begin{pmatrix} -3 -7 \mu - \lambda \\ -3 + 3 \mu - 4 \lambda \\ 2 - \mu \end{pmatrix}",
                color=WHITE,
                font_size=25,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN * 3.7)
        )

        connection_vec_short = (
            MathTex(
                r"\vec{ {P_gP_h} } = \begin{pmatrix} -3 -7 \mu - \lambda \\ -3 + 3 \mu - 4 \lambda \\ 2 - \mu \end{pmatrix}",
                font_size=25,
                color=WHITE,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN * 1)
        )

        self.add_fixed_in_frame_mobjects(connection_vec)
        self.play(
            line_g_eq.animate.to_corner(UP + LEFT),
            line_h_eq.animate.to_corner(UP + LEFT).shift(DOWN * 1.2),
            line_as_point_g.animate.to_corner(UP + LEFT).shift(DOWN * 2.5),
            line_as_point_h.animate.to_corner(UP + LEFT).shift(DOWN * 3),
            Write(connection_vec),
        )

        self.wait(2)

        self.begin_ambient_camera_rotation(rate=-0.1, about="phi")

        start_points = line_g.get_all_points()
        end_points = line_h.get_all_points()

        first_connection_vec = Arrow3D(
            start_points[0],
            end_points[0],
            color=WHITE,
        )

        second_connection_vec = Arrow3D(
            start_points[100],
            end_points[100],
            color=WHITE,
        )

        third_connection_vec = Arrow3D(
            start_points[200],
            end_points[200],
            color=WHITE,
        )

        fourth_connection_vec = Arrow3D(
            start_points[300],
            end_points[500],
            color=WHITE,
        )

        fith_connection_vec = Arrow3D(
            start_points[500],
            end_points[300],
            color=WHITE,
        )

        sixth_connection_vec = Arrow3D(
            start_points[150],
            end_points[100],
            color=WHITE,
        )

        self.play(Create(fith_connection_vec))

        self.play(
            FadeOut(line_as_point_h),
            FadeOut(line_as_point_g),
            FadeOut(line_h_eq),
            FadeOut(line_g_eq),
        )

        self.stop_ambient_camera_rotation(about="phi")

        scalar_product_g = (
            MathTex(
                r"\vec{ {P_gP_h} } \circ \begin{pmatrix} 1 \\ 4 \\ 0 \end{pmatrix} = 0",
                font_size=25,
                color=BLUE,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN * 2.5)
        )

        scalar_product_h = (
            MathTex(
                r"\vec{ {P_gP_h} } \circ \begin{pmatrix} -7 \\ 3 \\ -1 \end{pmatrix} = 0",
                font_size=25,
                color=GREEN,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN * 3.7)
        )

        self.add_fixed_in_frame_mobjects(scalar_product_g)
        self.add_fixed_in_frame_mobjects(scalar_product_h)
        self.play(
            connection_vec.animate.to_corner(UP + LEFT).shift(DOWN * 1),
            ReplacementTransform(connection_vec, connection_vec_short),
            Write(scalar_product_g),
            Write(scalar_product_h),
        )
        self.add_fixed_in_frame_mobjects(connection_vec_short)

        self.play(ReplacementTransform(fith_connection_vec, second_connection_vec))
        self.wait(0.5)
        self.play(ReplacementTransform(second_connection_vec, third_connection_vec))
        self.wait(0.5)
        self.play(ReplacementTransform(third_connection_vec, fourth_connection_vec))
        self.wait(0.5)
        self.play(ReplacementTransform(fourth_connection_vec, fith_connection_vec))
        self.wait(0.5)
        self.play(ReplacementTransform(fith_connection_vec, sixth_connection_vec))
        self.wait(0.5)
        self.play(ReplacementTransform(sixth_connection_vec, second_connection_vec))
        self.wait(0.5)
        self.play(ReplacementTransform(second_connection_vec, third_connection_vec))
        self.wait(0.5)
        self.play(ReplacementTransform(third_connection_vec, fourth_connection_vec))
        self.wait(5)
        self.play(FadeOut(fourth_connection_vec))

        half_scalar_product_g = (
            MathTex(
                r"-15 + 5 \mu - 17 \lambda = 0",
                font_size=25,
                color=BLUE,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN * 2.5)
        )

        half_scalar_product_h = (
            MathTex(
                r"10 + 59 \mu - 5 \lambda = 0",
                font_size=25,
                color=GREEN,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN * 3.3)
        )

        self.play(ReplacementTransform(scalar_product_g, half_scalar_product_g))
        self.add_fixed_in_frame_mobjects(half_scalar_product_g)

        self.wait(2)

        self.play(
            ReplacementTransform(scalar_product_h, half_scalar_product_h),
        )
        self.add_fixed_in_frame_mobjects(half_scalar_product_h)

        self.wait(2)

        lambda_solution = (
            MathTex(
                r"\lambda \approx -0,93",
                font_size=25,
                color=BLUE,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN * 2.5)
        )

        mu_solution = (
            MathTex(
                r"\mu \approx -0,17",
                font_size=25,
                color=GREEN,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN * 3.3)
        )

        self.play(
            ReplacementTransform(half_scalar_product_g, lambda_solution)
        )
        self.add_fixed_in_frame_mobjects(lambda_solution)
        self.wait(2)
        self.play(ReplacementTransform(half_scalar_product_h, mu_solution))
        self.add_fixed_in_frame_mobjects(mu_solution)
        self.wait(2)

        self.play(
            FadeOut(connection_vec_short),
            lambda_solution.animate.to_corner(UP + LEFT).shift(DOWN),
            mu_solution.animate.to_corner(UP + LEFT).shift(DOWN * 1.5),
        )

        point_g_line = (
            MathTex(
                "P_g = (1 +",
                "\\lambda",
                "\\mid 2 + 4",
                "\\lambda",
                "\\mid 0)",
                color=BLUE,
                font_size=25,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN * 2.5)
        )

        point_h_line = (
            MathTex(
                "P_h = (-2 - 7",
                "\\mu",
                "\\mid -1 + 3",
                "\\mu",
                "\\mid 2 -",
                "\\mu",
                ")",
                color=GREEN,
                font_size=25,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN * 3)
        )

        self.add_fixed_in_frame_mobjects(point_g_line)
        self.play(Write(point_g_line))
        self.add_fixed_in_frame_mobjects(point_h_line)
        self.play(Write(point_h_line))

        self.play(
            point_g_line[1].animate.set_color(YELLOW),
            point_g_line[3].animate.set_color(YELLOW),
        )

        complete_point_g_line = (
            MathTex(
                r"P_g = (1 - 0,93 \mid 2 + 4 \cdot (-0,93) \mid 0)",
                color=BLUE,
                font_size=25,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN * 2.5)
            .set_opacity(0)
        )

        self.add_fixed_in_frame_mobjects(complete_point_g_line)

        self.play(ReplacementTransform(point_g_line, complete_point_g_line), complete_point_g_line.animate.set_opacity(1))

        self.wait(2)

        self.play(
            point_h_line[1].animate.set_color(YELLOW),
            point_h_line[3].animate.set_color(YELLOW),
            point_h_line[5].animate.set_color(YELLOW),
        )

        complete_point_h_line = (
            MathTex(
                r"P_h = (-2 - 7 \cdot (-0,17) \mid -1 + 3 \cdot (-0,17) \mid 2 + -0,17)",
                color=GREEN,
                font_size=25,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN * 3)
            .set_opacity(0)
        )

        self.add_fixed_in_frame_mobjects(complete_point_h_line)

        self.play(ReplacementTransform(point_h_line, complete_point_h_line), complete_point_h_line.animate.set_opacity(1))

        self.wait(2)
