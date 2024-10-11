from manim import *

# This will be a simple picture scnene, no animations

# Terminal command for rendering this manim scene at 60fps and 1080p resolution
# manim -pql main.py VekorenBild -r 1920,1080


class VekorenBild(ThreeDScene):
    def construct(self):

        # Change background color to white
        self.camera.background_color = WHITE

        axes = ThreeDAxes(
            x_length=7,
            y_length=7,
            z_length=7,
            x_axis_config={"color": RED},
            y_axis_config={"color": GREEN},
            z_axis_config={"color": BLUE},
        )

        self.play(Create(axes), run_time=1)
        vektor = Arrow3D([0, 0, 0], [1, 2, 3], color=BLACK)
        dot = Dot(ORIGIN, color="Black")
        x_label = MathTex("y", color=BLACK).next_to(axes.x_axis.get_end(), RIGHT, buff=0.2)
        y_label = MathTex("z", color=BLACK).next_to(axes.y_axis.get_end(), LEFT, buff=0.2)
        z_label = MathTex("x", color=BLACK).next_to(axes.z_axis.get_end(), UP, buff=0.2)
        origin_text = Text("(0, 0, 0)", color=BLACK).next_to(dot, DOWN).scale(0.5)
        tip_text = Text("(1, 2, 3)", color=BLACK).next_to(vektor.get_end(), RIGHT).scale(0.5)

        self.play(Create(vektor), Create(dot), run_time=1)

        axis_and_lines = VGroup(axes, vektor, dot, x_label, y_label, z_label)
        self.play(axis_and_lines.animate.rotate(angle=PI / 6, axis=UP))
        self.play(axis_and_lines.animate.rotate(angle=-PI / 12, axis=LEFT))

        self.play(Create(origin_text), Create(tip_text), run_time=1)
        self.wait(6)
