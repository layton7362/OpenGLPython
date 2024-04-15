
from typing import List 
from OpenGL.GL import *
import Core
import glfw
from math import sin

class Shader(Core.Base_Shader):
    pass
    
class ShaderVertex(Shader):
    def __init__(self, path) -> None:
        super().__init__(path, GL_VERTEX_SHADER)
 
        
class ShaderFragment(Shader):
    def __init__(self, path) -> None:
        super().__init__( path, GL_FRAGMENT_SHADER)
        
class ShaderGeometry(Shader):
    def __init__(self, path) -> None:
        super().__init__( path, GL_GEOMETRY_SHADER)
     
class Material(Core.Base_Material):
    def __init__(self, shaders: List[Shader], dispose = True, uniforms: map = None) -> None:
        super().__init__(shaders, dispose, uniforms)

        
class DefaultMaterial(Material):
    def __init__(self) -> None:
        shaders: List[Shader] = [None for i in range(len(Core.ShaderData))]
        shaders[Core.ShaderData.VERTEX.value] = ShaderVertex("shaders/basic.vert")
        shaders[Core.ShaderData.FRAGMENT.value] = ShaderFragment("shaders/basic.frag")
        # shaders[Core.ShaderData.GEOMETRY.value] = ShaderGeometry("shaders/basic.gs")
        super().__init__(shaders, True, {"time": sin(glfw.get_time()) })