from manim import *

# Enthält die erste Szene des Videos nach der Einleitung

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
