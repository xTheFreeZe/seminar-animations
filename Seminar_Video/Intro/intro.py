from manim import *


class Intro(ThreeDScene):
    def construct(s):
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

        s.play(Create(framebox_one))
        s.wait()

        skew_definition_header = Tex("Voraussetzungen windschief", font_size=30)
        skew_definition_one = MathTex("\\times \\text{ ...}", font_size=30)
        skew_definition_two = MathTex("\\times \\text{ ...}", font_size=30)
        skew_definition_three = MathTex("\\times \\text{ ...}", font_size=30)

        # Group the elements and arrange them vertically with a specific spacing
        skew_definition = VGroup(
            skew_definition_header,
            skew_definition_one,
            skew_definition_two,
            skew_definition_three,
        )
        skew_definition.arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        s.play(Write(skew_definition))
        s.wait()

        s.play(ReplacementTransform(framebox_one, framebox_two))
        s.wait()
