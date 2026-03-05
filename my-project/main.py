from manim import *
from .kg_vecstore_comparison import KGVectorStoreComparisonScene, VectorStoreKGStructureScene

class MainScene(Scene):
    def construct(self):
        KGVectorStoreComparisonScene.construct(self)
        # clear the scene for next one
        self.clear()
        self.wait(1)
        VectorStoreKGStructureScene.construct(self)