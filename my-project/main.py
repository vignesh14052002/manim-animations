from manim import *
from kg_vecstore_comparison import KGVectorStoreComparisonScene, VectorStoreKGStructureScene
from kg_creation import KGCreation
from graph_rag import GraphRAGScene
from summary import SummaryScene
class MainScene(Scene):
    def construct(self):
        KGVectorStoreComparisonScene.construct(self)
        # clear the scene for next one
        self.clear()
        self.wait(1)
        VectorStoreKGStructureScene.construct(self)
        self.clear()
        self.wait(1)
        KGCreation.construct(self)
        self.clear()
        self.wait(1)
        GraphRAGScene.construct(self)
        self.clear()
        self.wait(1)
        SummaryScene.construct(self)