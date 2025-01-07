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