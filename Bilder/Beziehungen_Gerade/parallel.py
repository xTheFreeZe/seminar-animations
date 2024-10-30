from manim import *


# manim -ql -p Bilder/Beziehungen_Gerade/parallel.py Parallel -r 1920,1080

class Parallel(ThreeDScene):
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

        z_label = MathTex("z", color=BLACK).next_to(axes.z_axis.get_end(), UP * 0.9, buff=0.3)

        # (1, 2, 3) + t * (1, 0 , 2)
        start_point_g1 = [1, 2, 3]
        direction_g1 = [1, 0, 2]
        line_g1 = Line3D(
            start=[start_point_g1[i] - 10 * direction_g1[i] for i in range(3)],
            end=[start_point_g1[i] + 10 * direction_g1[i] for i in range(3)],
            color=BLACK,
            thickness=0.02,
            show_ends=False,
        )

        start_point_g2 = [3, 2, 1]
        direction_g2 = [1, 0, 2]
        line_g2 = Line3D(
            start=[start_point_g2[i] - 10 * direction_g2[i] for i in range(3)],
            end=[start_point_g2[i] + 10 * direction_g2[i] for i in range(3)],
            color=BLACK,
            thickness=0.02,
            show_ends=False,
        )

        # Rotate the letters OF THE AXES to make them readable
        x_label.rotate(PI / 2, axis=RIGHT).rotate(PI*0.9, axis=OUT)
        y_label.rotate(PI / 2, axis=RIGHT).rotate(PI*0.9, axis=OUT)
        z_label.rotate(PI / 2, axis=RIGHT).rotate(PI*0.9, axis=OUT)

        g1_label = MathTex("g_1", color=BLACK).next_to(line_g1, UP, buff=0.2)
        g2_label = MathTex("g_2", color=BLACK).next_to(line_g2, DOWN, buff=0.2)

        g1_label.rotate(PI / 2, axis=RIGHT).rotate(PI*0.9, axis=OUT)
        g2_label.rotate(PI / 2, axis=RIGHT).rotate(PI*0.9, axis=OUT)

        self.set_camera_orientation(phi=80 * DEGREES, theta=40 * DEGREES)

        g1_label.scale(0.8)
        g2_label.scale(0.8)

        self.add(axes, line_g1, line_g2)
        self.add(x_label, y_label, z_label)
        self.add(g1_label, g2_label)
        self.wait(10)
