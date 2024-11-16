from manim import *


class Ebene(ThreeDScene):
    def construct(s):
        s.camera.background_color = WHITE
        s.set_camera_orientation(phi=60 * DEGREES, theta=30 * DEGREES)

        axes = ThreeDAxes(
            x_length=5,
            y_length=5,
            z_length=5,
            x_axis_config={"color": BLUE},
            y_axis_config={"color": RED},
            z_axis_config={"color": GREEN},
        )

        def plane(u, v):
            return axes.c2p(
                u,  # x-kooordinate
                v,  # y-kooordinate
                1,  # z-kooordinate (fest)
            )

        plane_surface = Surface(
            plane,
            u_range=[-5, 5],
            v_range=[-5, 5],
            checkerboard_colors=[BLUE_D, BLUE_E],
        )

        plane_surface.set_opacity(0.4)

        # Aufpunkt
        point = [0, 0, 1]
        vec_to_point = Arrow3D(
            start=[0, 0, 0], end=point, color=BLACK, stroke_width=0.5
        )

        # Richtungsvektoren
        vec1 = Arrow3D(
            start=point,
            end=[point[0] + 2.5, point[1], point[2]],
            color=BLACK,
            stroke_width=0.5,
        )
        vec2 = Arrow3D(
            start=point,
            end=[point[0], point[1] + 2.5, point[2]],
            color=BLACK,
            stroke_width=0.5,
        )

        dot = Dot3D(point, color=BLACK, radius=0.08)

        plane_label = MathTex("E", color=BLACK).scale(0.5)
        dot_label = MathTex("P", color=BLACK).scale(0.5)
        vec_label = MathTex("\\vec{v}", color=BLACK).scale(0.5)
        vec1_label = MathTex("\\vec{a}", color=BLACK).scale(0.5)
        vec2_label = MathTex("\\vec{b}", color=BLACK).scale(0.5)

        s.add(axes)
        s.add(plane_surface)
        s.add(vec_to_point, vec1, vec2, dot)

        s.add_fixed_in_frame_mobjects(plane_label)
        s.add_fixed_in_frame_mobjects(dot_label)
        s.add_fixed_in_frame_mobjects(vec_label)
        s.add_fixed_in_frame_mobjects(vec1_label)
        s.add_fixed_in_frame_mobjects(vec2_label)

        group = VGroup(axes, plane_surface, vec_to_point, vec1, vec2, dot)
        group.scale(1.2)

        plane_label.shift(LEFT * 2.5, UP * 2)
        dot_label.shift(UP * 1.5, RIGHT * 0.3)
        vec_label.shift(UP * 0.5, RIGHT * 0.3)
        vec1_label.shift(UP * 1, RIGHT * 1.5)
        vec2_label.shift(UP * 0.8, LEFT * 1.3)                
