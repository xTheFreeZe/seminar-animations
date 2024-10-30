from manim import *


class Video(ThreeDScene):
    def construct(s):
        s.fps = 60
        title = Tex("Seminarvideo Marwin Eder ft13a", font_size=30)
        topic = Tex("Abstand zweier", " windschiefer", " Geraden", font_size=25)

        s.play(Write(title))
        s.wait()

        transform_title = Tex("Thema:", font_size=25)
        transform_title.to_corner(UP + LEFT)

        s.play(Transform(title, transform_title))
        s.wait(0.5)
        s.play(Write(topic))

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

        # Group the elements and arrange them vertically with a specific spacing
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
        s.wait(5)

        s.play(
            ReplacementTransform(framebox_one, framebox_two),
            LaggedStart(*[FadeOut(mob, shift=DOWN) for mob in skew_definition]),
        )
        s.wait()

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

        s.wait(2)

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

        s.wait(2)

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
            start=[-3, 0, -1],
            end=[3, 4, 2],
            color=BLUE,
        )

        line_two_skew = Line3D(
            start=[2, -3, 3],
            end=[-2, 2, -1],
            color=RED,
        )

        group_three = VGroup(axes_three, line_one_skew, line_two_skew)
        group_three.scale(0.2).move_to(RIGHT * 4)
        s.play(LaggedStart(*[FadeIn(mob, shift=UP) for mob in group_three]))

        s.wait(2)

        # Start rotating the group
        s.play(Rotating(group_one, axis=UP, radians=2 * PI, run_time=3))
        s.wait(2)
        s.play(Rotating(group_two, axis=UP, radians=2 * PI, run_time=3))
        s.wait(2)
        s.play(Rotating(group_three, axis=UP, radians=2 * PI, run_time=3))
        s.wait(5)
