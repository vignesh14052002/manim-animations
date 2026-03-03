from manim import *

class KGVectorStoreComparisonScene(Scene):
    def construct(self):
        kg_circle = Circle(radius=1.0, color=BLUE, fill_color=BLUE, fill_opacity=0.2)
        vs_circle = Circle(radius=1.0, color=GREEN, fill_color=GREEN, fill_opacity=0.3)

        kg_label = Text("Knowledge Graph", font_size=28, color=BLUE)
        vs_label = Text("Vector Store", font_size=28, color=GREEN)

        kg_group = VGroup(kg_circle, kg_label)
        vs_group = VGroup(vs_circle, vs_label)

        kg_label.next_to(kg_circle, DOWN, buff=0.3)
        vs_label.next_to(vs_circle, DOWN, buff=0.3)

        kg_group.to_edge(LEFT, buff=4)
        vs_group.to_edge(RIGHT, buff=4)

        self.play(FadeIn(kg_group))
        self.wait(1)
        self.play(FadeIn(vs_group))
        self.wait(1)

        kg_outer = Circle(radius=2.1, color=BLUE, fill_color=BLUE, fill_opacity=0.18)
        vs_inner = Circle(radius=1.0, color=GREEN, fill_color=GREEN, fill_opacity=0.35)

        kg_outer.move_to(ORIGIN)
        vs_inner.move_to(ORIGIN)

        kg_label_center = Text("Knowledge Graph", font_size=30, color=BLUE)
        vs_label_center = Text("Vector Store", font_size=24, color=GREEN)

        kg_label_center.next_to(kg_outer, DOWN, buff=0.25)
        vs_label_center.next_to(vs_inner, DOWN, buff=0.25)

        self.play(
            Transform(kg_circle, kg_outer),
            Transform(vs_circle, vs_inner),
            Transform(kg_label, kg_label_center),
            Transform(vs_label, vs_label_center),
            run_time=1,
        )

        self.wait(1)

