from manim import *


class Hilfsebene(ThreeDScene):
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

        line_1 = Line3D(start=[3, 0, -1], end=[-3, 0, -1], color=BLACK)
        line_2 = Line3D(start=[0, -3, 1], end=[0, 3, 1], color=BLACK)

        line_1_label = MathTex("g", color=BLACK).scale(0.5).next_to(line_1.get_start())
        line_2_label = (
            MathTex("h", color=BLACK)
            .scale(0.5)
            .next_to(line_2.get_end())
            .shift(0.2 * RIGHT)
        )

        plane = Surface(
            lambda u, v: axes.coords_to_point(6 * (1 - u) - 5 * u, v, -1),
            u_range=[0, 1],
            v_range=[-5, 5],
            checkerboard_colors=[BLUE_D, BLUE_E],
        )
        plane.set_opacity(0.3)

        plane_label = MathTex("E", color=BLACK).scale(0.5).next_to(plane, 0.5 * DOWN).shift(0.5 * RIGHT)

        self.add_fixed_orientation_mobjects(line_1_label, line_2_label, plane_label)
        self.add(line_1, line_2, plane)