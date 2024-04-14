from copy import copy, deepcopy
import numpy as np
from OpenGL.GL import *
from typing import List
import glm
import Util

class MeshData(enumerate):
    VERTEX = 0
    NORMAL = 1
    COLOR = 2
    UV1 = 3
    UV2 = 4
    INDEX = 5


class Base():
    def __init__(self) -> None:
        pass
    
    def dispose():
        pass

class Node(Base):
    
    def __init__(self) -> None:
        super().__init__()
        
        self.is_in_scene = False
    
    def update(self):
        pass
    
    def dispose():
        pass    

class Actor3D(Node):
    def __init__(self) -> None:
        super().__init__()
        self.pos = glm.vec3
        self.scale = glm.vec3
        self.rot = glm.mat3x4
     
class Mesh3D(Actor3D):
    
    def __init__(self) -> None:
        super().__init__()
        self.mesh = None
        
    def set_mesh(self, mesh):
        self.mesh = mesh
        
class Resource(Base):
    def __init__(self) -> None:
        super().__init__()
        self.counter = 0

class Base_Material(Resource):
    pass

class Base_Mesh(Resource):
    def __init__(self, verts, normals = None, indices = None, colors = None) -> None:
        super().__init__()
        self.verts = Util.to_float_array(verts)
        self.vert_count: int = int(len(self.verts) / 3)
        self.normals = normals
        self.colors = colors
        self.indices = indices
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
    
    def translate(self, translation):
        for i in range(0, len(self.verts),3):
            self.verts[i] += translation[0]
            self.verts[i+1] += translation[1]
            self.verts[i+2] += translation[2]
        self.update_vertices(self.verts)
        return self
    
    def scale(self, scale_factors):
        for i in range(0, len(self.verts), 3):
            self.verts[i] *= scale_factors[0]
            self.verts[i + 1] *= scale_factors[1]
            self.verts[i + 2] *= scale_factors[2]
        self.update_vertices(self.verts)
        return self
    
    def rotate(self, angle, axis):
        c = np.cos(angle)
        s = np.sin(angle)
        x, y, z = axis / np.linalg.norm(axis)
        rotation_matrix = np.array([[c + x**2*(1-c), x*y*(1-c) - z*s, x*z*(1-c) + y*s],
                                    [y*x*(1-c) + z*s, c + y**2*(1-c), y*z*(1-c) - x*s],
                                    [z*x*(1-c) - y*s, z*y*(1-c) + x*s, c + z**2*(1-c)]])
        for i in range(0, len(self.verts), 3):
            v = np.array(self.verts[i:i+3])  # Vertices als Spaltenvektor
            v_rotated = np.dot(rotation_matrix, v)  # Rotation anwenden
            self.verts[i:i+3] = v_rotated  # Ergebnis speichern
        self.update_vertices(self.verts)
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
    pass

class Base_SceneTree(Base):
    pass


