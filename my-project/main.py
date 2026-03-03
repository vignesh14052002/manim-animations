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
            height=3.0,
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
                    width=3.2,
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
        chunks.move_to(LEFT * 2)

        chunk_labels = VGroup(*[Text(f"Chunk {i+1}", font_size=24, color=BLUE) for i in range(5)])
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
            "Page: 3",
        ]
        metadatas = VGroup(*[Text(text, font_size=18, color=WHITE) for text in metadatas_text])
        for emb, rect, meta in zip(embeddings, chunks, metadatas):
            if emb == embeddings[0]:
                emb.next_to(rect, RIGHT, buff=1)
                self.play(TransformFromCopy(rect, emb), run_time=0.8)
                meta.next_to(emb, RIGHT, buff=0.5)
                self.play(FadeIn(meta), run_time=0.8)
                self.wait(1)
            else:
                emb.next_to(rect, RIGHT, buff=1)
                self.play(TransformFromCopy(rect, emb), run_time=0.5)
                meta.next_to(emb, RIGHT, buff=0.5)
                self.play(FadeIn(meta), run_time=0.5)

        vector_store_text = Text("Vector Store", font_size=36, color=GREEN)
        vector_store_text.to_edge(DOWN, buff=0.6)

        self.play(Write(vector_store_text), run_time=0.8)
        self.wait(0.5)

        next_arrows = VGroup()
        next_labels = VGroup()
        for i in range(4):
            start = chunks[i].get_bottom()
            end = chunks[i + 1].get_top()
            arrow = Arrow(start, end, buff=0.05, color=YELLOW, stroke_width=4)
            label = Text("NEXT_TO", font_size=20, color=YELLOW)
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
        refers_label_1 = Text("REFERS_TO", font_size=20, color=ORANGE)
        refers_label_1.next_to(refers_arrow_1, LEFT, buff=0.2)

        refers_arrow_2 = CurvedArrow(
            start_point=chunks[4].get_right() + RIGHT * 0.05,
            end_point=chunks[2].get_right() + RIGHT * 0.05,
            angle=PI / 2,
            color=ORANGE,
            stroke_width=4,
        )
        refers_label_2 = Text("REFERS_TO", font_size=20, color=ORANGE)
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

        knowledge_graph_text = Text("Knowledge Graph", font_size=36, color=BLUE)
        knowledge_graph_text.move_to(vector_store_text.get_center())
        self.play(Transform(vector_store_text, knowledge_graph_text), run_time=1)
        self.wait(1)
