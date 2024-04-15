import Core
from RenderEngine import RenderType, Renderer

class SceneTree(Core.Base_SceneTree):
    def __init__(self) -> None:
        super().__init__()
        self.renderer: Renderer = Renderer()
        
        from GameSceneTest import GameSceneTest
        self.load_scene(GameSceneTest(self))
    
    def render(self):
        for renderObject in self.renderObjects:
            self.renderer.render(renderObject, RenderType.TRIANGLES)
            