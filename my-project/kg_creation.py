from functools import partial

from manim import *

ManimText = Text
Text = partial(ManimText, font="Segoe UI")

class KGCreation(Scene):
    def construct(self):
        vignesh_circle = Circle(radius=0.6, color=BLUE, fill_color=BLUE, fill_opacity=0.2)
        vignesh_circle.move_to(LEFT * 3)
        vignesh_name = Text("Vignesh", font_size=20, color=BLUE)
        vignesh_name.move_to(vignesh_circle.get_center())
        vignesh_prop = Text("age:24", font_size=22, color=BLUE)
        vignesh_prop.next_to(vignesh_circle, DOWN, buff=0.25)
        vignesh_node_type = Text("Person", font_size=18, color=BLUE)
        vignesh_node_type.next_to(vignesh_circle, UP, buff=0.25)

        raghul_circle = Circle(radius=0.6, color=BLUE, fill_color=BLUE, fill_opacity=0.2)
        raghul_circle.move_to(RIGHT * 0.6)
        raghul_name = Text("Raghul", font_size=20, color=BLUE)
        raghul_name.move_to(raghul_circle.get_center())
        raghul_prop = Text("age:30", font_size=22, color=BLUE)
        raghul_prop.next_to(raghul_circle, DOWN, buff=0.25)
        raghul_node_type = Text("Person", font_size=18, color=BLUE)
        raghul_node_type.next_to(raghul_circle, UP, buff=0.25)

        relation_arrow = Arrow(
            start=vignesh_circle.get_right(),
            end=raghul_circle.get_left(),
            buff=0.1,
            color=YELLOW,
            stroke_width=4,
        )
        relation_label = Text("friend_of", font_size=22, color=YELLOW)
        relation_label.next_to(relation_arrow, UP, buff=0.1)
        relation_prop = Text("place:office", font_size=20, color=YELLOW)
        relation_prop.next_to(relation_arrow, DOWN, buff=0.1)

        self.play(FadeIn(VGroup(vignesh_circle, vignesh_name, raghul_circle, raghul_name)), run_time=0.8)
        self.play(FadeIn(vignesh_node_type, raghul_node_type), run_time=0.5)
        self.play(FadeIn(vignesh_prop,raghul_prop), run_time=0.5)
        self.play(Create(relation_arrow), FadeIn(relation_label), run_time=0.8)
        self.play(FadeIn(relation_prop), run_time=0.5)
        self.wait(0.5)

        graph_group = VGroup(
            vignesh_circle,
            vignesh_name,
            vignesh_prop,
            vignesh_node_type,
            raghul_circle,
            raghul_name,
            raghul_prop,
            relation_arrow,
            relation_label,
            relation_prop,
            raghul_node_type
        )

        self.play(graph_group.animate.shift(LEFT * 2 + UP * 2.5), run_time=1.0)

        cypher_title = Text("Neo4j Cypher", font_size=28, color=WHITE)
        cypher_title.to_edge(RIGHT, buff=3).shift(LEFT * 1.2 + UP * 3)

        create_text1 = Text("CREATE", font_size=16, color=WHITE)
        create_text1.next_to(cypher_title, DOWN, buff=0.5).align_to(cypher_title, LEFT)
        q1 = Paragraph(
            '(v:Person{name:"Vignesh",age:24})',
            '-[:FRIEND_OF{place:"office"}]->',
            '(r:Person{name:"Raghul",age:30})',
            font_size=16,
            line_spacing=1.1,
        )
        q1.next_to(create_text1, RIGHT, buff=0.3, aligned_edge=UP)
        create_text2 = Text("CREATE", font_size=16, color=WHITE)
        create_text2.next_to(q1, DOWN, buff=0.5).align_to(cypher_title, LEFT)
        q2 = Paragraph(
            '(v:Person{name:"Vignesh",age:24})',
            '-[:FRIEND_OF{place:"college"}]->',
            '(k:Person{name:"Kumar",age:24})',
            font_size=16,
            line_spacing=1.1,
        )
        q2.next_to(create_text2, RIGHT, buff=0.3, aligned_edge=UP)
        self.play(Write(cypher_title), run_time=0.6)
        self.play(Write(create_text1), run_time=0.5)
        self.play(
            TransformFromCopy(
                VGroup(
                    vignesh_circle,
                    vignesh_name,
                    vignesh_prop,
                    relation_arrow,
                    relation_label,
                    relation_prop,
                    raghul_circle,
                    raghul_name,
                    raghul_prop,
                ),
                q1,
            ),
            run_time=1.2,
        )
        self.wait(0.6)

        kumar_circle = Circle(radius=0.6, color=BLUE, fill_color=BLUE, fill_opacity=0.2)
        kumar_circle.move_to(vignesh_circle.get_center() + DOWN * 2.5 + RIGHT * 0.4)
        kumar_name = Text("Kumar", font_size=20, color=BLUE)
        kumar_name.move_to(kumar_circle.get_center())
        kumar_prop = Text("age:24", font_size=22, color=BLUE)
        kumar_prop.next_to(kumar_circle, DOWN, buff=0.25)

        relation2_arrow = Arrow(
            start=vignesh_circle.get_bottom(),
            end=kumar_circle.get_top(),
            buff=0.1,
            color=YELLOW,
            stroke_width=4,
        )
        relation2_label = Text("friend_of", font_size=20, color=YELLOW)
        relation2_label.next_to(relation2_arrow, LEFT, buff=0.1).shift(DOWN * 0.1)
        relation2_prop = Text("place:college", font_size=20, color=YELLOW)
        relation2_prop.next_to(relation2_arrow, RIGHT, buff=0.12).shift(DOWN * 0.1)

        self.play(FadeIn(VGroup(kumar_circle, kumar_name)), run_time=0.8)
        self.play(FadeIn(kumar_prop), run_time=0.5)
        self.play(Create(relation2_arrow), FadeIn(relation2_label), run_time=0.8)
        self.play(FadeIn(relation2_prop), run_time=0.5)

        self.play(Write(create_text2), run_time=0.5)
        self.play(
            TransformFromCopy(
                VGroup(
                    vignesh_circle,
                    vignesh_name,
                    vignesh_prop,
                    relation2_arrow,
                    relation2_label,
                    relation2_prop,
                    kumar_circle,
                    kumar_name,
                    kumar_prop,
                ),
                q2,
            ),
            run_time=1.2,
        )


        data_type = Text("Structured Data", font_size=30, color=WHITE)
        data_type.move_to(DOWN * 1.5)

        table_box = SVGMobject("./assets/database.svg",height=1.2, stroke_width=4, stroke_color=BLUE)
        table_box.move_to(LEFT * 4 + DOWN * 2.8)
        table_text = Text("Table", font_size=24, color=WHITE)
        table_text.next_to(table_box, DOWN, buff=0.2)

        script_box = SVGMobject("./assets/script-file.svg", color=BLUE, fill_color=BLUE, height=1.2, stroke_width=1)
        script_box.move_to(DOWN * 2.8)
        script_text = Text("Script", font_size=24, color=WHITE)
        script_text.next_to(script_box, DOWN, buff=0.2)

        cypher_box = Rectangle(width=2, height=1.1, color=BLUE)
        cypher_box.move_to(RIGHT * 4 + DOWN * 2.8)
        cypher_box_text = Text("Cypher", font_size=22, color=WHITE)
        cypher_box_text.move_to(cypher_box.get_center())

        arrow_1 = Arrow(start=table_box.get_right(), end=script_box.get_left(), buff=0.15, color=YELLOW)
        arrow_2 = Arrow(start=script_box.get_right(), end=cypher_box.get_left(), buff=0.15, color=YELLOW)

        self.play(Create(table_box), Write(table_text), run_time=0.6)
        self.play(Create(arrow_1), Create(script_box), Write(script_text), run_time=0.7)
        self.play(Create(arrow_2), Create(cypher_box), Write(cypher_box_text), run_time=0.7)

        unstructured_data = Text("Unstructured Data", font_size=30, color=WHITE)
        unstructured_data.move_to(data_type.get_center())
        document_box = SVGMobject("./assets/document.svg", color=BLUE, fill_color=BLUE, height=1.2)
        document_box.move_to(table_box.get_center())
        document_text = Text("Document", font_size=24, color=WHITE)
        document_text.next_to(document_box, DOWN, buff=0.2)
        ai_box = SVGMobject("./assets/ai-bot.svg", color=BLUE, fill_color=BLUE, height=1.2)
        ai_box.move_to(script_box.get_center())
        ai_text = Text("AI", font_size=24, color=WHITE)
        ai_text.next_to(ai_box, DOWN, buff=0.2)

        self.play(Transform(data_type, unstructured_data), run_time=1.0)
        self.play(Transform(table_text, document_text),Transform(table_box, document_box), run_time=1.0)
        self.play(
            Transform(script_text, ai_text),
            Transform(script_box, ai_box),
            run_time=1.0,
        )
        self.wait(1.0)