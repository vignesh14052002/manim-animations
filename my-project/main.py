from manim import *

class DefaultTemplate(MovingCameraScene):
    def create_node(self, label, **kwargs):
        circle = Circle(**kwargs)

        lines = label.split("\n")
        if len(lines) > 1:
            text = Paragraph(*lines, alignment="center", font_size=24)
        else:
            text = Text(label, font_size=24)

        text.next_to(circle, DOWN)
        return VGroup(circle, text)
    
    def construct(self):
        # self.play_high_level_agent_workflow()
        # return



        query_generator = self.create_node("Query\nGenerator", color=BLUE, radius=0.5).shift(LEFT * 4)
        document_retriever = self.create_node("Document\nRetriever", color=BLUE, radius=0.5).shift(LEFT * 4)
        context_filter = self.create_node("Context\nFilter", color=BLUE, radius=0.5)
        answer_generator = self.create_node("Answer\nGenerator", color=BLUE, radius=0.5)
        document_retriever.next_to(query_generator, RIGHT, buff=2)
        context_filter.next_to(document_retriever, RIGHT, buff=2)
        answer_generator.next_to(context_filter, RIGHT, buff=2)
        # connect the two node's circles with an arrow
        arrow = Arrow(query_generator[0].get_right(), document_retriever[0].get_left())
        arrow1 = Arrow(document_retriever[0].get_right(), context_filter[0].get_left())
        arrow2 = Arrow(context_filter[0].get_right(), answer_generator[0].get_left())
        self.add(arrow, arrow1, arrow2)
        self.add(query_generator, document_retriever, context_filter, answer_generator)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=1).move_to(query_generator[0]))
        user_query = Paragraph("How much revenue our company","made last quarter?", alignment="center", font_size=24)
        retrieval_query = Text("Google's 2025 Q1 Revenue", font_size=24).next_to(user_query, DOWN, buff=1)
        a1 = Arrow(user_query.get_bottom(), retrieval_query.get_top(), buff=0.2)
        a1.set_stroke(width=1)
        query_group = VGroup(user_query, retrieval_query, a1)
        query_group.scale_to_fit_width(self.camera.frame.get_width() * 0.8)  # fit inside zoomed view
        query_group.move_to(self.camera.frame.get_center())#.shift(0.25 * self.camera.frame.get_width() * UP)
        
        self.play(Write(user_query))
        self.play(GrowArrow(a1))
        self.play(Write(retrieval_query))

    def play_high_level_agent_workflow(self):
        user_query = Text("User Query", font_size=24).shift(3 * LEFT)

        ai_bot = SVGMobject(
            "./assets/ai-bot.svg", stroke_color=WHITE, stroke_width=4
        ).set(height=1.5)
        database = SVGMobject(
            "./assets/database.svg", stroke_color=WHITE, stroke_width=4
        ).set(height=1.5)

        # Lay out left -> right to avoid overlap
        ai_bot.next_to(user_query, RIGHT, buff=2.0)
        database.next_to(ai_bot, RIGHT, buff=2.0)

        db_label = Text("Knowledge Base", font_size=24).next_to(database, DOWN)

        arrow1 = Arrow(user_query.get_right(), ai_bot.get_left(), buff=0.2)
        arrow2 = Arrow(ai_bot.get_right(), database.get_left(), buff=0.2)

        self.play(FadeIn(ai_bot))
        self.wait(1)
        self.play(FadeIn(database),Write(user_query), Write(db_label))
        self.wait(1)
        self.play(GrowArrow(arrow1))
        self.play(GrowArrow(arrow2))
        # Fade out all elements
        self.wait(1)
        self.play(
            FadeOut(user_query),
            FadeOut(ai_bot),
            FadeOut(database),
            FadeOut(db_label),
            FadeOut(arrow1),
            FadeOut(arrow2),
        )
        