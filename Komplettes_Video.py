from manim import *


class Video(ThreeDScene):
    def construct(s):
        s.fps = 60
        title = Tex("Seminarvideo Marwin", font_size=30)
        topic = Tex("Abstand zweier", " windschiefer", " Geraden", font_size=25)

        s.play(Write(title))
        s.wait()

        transform_title = Tex("Thema:", font_size=25)
        transform_title.to_corner(UP + LEFT)

        s.play(Transform(title, transform_title))
        s.wait(0.5)
        s.play(Write(topic))

        s.wait(5)

        s.play(topic.animate.to_corner(UP + LEFT).shift(DOWN * 0.5))
        s.wait()

        framebox_one = SurroundingRectangle(topic[1], buff=0.05)
        framebox_two = SurroundingRectangle(topic[2], buff=0.05)

        skew_definition_header = Tex("Voraussetzungen windschief", font_size=30)
        skew_definition_one = MathTex("\\circ \\text{ Nicht parallel}", font_size=30)
        skew_definition_two = MathTex(
            "\\circ \\text{ Keinen Schnittpunkt}", font_size=30
        )
        skew_definition_three = MathTex("\\circ \\text{ Nicht identisch}", font_size=30)

        # This groups the elements together, placing them in a downward direction
        skew_definition = VGroup(
            skew_definition_header,
            skew_definition_one,
            skew_definition_two,
            skew_definition_three,
        )
        skew_definition.arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        s.play(
            Create(framebox_one),
            LaggedStart(*[FadeIn(mob, shift=UP) for mob in skew_definition]),
        )
        s.wait(11)

        s.play(
            ReplacementTransform(framebox_one, framebox_two),
            LaggedStart(*[FadeOut(mob, shift=DOWN) for mob in skew_definition]),
        )
        s.wait(2)

        # two lines that intersect each other
        axes_one = ThreeDAxes(
            x_length=10,
            y_length=10,
            z_length=10,
            x_axis_config={"color": WHITE},
            y_axis_config={"color": WHITE},
            z_axis_config={"color": WHITE},
        )

        line_one_intersect = Line3D(
            start=[-3, -3, 0],
            end=[3, 3, 0],
            color=BLUE,
        )

        line_two_intersect = Line3D(
            start=[-3, 3, 0],
            end=[3, -3, 0],
            color=RED,
        )

        group_one = VGroup(axes_one, line_one_intersect, line_two_intersect)
        group_one.scale(0.2).move_to(LEFT * 4)
        s.play(LaggedStart(*[FadeIn(mob, shift=UP) for mob in group_one]))
        group_one_box = SurroundingRectangle(group_one, buff=0.1, color=WHITE)

        s.wait(0.5)

        # two lines that are parallel to each other
        axes_two = ThreeDAxes(
            x_length=10,
            y_length=10,
            z_length=10,
            x_axis_config={"color": WHITE},
            y_axis_config={"color": WHITE},
            z_axis_config={"color": WHITE},
        )

        line_one_parallel = Line3D(
            start=[-3, -3, 0],
            end=[3, 3, 0],
            color=BLUE,
        )

        line_two_parallel = Line3D(
            start=[-3, -3, 1],
            end=[3, 3, 1],
            color=RED,
        )

        group_two = VGroup(axes_two, line_one_parallel, line_two_parallel)
        group_two.scale(0.2).move_to(ORIGIN)
        s.play(LaggedStart(*[FadeIn(mob, shift=UP) for mob in group_two]))
        group_two_box = SurroundingRectangle(group_two, buff=0.1, color=WHITE)

        s.wait(0.5)

        # two lines that are skew to each other
        axes_three = ThreeDAxes(
            x_length=10,
            y_length=10,
            z_length=10,
            x_axis_config={"color": WHITE},
            y_axis_config={"color": WHITE},
            z_axis_config={"color": WHITE},
        )

        line_one_skew = Line3D(
            start=[-5, -2, -3],
            end=[5, 2, -1],
            color=BLUE,
        )

        line_two_skew = Line3D(
            start=[2, -4, 5],
            end=[-2, 3, 8],
            color=RED,
        )

        group_three = VGroup(axes_three, line_one_skew, line_two_skew)
        group_three.scale(0.2).move_to(RIGHT * 4)
        s.play(LaggedStart(*[FadeIn(mob, shift=UP) for mob in group_three]))
        group_three_box = SurroundingRectangle(group_three, buff=0.1, color=WHITE)

        s.play(FadeOut(group_two, group_three))
        s.play(Create(group_one_box))
        s.play(group_one.animate.move_to(ORIGIN), group_one_box.animate.move_to(ORIGIN))
        s.play(group_one.animate.scale(1.8), group_one_box.animate.scale(1.8))
        s.play(Rotating(group_one, axis=UP, radians=2 * PI, run_time=6.5))
        s.wait(3)
        s.play(
            group_one.animate.move_to(LEFT * 4), group_one_box.animate.move_to(LEFT * 4)
        )
        s.play(group_one.animate.scale(0.6), group_one_box.animate.scale(0.6))
        s.play(FadeIn(group_two, group_three))
        s.play(ReplacementTransform(group_one_box, group_two_box))
        s.play(FadeOut(group_one, group_three))
        s.play(
            group_two.animate.scale(1.8),
            group_two_box.animate.scale(1.8),
        )
        s.play(Rotating(group_two, axis=UP, radians=2 * PI, run_time=6.5))
        s.wait(3)
        s.play(group_two.animate.scale(0.6), group_two_box.animate.scale(0.6))
        s.play(FadeIn(group_three, group_one))
        s.play(ReplacementTransform(group_two_box, group_three_box))
        s.play(FadeOut(group_one, group_two))
        s.play(
            group_three.animate.move_to(ORIGIN), group_three_box.animate.move_to(ORIGIN)
        )
        s.play(group_three.animate.scale(1.8), group_three_box.animate.scale(2))
        s.play(Rotating(group_three, axis=UP, radians=2 * PI, run_time=6.5))
        s.play(
            group_three.animate.move_to(RIGHT * 4),
            group_three_box.animate.move_to(RIGHT * 4),
        )
        s.play(group_three.animate.scale(0.6), group_three_box.animate.scale(0.6))
        s.play(FadeOut(group_three_box))
        s.play(FadeIn(group_one, group_two))
        s.wait(3)
        s.play(FadeOut(framebox_two))
        s.wait(2)

        # Fade out everything except group_three and put it in the center
        s.play(FadeOut(group_one, group_two))
        s.play(FadeOut(topic, transform_title, title))
        s.play(group_three.animate.move_to(ORIGIN))
        s.play(group_three.animate.scale(1.7))

        s.wait(2)


