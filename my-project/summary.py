from manim import *

class SummaryScene(Scene):
    def construct(self):
        audio_file = "./assets/audio/summary.m4a"
        self.add_sound(audio_file, time_offset=0.5)
        data_box = RoundedRectangle(
            width=3,
            height=1.2,
            corner_radius=0.18,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.15,
        )
        data_label = Text("Data", font_size=38, color=BLUE)
        data_group = VGroup(data_box, data_label)
        data_group.to_edge(LEFT, buff=1.2)

        qdrant = SVGMobject("./assets/qdrant.svg", height=1.1)
        neo4j = SVGMobject("./assets/neo4j.svg", height=0.8, fill_color=BLUE)
        postgres = SVGMobject("./assets/postgresql1.svg", height=1.1, fill_color=BLUE)

        qdrant.to_edge(RIGHT, buff=1.3).shift(UP * 2.0)
        neo4j.to_edge(RIGHT, buff=1.3)
        postgres.to_edge(RIGHT, buff=1.3).shift(DOWN * 2.0)

        arrow_to_qdrant = Arrow(
            start=data_box.get_right(),
            end=qdrant.get_left(),
            buff=0.15,
            color=YELLOW,
            stroke_width=4,
        )
        arrow_to_neo4j = Arrow(
            start=data_box.get_right(),
            end=neo4j.get_left(),
            buff=0.15,
            color=YELLOW,
            stroke_width=4,
        )
        arrow_to_postgres = Arrow(
            start=data_box.get_right(),
            end=postgres.get_left(),
            buff=0.15,
            color=YELLOW,
            stroke_width=4,
        )

        unstructured_label = Text("un structured", font_size=24, color=YELLOW)
        semi_structured_label = Text("semi-structured", font_size=24, color=YELLOW)
        structured_label = Text("structured", font_size=24, color=YELLOW)

        unstructured_label.next_to(arrow_to_qdrant, UP, buff=0.1).shift(DOWN).rotate(15 * DEGREES)
        semi_structured_label.next_to(arrow_to_neo4j, UP, buff=0.1).shift(RIGHT)
        structured_label.next_to(arrow_to_postgres, DOWN, buff=0.1).shift(UP).rotate(-15 * DEGREES)

        self.wait(3)
        self.play(FadeIn(data_group), run_time=0.8)
        self.play(Write(arrow_to_qdrant), Write(unstructured_label), run_time=1)
        self.wait(3)
        self.play(FadeIn(qdrant), run_time=1)
        self.wait(1)
        self.play(Write(arrow_to_postgres), Write(structured_label), run_time=1)
        self.wait(1)
        self.play(FadeIn(postgres), run_time=0.8)
        self.wait(1)
        self.play(Create(arrow_to_neo4j), Write(semi_structured_label), run_time=1)
        self.wait(2)
        self.play(FadeIn(neo4j), run_time=1)
        self.wait(1)
        