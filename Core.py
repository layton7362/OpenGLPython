from __future__ import annotations
from Input import Input
from copy import copy, deepcopy
import numpy as np
from OpenGL.GL import *
from typing import List, Callable
import glm
from math import sin
import glfw
import Util
from enum import Enum
from Const import * 


class Base():
    def __init__(self) -> None:
        pass
    
    def dispose():
        pass

class Node(Base):
    
    def __init__(self) -> None:
        super().__init__()
        self.name: str = ""
        self.is_in_scene = False
    
    def update(self, delta: float):
        pass
    
    def dispose(self):
        pass    

class Node3D(Node):
    def __init__(self) -> None:
        super().__init__()
        # self.pos = glm.vec3
        # self.scale = glm.vec3
        # self.rot = glm.mat3x4
        self.transformation: glm.mat4 = glm.mat4(
            1,0,0,0,
            0,1,0,0,
            0,0,1,0,
            0,0,0,1
        )
    
        # self.scaleIt(glm.vec3(0.5))
        # self.trans(glm.vec3(0.001,0,0))
        
    def scaleIt(self, factor: glm.vec3):
        self.transformation *= glm.scale(factor)
    
    def translateIt(self, positon: glm.vec3):
        self.transformation *= glm.translate(positon)
        
    def rotIt(self, angle: glm.float32,axis: glm.vec3): 
        dd = glm.rotate(angle, axis )
        self.transformation *= glm.rotate(angle, axis )
     
     
class Object3D(Node3D):
    
    def __init__(self) -> None:
        super().__init__()
        self.mesh: Base_Mesh = None
        self.material: Base_Material = None
        self.uniforms: map[str, any] = {}
    
    def update(self, delta):
        super().update(delta)
        # self.rotIt((0.01), glm.vec3(1,0,0))
        
        if Input.is_pressed(glfw.KEY_A):
            self.trans(glm.vec3(0,1,0))      
            pass
        if Input.is_pressed(glfw.KEY_D):
            self.trans(glm.vec3(0,-1,0))      
        
        self.mesh.material.uniforms["time"] = sin(glfw.get_time() * 2)
        self.mesh.material.uniforms["matrix"] = self.transformation
    
    def set_mesh(self, mesh):
        self.mesh = mesh
        
class Resource(Base):
    def __init__(self) -> None:
        super().__init__()
        self.counter = 0

class Base_Shader(Resource):
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

class Base_Material(Resource):
    def __init__(self, shaders: List[Base_Shader], dispose_shader = True, uniforms: map[str, any] = None) -> None:
        super().__init__()
        
        self.program = glCreateProgram()
        self.uniforms = uniforms
        
        if not shaders[ShaderData.VERTEX.value] or not shaders[ShaderData.FRAGMENT.value]:
            raise ValueError("Vertex or Fragment Shader are missing!")
        for shader in shaders:
            if shader:
                glAttachShader(self.program, shader.get_shader())
        glLinkProgram(self.program)
        if dispose_shader:
            for shader in shaders:
                if shader:
                    shader.dispose()
        
        if not glGetProgramiv(self.program , GL_LINK_STATUS):
            print("ERROR::SHADER::PROGRAM::LINKING_FAILED")
            print(glGetProgramInfoLog(self.program ))
    
    def use(self):
        glUseProgram(self.program)
        for key in self.uniforms:
            value = self.uniforms[key]
            uniform_location: int = glGetUniformLocation(self.program, key)
            _type = type(value)
            if _type == float:
                glUniform1f(uniform_location, value)
            elif _type == glm.mat4:
                glUniformMatrix4fv(uniform_location, 1, GL_FALSE, glm.value_ptr(value))
        
    def dispose(self):
        glDeleteProgram(self.program)     
    
class Base_Mesh(Resource):
    def __init__(self, meshData: List[List]) -> None:
        super().__init__()
        if len(meshData) < len(MeshData):
            raise ValueError("MeshData Array to short!")
        self.verts = meshData[MeshData.VERTEX.value]
        # self.normals = meshData[MeshData.NORMAL.value]
        # self.colors = meshData[MeshData.COLOR.value]
        # self.uv1 =  meshData[MeshData.UV1.value]
        # self.uv2 =  meshData[MeshData.UV2.value]
        # self.indices = meshData[MeshData.INDEX.value]
        
        self.vert_count: int = int(len(self.verts) / 3)
        self.material: Base_Material = None

        self.build()

    def build(self):
        self.VAO = glGenVertexArrays(1)
        self.VBO = glGenBuffers(1)
        glBindVertexArray(self.VAO)
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBufferData(GL_ARRAY_BUFFER,glm.sizeof(glm.float32) * len(self.verts), self.verts, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), None)
        glEnableVertexAttribArray(0)    
        glBindBuffer(GL_ARRAY_BUFFER, 0) 
    
    def update_vertices(self, vertices):
        self.verts = Util.to_float_array(vertices)
        self.vert_count = int(len(self.verts) / 3)
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBufferData(GL_ARRAY_BUFFER,glm.sizeof(glm.float32) * len(self.verts),self.verts, GL_STATIC_DRAW)
        glBindBuffer(GL_ARRAY_BUFFER, 0) 
        
    def set_material(self, material: Base_Material):
        self.material = material
        return self
    
    def get_vertices(self):
        return self.verts
    
    def get_vertices_count(self):
        return self.vert_count
    
    def bind(self):
        glBindVertexArray(self.VAO)
    
    def dispose(self):
        # TODO FIX
        glDeleteVertexArrays(1, self.VAO)
        glDeleteBuffers(1, self.VBO)

    def draw(self, type = GL_TRIANGLES):
        self.material.use()
        self.bind()
        glDrawArrays(type, 0, self.get_vertices_count())     
    
    def draw_element(self, type = GL_TRIANGLES):
        self.material.use()
        self.bind()
        glDrawElements(type, 0, self.get_vertices_count())     
    pass

class Base_SceneTree(Base):
    def __init__(self) -> None:
        super().__init__()
        self.delta: float = 0
        self.nodes: List[Node] = list()
        self.renderObjects: List[Object3D] = list()
        self.deferred_calls : List[Callable] = list()
        self.scene: GameScene = None
        
    def load_scene(self, scene: GameScene):
        self.scene = scene
        self.scene.init()
    
    def add_node(self, node: Node):
        if self.nodes.count(node) == 0:
            self.nodes.append(node)
            if isinstance(node, Object3D):
                mesh = node
                if (node.mesh):
                    self.renderObjects.append(node)
                    self.renderer.add_mesh(node)
    
    def remove_node(self, node: Node):
        if self.nodes.count(node):
            self.nodes.remove(node)    
            if type(node) is Object3D:
                if (node.mesh and self.renderObjects.count(node)):
                    self.renderObjects.remove(node)
                    self.renderer.delete_mesh(node)
    
    def main_update(self):
        self.scene.update(self.delta)
        for node in self.nodes:
            node.update(self.delta)

    def main_deferred(self):
        for call in self.deferred_calls:
            call()
        self.deferred_calls.clear()
        
    def scene_dispose(self):
        self.scene.dispose()
        for object in self.renderObjects:
            self.dispose_object(object)

    def render(self):
        pass
    
    def dispose_object(self, object: Object3D):
        pass
    
    def dispose(self):
        self.scene_dispose()
    
class GameScene(Base):
    
    def __init__(self, tree: Base_SceneTree) -> None:
        super().__init__()
        self.tree = tree
    
    def init(self):
        pass
    
    def update(self, delta: float):
        pass
    
    def dispose(self):
        pass