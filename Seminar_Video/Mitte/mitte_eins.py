from manim import *


class Mitte_eins(ThreeDScene):
    def construct(s):
        s.fps = 60

        axes = ThreeDAxes(
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

        group = VGroup(axes, line_one_skew, line_two_skew)
        group.scale(0.2)
        group.scale(1.8)
        s.add(group)
        s.wait(2)

        # Das tatsächliche Video beginnt jetzt
        # Bis hier hin war nur das Koordanensystem und die Linien
        # der Einleitung. Somit herrscht ein reibungsloser Übergang

        skew_line_pairs = [
            (
                Line3D(start=[-6, -4, -8], end=[6, 2, -2], color=GREEN),
                Line3D(start=[-3, 4, 2], end=[5, -4, 10], color=ORANGE),
            ),
            (
                Line3D(start=[-7, -2, -6], end=[7, 4, -4], color=PURPLE),
                Line3D(start=[-2, 6, 3], end=[4, -6, 9], color=YELLOW),
            ),
            (
                Line3D(start=[-8, -5, -9], end=[8, 5, -3], color=PINK),
                Line3D(start=[-5, 3, 1], end=[3, -3, 8], color=MAROON),
            ),
            (
                Line3D(start=[-4, -3, -5], end=[6, 3, -1], color=TEAL),
                Line3D(start=[-3, 5, 4], end=[5, -5, 11], color=GOLD),
            ),
            (
                Line3D(start=[-7, -6, -4], end=[7, 2, 0], color=YELLOW),
                Line3D(start=[-2, 4, 5], end=[4, -4, 12], color=GRAY),
            ),
            (
                Line3D(start=[-6, -4, -7], end=[6, 3, -2], color=BLUE),
                Line3D(start=[-1, 7, 4], end=[3, -7, 10], color=RED),
            ),
            (
                Line3D(start=[-5, -2, -8], end=[5, 2, -5], color=PINK),
                Line3D(start=[-4, 3, 6], end=[4, -3, 15], color=GREEN),
            ),
            (
                Line3D(start=[-6, -3, -9], end=[6, 4, -3], color=TEAL_B),
                Line3D(start=[-3, 6, 2], end=[5, -6, 8], color=PURE_BLUE),
            ),
            (
                Line3D(start=[-8, -4, -10], end=[8, 4, -4], color=ORANGE),
                Line3D(start=[-5, 4, 7], end=[3, -4, 13], color=BLUE),
            ),
        ]

        def play_lines():
            prev_line_1 = Line3D()
            prev_line_2 = Line3D()
            # group = VGroup(axes, line_one_skew, line_two_skew, prev_line_1, prev_line_2)
            for i, (line_1, line_2) in enumerate(skew_line_pairs):
                line_1.scale(0.2).scale(1.8)
                line_2.scale(0.2).scale(1.8)

                if i == 0:
                    s.play(
                        ReplacementTransform(line_one_skew, line_1),
                        ReplacementTransform(line_two_skew, line_2),
                    )
                    prev_line_1 = line_1
                    prev_line_2 = line_2
                else:
                    s.play(
                        ReplacementTransform(prev_line_1, line_1),
                        ReplacementTransform(prev_line_2, line_2),
                    )
                    prev_line_1 = line_1
                    prev_line_2 = line_2
                # s.play(Rotating(group, axis=UP, radians=2 * PI, run_time=2))

        play_lines()

        s.wait(5)