class VectorStoreKGStructureScene(Scene):
    def construct(self):
        pdf_rect = RoundedRectangle(
            width=5.0,
            height=2.0,
            corner_radius=0.15,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.15,
        )
        pdf_title = Text("Document", font_size=34, color=BLUE)
        pdf_group = VGroup(pdf_rect, pdf_title)

        self.play(FadeIn(pdf_group), run_time=1)
        self.wait(0.5)

        chunks = VGroup(
            *[
                RoundedRectangle(
                    width=2,
                    height=0.75,
                    corner_radius=0.08,
                    color=BLUE,
                    fill_color=BLUE,
                    fill_opacity=0.15,
                )
                for _ in range(5)
            ]
        )
        chunks.arrange(DOWN, buff=0.5)
        chunks.move_to(LEFT * 3.5)

        chunk_labels = VGroup(*[Text(f"Chunk {i+1}", font_size=22, color=BLUE) for i in range(5)])
        for label, rect in zip(chunk_labels, chunks):
            label.move_to(rect.get_center())

        chunk_group = VGroup(chunks, chunk_labels)

        self.play(Transform(pdf_group, chunk_group), run_time=1.6)
        self.wait(0.5)

        embeddings_text = [
            "[0.2, ... ,0.8]",
            "[0.9, ... ,0.6]",
            "[0.3, ... ,0.2]",
            "[0.5, ... ,0.9]",
            "[0.1, ... ,0.4]",
        ]
        embeddings = VGroup(*[Text(text, font_size=22, color=WHITE) for text in embeddings_text])
        metadatas_text = [
            "Page: 1",
            "Page: 1",
            "Page: 2",
            "Page: 3",
            "Page: 4",
        ]
        metadatas = VGroup(*[Text(text, font_size=18, color=WHITE) for text in metadatas_text])
        for emb, rect, meta in zip(embeddings, chunks, metadatas):
            if emb == embeddings[0]:
                emb.next_to(rect, RIGHT, buff=1)
                self.play(TransformFromCopy(rect, emb), run_time=0.8)
                meta.next_to(emb, RIGHT, buff=0.3)
                self.play(FadeIn(meta), run_time=0.8)
                self.wait(1)
            else:
                emb.next_to(rect, RIGHT, buff=1)
                self.play(TransformFromCopy(rect, emb), run_time=0.5)
                meta.next_to(emb, RIGHT, buff=0.3)
                self.play(FadeIn(meta), run_time=0.5)

        vector_store_text = Text("Vector Store", font_size=30, color=GREEN)
        vector_store_text.to_edge(DOWN, buff=0.6)

        self.play(Write(vector_store_text), run_time=0.8)
        self.wait(0.5)

        next_arrows = VGroup()
        next_labels = VGroup()
        for i in range(4):
            start = chunks[i].get_bottom()
            end = chunks[i + 1].get_top()
            arrow = Arrow(start, end, buff=0.05, color=YELLOW, stroke_width=4)
            label = Text("NEXT_TO", font_size=15, color=YELLOW)
            label.next_to(arrow, LEFT, buff=0.15)
            next_arrows.add(arrow)
            next_labels.add(label)

        refers_arrow_1 = CurvedArrow(
            start_point=chunks[3].get_left() + LEFT * 0.05,
            end_point=chunks[0].get_left() + LEFT * 0.05,
            angle=-PI / 2,
            color=ORANGE,
            stroke_width=4,
        )
        refers_label_1 = Text("REFERS_TO", font_size=15, color=ORANGE)
        refers_label_1.next_to(refers_arrow_1, LEFT, buff=0.2)

        refers_arrow_2 = CurvedArrow(
            start_point=chunks[4].get_right() + RIGHT * 0.05,
            end_point=chunks[2].get_right() + RIGHT * 0.05,
            angle=PI / 2,
            color=ORANGE,
            stroke_width=4,
        )
        refers_label_2 = Text("REFERS_TO", font_size=15, color=ORANGE)
        refers_label_2.next_to(refers_arrow_2, RIGHT, buff=0.2)
        refers_label_2.shift(DOWN * 0.5)

        self.play(
            LaggedStart(*[Create(arrow) for arrow in next_arrows], lag_ratio=0.15),
            LaggedStart(*[FadeIn(label) for label in next_labels], lag_ratio=0.15),
            run_time=1.8,
        )

        self.play(
            Create(refers_arrow_1),
            Create(refers_arrow_2),
            FadeIn(refers_label_1),
            FadeIn(refers_label_2),
            run_time=1.6,
        )

        knowledge_graph_text = Text("Knowledge Graph", font_size=30, color=BLUE)
        knowledge_graph_text.move_to(vector_store_text.get_center())
        self.play(Transform(vector_store_text, knowledge_graph_text), run_time=1)
        self.wait(1)

        dim_overlay = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_opacity=0,
        )
        dim_overlay.set_z_index(1)
        self.play(FadeIn(dim_overlay), run_time=0.8)
        query_text_parts = [
            """collect chunks which is
similar to search term""",
            "gather all the references,",
            "expand the chunk selection",
            "if they belong to same page",
        ]
        query_text = VGroup(*[Text(part, font_size=22, color=WHITE) for part in query_text_parts])
        query_text.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        query_text.set_z_index(2)
        query_text.to_edge(RIGHT, buff=2).shift(UP * 0.5)
        self.play(Write(query_text), run_time=4)

        cypher_query_parts = ["""
CALL db.index.vector.queryNodes(
'index_name', 5, $query_vector) 
YIELD node AS startChunk
""",
"""
MATCH (startChunk)-[:refers_to]->(ref)
WITH collect(startChunk)+collect(ref) AS seeds
""",
"""
UNWIND seeds AS seed
MATCH (seed)-[:next_to]-(expanded)
""",
"""
WHERE expanded.page_num = seed.page_num
RETURN DISTINCT expanded
"""
        ]
        
        for i, part in enumerate(cypher_query_parts):
            part_text = Text(part, font_size=18, color=WHITE)
            part_text.move_to(query_text[i].get_center()).align_to(query_text[i], LEFT)

            self.play(Transform(query_text[i], part_text), run_time=1.5)
            self.wait(0.5)
        for i in range(len(cypher_query_parts)):
            if i > 0:
                self.play(query_text[i].animate.set_z_index(0), run_time=0.1)
  
        self.play(embeddings[3].animate.set_z_index(2), run_time=0.9)
        self.play(
            VGroup(chunks[3], chunk_labels[3]).animate.set_z_index(2),
            run_time=0.9,
        )
        self.play(query_text[1].animate.set_z_index(2), run_time=0.5)
        self.play(
            VGroup(refers_arrow_1, refers_label_1).animate.set_z_index(2),
            run_time=0.9,
        )
        self.play(
            VGroup(chunks[0], chunk_labels[0]).animate.set_z_index(2),
            run_time=0.9,
        )
        self.play(query_text[2].animate.set_z_index(2), run_time=0.5)
        
        self.play(
            VGroup(next_arrows[0], next_labels[0]).animate.set_z_index(2),
            VGroup(chunks[1], chunk_labels[1]).animate.set_z_index(2),
            VGroup(next_arrows[3], next_labels[3]).animate.set_z_index(2),
            VGroup(chunks[4], chunk_labels[4]).animate.set_z_index(2),
            run_time=1.3,
        )
        self.play(query_text[3].animate.set_z_index(2), run_time=0.5)
        

        self.play(
            VGroup(metadatas[0], metadatas[1], metadatas[3]).animate.set_z_index(2),
            run_time=1.3,
        )
        disabled_chunk_5 = VGroup(
            chunks[4],
            chunk_labels[4],
            embeddings[4],
            metadatas[4],
            next_arrows[3],
            next_labels[3],
        )
        self.play(disabled_chunk_5.animate.set_z_index(0), run_time=1)
        self.wait(1)

