from typing import List 
from OpenGL.GL import *
import Core

class Shader(Core.Resource):
    def __init__(self, path, type: int ) -> None:
        self.path = path
        self.code = ""
        self.genId = -1
        self.shader = -1
        self.type = type
        with open(path,'r') as data:
            self.code = data.read()

        self.shader = glCreateShader(self.type)
        glShaderSource(self.shader, self.code)
        glCompileShader(self.shader)
        
        if not glGetShaderiv(self.shader, GL_COMPILE_STATUS):
            print("ERROR::SHADER::VERTEX::COMPILATION_FAILED")
            print(glGetShaderInfoLog(self.shader))
        
    
    def get_shader(self):
        return self.shader
    
    def get_path(self):
        return self.path
    
    def dispose(self):
        glDeleteShader(self.shader)

    
class ShaderVertex(Shader):
    def __init__(self, path) -> None:
        super().__init__(path, GL_VERTEX_SHADER)
 
        
class ShaderFragment(Shader):
    def __init__(self, path) -> None:
        super().__init__( path, GL_FRAGMENT_SHADER)
        
        
class Material(Core.Base_Material):
    def __init__(self, shaders: List[Shader], dispose = True, uniforms: map = None) -> None:
        self.program = glCreateProgram()
        for shader in shaders:
            glAttachShader(self.program, shader.get_shader())
        glLinkProgram(self.program)
        if dispose:
            for shader in shaders:
                shader.dispose()
        
        if not glGetProgramiv(self.program , GL_LINK_STATUS):
            print("ERROR::SHADER::PROGRAM::LINKING_FAILED")
            print(glGetProgramInfoLog(self.program ))
        
    def use(self):
        glUseProgram(self.program)
    
    def dispose(self):
        glDeleteProgram(self.program)     
    
class DefaultMaterial(Material):
    def __init__(self) -> None:
        shaders: List[Shader] = list()
        vs = ShaderVertex("shaders/basic.vert")
        fs = ShaderFragment("shaders/basic.frag")
        super().__init__([vs,fs])