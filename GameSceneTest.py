import Mesh
import Core
import Material
import glm

class GameSceneTest(Core.GameScene):
    
    def __init__(self, tree: Core.Base_SceneTree):
        super().__init__(tree)
    
    def init(self):
        
        cube = Mesh.Cube().set_material(Material.DefaultMaterial())
        self.node1 = Core.Object3D()
        self.node1.scaleIt(
            glm.vec3(0.2,1,1)
            )
        self.node1.mesh = cube
        self.node1.name = "One"
        
        cube = Mesh.Triangle2D().set_material(Material.DefaultMaterial())
        self.node2 = Core.Object3D()
        self.node2.mesh = cube
        self.node2.name = "Two"
        
        self.tree.add_node(self.node1)
        self.tree.add_node(self.node2)
        
    def update(self, delta):
        self.node1.scaleIt(
            glm.vec3(1 * delta,1,1)
            )
        pass
        
        
