from OpenGL.GL import *
from Log import WARNING, INFO, ERROR
from Core import Object3D, Base_Mesh, Base_Material, Base_Shader
import glm
from enum import Enum

class RenderType(Enum):
    TRIANGLE_FAN = GL_TRIANGLE_FAN,
    TRIANGLES = GL_TRIANGLES

class Renderer:
        
    def __init__(self) -> None:
        self._render_ids: map[Object3D, id] = {}

    def get_render_id(self, object: Object3D) -> int:
        if object in self._render_ids:
            return self._render_ids[object]
        else:
            return None

    def add_material(self, material: Base_Material):
        pass
    
    def add_mesh(self, object: Object3D):
        if object in self._render_ids:
            WARNING("Mesh has render id:" + object)
        
        mesh: Base_Mesh =  object.mesh
        
        VAO = glGenVertexArrays(1)
        VBO = glGenBuffers(1)
        glBindVertexArray(VAO)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER,glm.sizeof(glm.float32) * len(mesh.verts), mesh.verts, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), None)
        glEnableVertexAttribArray(0)    
        glBindBuffer(GL_ARRAY_BUFFER, 0) 
        
        self._render_ids[object] = VAO
    
    def delete_mesh(self, object: Object3D):
        # TODO
        pass
    
    def render_begin():
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
    
    
    def render(self, object: Object3D, type: RenderType):
        
        if object not in self._render_ids:
            WARNING("Object has no renderId: " + object )
            return -1
        
        VAO: int =  self._render_ids[object]
        mesh: Base_Mesh = object.mesh
        count = mesh.get_vertices_count()
        mesh.material.use()
        
        self.set_uniforms(object)
        
        glBindVertexArray(VAO)
        glDrawArrays(type.value, 0, count)     
    
    def set_uniforms(self, object: Object3D):
        uniforms = object.uniforms
        # object.material 
        for location in uniforms:
            value = uniforms[location]
            match(type(value)):
                case glm.float32:
                    glUniform1f(location, value)
                case glm.int32:
                    glUniform1i(location, value)
                case glm.Mat4:
                    glUniformMatrix4fv(location, 1, GL_FALSE, glm.value_ptr(value))