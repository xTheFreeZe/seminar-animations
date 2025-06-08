from manim import *


class Spat(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE

        axes = ThreeDAxes(
            x_length=5,
            y_length=5,
            z_length=5,
            x_axis_config={"color": BLUE},
            y_axis_config={"color": RED},
            z_axis_config={"color": GREEN},
        )

        x_label = (
            MathTex("x", color=BLACK).next_to(axes.get_x_axis().get_end()).scale(0.7)
        )
        y_label = (
            MathTex("y", color=BLACK)
            .next_to(axes.get_y_axis().get_end())
            .scale(0.7)
            .shift(0.2 * UP)
        )
        z_label = (
            MathTex("z", color=BLACK).next_to(axes.get_z_axis().get_end()).scale(0.7)
        )

        self.add_fixed_orientation_mobjects(x_label, y_label, z_label)
        self.add(axes)
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES)

        a = np.array([2, 0, 0])
        b = np.array([0, 2, 0])
        c = np.array([1, 1, 2])

        vec_a = Arrow3D(start=ORIGIN, end=a, color=BLACK)
        vec_b = Arrow3D(start=ORIGIN, end=b, color=BLACK)
        vec_c = Arrow3D(start=ORIGIN, end=c, color=BLACK)

        vec_a_label = MathTex("\\vec{a}", color=BLACK).scale(0.5).next_to(vec_a.get_end()).shift(0.2 * RIGHT + 0.3 * DOWN)
        vec_b_label = MathTex("\\vec{b}", color=BLACK).scale(0.5).next_to(vec_b.get_end()).shift(0.3 * RIGHT)
        vec_c_label = MathTex("\\vec{c}", color=BLACK).scale(0.5).next_to(vec_c.get_end())

        self.add_fixed_orientation_mobjects(vec_a_label, vec_b_label, vec_c_label)

        self.add(vec_a, vec_b, vec_c)

        lines = VGroup(
            Line(a, a + b, color=GRAY),
            Line(a + b, b, color=GRAY),
            Line(b, ORIGIN, color=GRAY),
            Line(a, a + c, color=GRAY),
            Line(a + b, a + b + c, color=GRAY),
            Line(a + c, a + b + c, color=GRAY),
            Line(ORIGIN, c, color=GRAY),
            Line(b, b + c, color=GRAY),
            Line(c, a + c, color=GRAY),
            Line(b + c, a + b + c, color=GRAY),
            Line(c, b+c, color=GRAY),
        )

        self.add(lines)