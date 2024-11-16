from manim import *


class Windschief(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE

        axes = ThreeDAxes(
            x_length=7,
            y_length=7,
            z_length=7,
            x_axis_config={"color": BLUE},
            y_axis_config={"color": RED},
            z_axis_config={"color": GREEN},
        )

        x_label = MathTex("x", color=BLACK).next_to(
            axes.x_axis.get_end(), RIGHT, buff=0.3
        )

        y_label = MathTex("y", color=BLACK).next_to(
            axes.y_axis.get_end(), LEFT * 1.1, buff=0.3
        )

        z_label = MathTex("z", color=BLACK).next_to(
            axes.z_axis.get_end(), UP * 0.9, buff=0.3
        )

        start_point_g1 = [1, -2, 1]
        direction_g1 = [2, 2, 1]
        line_g1 = Line3D(
            start=[start_point_g1[i] - 10 * direction_g1[i] for i in range(3)],
            end=[start_point_g1[i] + 10 * direction_g1[i] for i in range(3)],
            color=BLACK,
            thickness=0.02,
            show_ends=False,
        )

        start_point_g2 = [3, -3, 0]
        direction_g2 = [0, 3, 1]
        line_g2 = Line3D(
            start=[start_point_g2[i] - 10 * direction_g2[i] for i in range(3)],
            end=[start_point_g2[i] + 10 * direction_g2[i] for i in range(3)],
            color=BLACK,
            thickness=0.01,
            show_ends=False,
        )

        g1_label = MathTex("g_1", color=BLACK).next_to([2, -2, 1.5], UP, buff=0.2)
        g2_label = MathTex("g_2", color=BLACK).next_to([2, -2, -0.3], DOWN, buff=0.2)

        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES)

        g1_label.scale(0.8)
        g2_label.scale(0.8)

        self.add(axes)
        self.add(line_g1, line_g2)
        self.add(x_label, y_label, z_label)
        self.add(g1_label, g2_label)

        x_label.rotate(PI / 2, axis=RIGHT).rotate(PI * 0.6, axis=OUT)
        y_label.rotate(PI / 2, axis=RIGHT).rotate(PI * 0.6, axis=OUT)
        z_label.rotate(PI / 2, axis=RIGHT).rotate(PI * 0.6, axis=OUT)
        g1_label.rotate(PI / 2, axis=RIGHT).rotate(PI * 0.6, axis=OUT)
        g2_label.rotate(PI / 2, axis=RIGHT).rotate(PI * 0.6, axis=OUT)

        self.wait(10)
