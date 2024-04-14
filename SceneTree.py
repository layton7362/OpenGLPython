import Core
import typing 
from OpenGL.GL import *

class SceneTree(Core.Base_SceneTree):
    
    def __init__(self) -> None:
        super().__init__()
        
        self.nodes: typing.List[Core.Base_Node] = list()
        self.meshes: typing.List[Core.Base_Mesh] = list()
        
        self.deferred_calls : typing.List[typing.Callable] = list()

        
    
    def load_scene(self, file):
        with open(file, 'r') as data:
            code = data.read()
            eval(code)
        pass
    
    def add_node(self, node: Core.Node):
        if self.nodes.count(node) == 0:
            self.nodes.append(node)
            if isinstance(node, Core.Mesh3D):
                mesh = node
                if (node.mesh):
                    self.meshes.append(node.mesh)
    
    def remove_node(self, node: Core.Node):
        if self.nodes.count(node):
            self.nodes.remove(node)    
            if type(node) is Core.Mesh3D:
                if (node.mesh and self.meshes.count(node.mesh)):
                    self.meshes.remove(node.mesh)
    
    def main_update(self):
        for node in self.nodes:
            node.update()
            
    def render(self):
               
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        for mesh in self.meshes:
            mesh.draw()
            
    def main_deferred(self):
        for call in self.deferred_calls:
            call()
        self.deferred_calls.clear()