class Mitte_eins(ThreeDScene):
    def construct(self):
        self.fps = 60

        axes = ThreeDAxes(
            x_length=10,
            y_length=10,
            z_length=10,
            x_axis_config={"color": WHITE},
            y_axis_config={"color": WHITE},
            z_axis_config={"color": WHITE},
        )

        silent_axes = ThreeDAxes(
            x_length=15,
            y_length=15,
            z_length=10,
        )

        line_one_skew = Line3D(
            start=[-5, -2, -3],
            end=[5, 2, -1],
            color=BLUE,
        )

        line_two_skew = Line3D(
            start=[2, -4, 5],
            end=[-2, 3, 8],
            color=RED,
        )

        group = VGroup(axes, line_one_skew, line_two_skew)
        group.scale(0.2)
        group.scale(1.8)
        group.move_to(ORIGIN)
        self.add(group)
        self.wait(1)

        text = Tex("Verbindungsvektor", font_size=35).move_to(ORIGIN)
        text_2 = Tex("Methode des Verbindungsvektores", font_size=25).to_corner(UL)

        wave_to_right = ParametricFunction(
            lambda t: np.array(
                [
                    t,
                    0.5 * np.sin(t * 0.5 * PI),
                    0,
                ]
            ),
            t_range=[2, 10],
            color=BLUE,
        )

        wave_to_left = ParametricFunction(
            lambda t: np.array(
                [
                    -t,
                    0.5 * np.sin(t * 0.5 * PI),
                    0,
                ]
            ),
            t_range=[2, 10],
            color=BLUE,
        )

        self.play(
            ReplacementTransform(group, text, run_time=1),
            Create(wave_to_right),
            Create(wave_to_left),
        )

        self.play(
            wave_to_right.animate.set_opacity(0),
            wave_to_left.animate.set_opacity(0),
            run_time=0.5,
        )

        self.play(ReplacementTransform(text, text_2, run_time=1))

        header = Tex("Warum der Verbindungsvektor", font_size=30)
        body_1 = MathTex("\\circ \\text{ Direkt und anschaulich}", font_size=30)
        body_2 = MathTex(
            "\\circ \\text{ Verwendung grundlegender Vektorrechnung}", font_size=30
        )
        body_3 = MathTex("\\circ \\text{ Effizient}", font_size=30)

        # This groups the elements together, placing them in a downward direction
        wow = VGroup(
            header,
            body_1,
            body_2,
            body_3,
        )
        wow.move_to(ORIGIN)
        wow.arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(
            LaggedStart(*[FadeIn(mob, shift=UP) for mob in wow]),
        )
        self.wait(5)

        self.play(
            FadeOut(wow),
            FadeOut(text_2),
        )

        self.wait(1)


