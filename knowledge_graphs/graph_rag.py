from manim import *


class GraphRAGScene(Scene):
    def construct(self):
        audio_file = "./assets/audio/graphrag.m4a"
        self.add_sound(audio_file, time_offset=0.5)
        ai_bot = SVGMobject("./assets/ai-bot.svg", fill_color=BLUE, height=1.25)
        ai_bot.to_edge(LEFT, buff=1)
        ai_bot.move_to([ai_bot.get_center()[0], 0, 0])

        get_schema_text = Paragraph("get_schema","()->str", font_size=24, color=WHITE)
        execute_query_text = Paragraph("execute_query","(query: str) -> list", font_size=24, color=WHITE)

        get_schema_text.move_to(LEFT * 2 + UP * 1.5)
        execute_query_text.move_to(LEFT * 2 + DOWN * 1.5)

        wire_to_schema = Arrow(
            start=ai_bot.get_right() + RIGHT * 0.06,
            end=get_schema_text.get_left() + LEFT * 0.08,
            buff=0.05,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.06,
            color=BLUE_B,
        )
        wire_to_query = Arrow(
            start=ai_bot.get_right() + RIGHT * 0.06,
            end=execute_query_text.get_left() + LEFT * 0.08,
            buff=0.05,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.06,
            color=BLUE_B,
        )

        self.play(FadeIn(ai_bot), run_time=1.0)
        self.wait(5)
        self.play(
            Write(get_schema_text),Create(wire_to_schema), run_time=1)
        self.play(
            Write(execute_query_text),
            Create(wire_to_query),
            run_time=1,
        )
        self.wait(1)
        self.play(Indicate(get_schema_text, color=YELLOW, scale_factor=1.07))

        kg_schema = [
            """Node Properties:
- Person (20) : (name:str, age:int)
- Company (3) : (name:str, industry:str)
""",
            """
Relationship Properties:
- KNOWS : (since:date)
- WORKS_AT : (role:str)
""",
            """
Relationships:
- (Person)-[:KNOWS]->(Person)
- (Person)-[:WORKS_AT]->(Company)
""",
        ]

        schema_blocks = VGroup(
            *[
                Text(block.strip(), font_size=20, color=WHITE, line_spacing=0.8)
                for block in kg_schema
            ]
        )
        schema_blocks.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        schema_blocks.move_to(RIGHT * 3)

        self.wait(2)
        self.play(Write(schema_blocks[0]), run_time=1)
        self.wait(5)
        self.play(Write(schema_blocks[1]), run_time=1)
        self.wait(3)
        self.play(Write(schema_blocks[2]), run_time=1)

        self.wait(2)
        self.play(FadeOut(schema_blocks, shift=UP * 0.15), run_time=0.65)

     

        query_text = Text(
            "MATCH (p:Person)-[:WORKS_AT]->(c:Company)\n"
            "RETURN p.name, c.name\n"
            "LIMIT 3",
            font_size=21,
            color=GREY_A,
        )
        query_text.move_to(RIGHT * 3)

        result_table = Table(
            [["Vignesh", "Soliton"], ["Vishal", "Zoho"], ["Kumar","Google"]],
            col_labels=[Text("p.name", font_size=24), Text("c.name", font_size=24)],
            include_outer_lines=True,
            line_config={"stroke_color": BLUE_B, "stroke_width": 2},
            element_to_mobject=lambda s: Text(str(s), font_size=24, color=WHITE),
        )
        result_table.scale(0.8)
        result_table.move_to(RIGHT * 3)

        self.play(Write(query_text), run_time=0.85)
        self.wait(2)
        self.play(Indicate(execute_query_text, color=YELLOW, scale_factor=1.05))

        self.play(ReplacementTransform(query_text, result_table), run_time=1.0)

        self.wait(4)
