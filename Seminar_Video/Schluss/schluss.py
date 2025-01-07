from manim import *


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
