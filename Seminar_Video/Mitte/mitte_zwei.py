from manim import *


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