class Mitte_zwei(Scene):
    def construct(self):
        self.fps = 60

        tools_text = Tex("Werkzeuge", font_size=50).move_to(ORIGIN)
        self.play(Write(tools_text))

        self.wait(1)

        self.play(
            tools_text.animate.scale(0.8).shift(UP * 3),
        )

        chest_closed_png = ImageMobject("Assets\\resized-chest_1-removebg-preview.png")
        chest_opened_empty_png = ImageMobject("Assets\\resized_chest_2.png")

        chest_closed_png.move_to(ORIGIN)
        chest_opened_empty_png.move_to(ORIGIN)

        self.play(FadeIn(chest_closed_png))

        self.play(ReplacementTransform(chest_closed_png, chest_opened_empty_png))

        skalarprodukt_text = Tex("Skalarprodukt", font_size=25).move_to(ORIGIN)
        self.play(
            Write(skalarprodukt_text),
            skalarprodukt_text.animate.move_to(LEFT * 4 + UP * 3),
        )

        self.wait(1)

        skalarprodukt_group = VGroup()

        start_vec = LEFT * 4 + UP * 3
        skalarprodukt_vektor_1 = Arrow(
            start=start_vec, end=start_vec + [-1, -3, 0], color=RED
        )
        skalarprodukt_vektor_2 = Arrow(
            start=start_vec, end=start_vec + [-3, 1, 0], color=BLUE
        )

        start_dot = Dot(point=start_vec, color=WHITE, radius=0.25)

        angle = Angle(
            Line(
                start=skalarprodukt_vektor_1.get_start(),
                end=skalarprodukt_vektor_1.get_end(),
            ),
            Line(
                start=skalarprodukt_vektor_2.get_start(),
                end=skalarprodukt_vektor_2.get_end(),
            ),
            radius=1,
            other_angle=True,
        )

        angle_dot = Dot(point=angle.get_center(), color=WHITE)

        skalarprodukt_group = VGroup(
            skalarprodukt_vektor_1, skalarprodukt_vektor_2, angle, start_dot, angle_dot
        )
        skalarprodukt_group.scale(0.5)

        self.play(ReplacementTransform(skalarprodukt_text, skalarprodukt_group))

        self.wait(1)

        knowledge_text = Tex("Lotgerade", font_size=25).move_to(ORIGIN)
        self.play(
            Write(knowledge_text),
            knowledge_text.animate.move_to(RIGHT * 4 + DOWN * 2),
        )

        lotgerade_group = VGroup()

        lotgerade_eins = Line(start=[0, 0, 0], end=[0, -2, 0], color=RED)
        lotgerade_zwei = Line(start=[-2, -2, 0], end=[2, -2, 0], color=BLUE)

        angle = Angle(
            Line(
                start=lotgerade_eins.get_end(),
                end=lotgerade_eins.get_start(),
            ),
            Line(
                start=lotgerade_zwei.get_end(),
                end=lotgerade_zwei.get_start(),
            ),
            radius=1,
            other_angle=False,
        )

        angle_dot_skalar = Dot(point=angle.get_center(), color=WHITE)

        lotgerade_group.add(lotgerade_eins, lotgerade_zwei, angle, angle_dot_skalar)
        lotgerade_group.scale(0.5)
        lotgerade_group.move_to(RIGHT * 4 + DOWN * 2)

        self.play(ReplacementTransform(knowledge_text, lotgerade_group))

        self.wait(2)

        self.play(
            FadeOut(skalarprodukt_group),
            FadeOut(lotgerade_group),
            FadeOut(chest_opened_empty_png),
            FadeOut(tools_text),
        )

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
        self.wait(5)

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

        self.wait(5)

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
        self.play(FadeOut(fourth_connection_vec))
        self.wait(25)

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

        self.wait(20)

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

        self.play(ReplacementTransform(half_scalar_product_g, lambda_solution))
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

        self.wait(2)

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

        self.wait(5)

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

        self.play(
            ReplacementTransform(point_g_line, complete_point_g_line),
            complete_point_g_line.animate.set_opacity(1),
        )

        self.wait(2)

        self.play(
            point_h_line[1].animate.set_color(YELLOW),
            point_h_line[3].animate.set_color(YELLOW),
            point_h_line[5].animate.set_color(YELLOW),
        )

        complete_point_h_line = (
            MathTex(
                r"P_h = (-2 - 7 \cdot (-0,17) \mid -1 + 3 \cdot (-0,17) \mid 2 + 0,17)",
                color=GREEN,
                font_size=25,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN * 3)
            .set_opacity(0)
        )

        self.add_fixed_in_frame_mobjects(complete_point_h_line)

        self.play(
            ReplacementTransform(point_h_line, complete_point_h_line),
            complete_point_h_line.animate.set_opacity(1),
        )

        self.wait(5)

        point_g = (
            MathTex(
                r"P_g = (0,07 \mid -1,72 \mid 0)",
                color=BLUE,
                font_size=25,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN)
        )

        point_h = (
            MathTex(
                r"P_h = (-0,81 \mid -1,51 \mid 2,17)",
                color=GREEN,
                font_size=25,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN * 1.5)
        )

        self.begin_ambient_camera_rotation(rate=0.1, about="theta")

        self.add_fixed_in_frame_mobjects(point_g, point_h)
        self.play(
            FadeOut(lambda_solution),
            FadeOut(mu_solution),
            FadeOut(complete_point_g_line),
            FadeOut(complete_point_h_line),
            Write(point_g),
            Write(point_h),
        )

        g_point_3d = Dot3D(
            axes.coords_to_point(0.07, -1.72, 0), color=WHITE, radius=0.07
        )
        h_point_3d = Dot3D(
            axes.coords_to_point(-0.81, -1.51, 2.17), color=WHITE, radius=0.07
        )

        self.play(Create(g_point_3d), Create(h_point_3d))

        self.stop_ambient_camera_rotation(about="theta")

        self.wait(2)

        distance_vec = (
            MathTex(
                r"\vec{P_gP_h} = \begin{pmatrix} -0,81 - 0,07 \\ -1,51 + 1,72 \\ 2,17 - 0 \end{pmatrix}",
                font_size=25,
                color=WHITE,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN * 2.5)
        )

        distance_vec_short = (
            MathTex(
                r"\vec{P_gP_h} = \begin{pmatrix} -0,88 \\ 0,21 \\ 2,17 \end{pmatrix}",
                font_size=25,
                color=WHITE,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN * 2.5)
        )

        self.add_fixed_in_frame_mobjects(distance_vec)
        self.play(Write(distance_vec))

        self.wait(10)

        self.play(
            ReplacementTransform(distance_vec, distance_vec_short),
        )
        self.add_fixed_in_frame_mobjects(distance_vec_short)

        distance_arrow = Arrow3D(
            start=g_point_3d.get_center(),
            end=h_point_3d.get_center(),
            color=WHITE,
        )

        self.play(Create(distance_arrow))

        self.wait(5)

        length_distance = (
            MathTex(
                r"s = \sqrt{(-0,88)^2 + (0,21)^2 + (2,17)^2}",
                font_size=25,
                color=WHITE,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN * 4)
        )

        self.add_fixed_in_frame_mobjects(length_distance)
        self.play(Write(length_distance))

        length_complete = (
            MathTex(
                r"\sqrt{(-0,88)^2 + (0,21)^2 + (2,17)^2} \approx 2,35",
                font_size=25,
                color=YELLOW,
            )
            .to_corner(UP + LEFT)
            .shift(DOWN * 4)
        )

        self.play(ReplacementTransform(length_distance, length_complete))
        self.add_fixed_in_frame_mobjects(length_complete)

        self.play(distance_arrow.animate.set_color(YELLOW))

        self.wait(10)


class Schluss(Scene):
    def construct(self):
        self.fps = 30

        music_credits = Tex("Musik: Sixes von Vincent Rubinetti", font_size=50).move_to(
            ORIGIN
        )

        self.play(
            Write(music_credits),
        )

        self.wait(2)

        self.play(
            music_credits.animate.shift(UP * 2).scale(0.5),
        )

        code_credits = Tex("Animationen geschrieben in Python", font_size=50).move_to(
            ORIGIN
        )

        self.play(
            Write(code_credits),
        )

        self.wait(2)

        self.play(
            code_credits.animate.shift(UP).scale(0.5),
        )

        self.wait(2)
