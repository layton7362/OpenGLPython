from Const import * 
from OpenGL.GL import *
import Util
from Core import Base_Mesh, Base_Material, MeshData

class Mesh(Base_Mesh):
    pass

class Cube(Mesh):
    def __init__(self, size = 1.0, color=(1.0, 1.0, 1.0)) -> None:
        
        meshData = [None for i in range(len(MeshData))]
        
        meshData[MeshData.VERTEX.value] = Util.to_float_array([
            size,  size, size,  # top right
            size, -size, size,  # bottom right
            -size, -size, size,  # bottom left
            -size,  size, size   # top left 
        ])
        meshData[MeshData.INDEX.value] = Util.to_float_array([  # note that we start from 0!
            0, 1, 3,   # first triangle
            1, 2, 3    # second triangle
        ])
        super().__init__(meshData)
    
class Triangle2D(Mesh):
    def __init__(self, size=1.0, color=(1.0, 1.0, 1.0)) -> None:

        meshData = [None for i in range(len(MeshData))]
        
        meshData[MeshData.VERTEX.value] = Util.to_float_array([
            -0.5, -0.5, 0.0,
            0.5, -0.5, 0.0,
            0.0,  1, 0.0
        ])
        meshData[MeshData.INDEX.value] = Util.to_float_array([  
            0, 1, 2,   # first triangle
            1, 2, 0    # second triangle
        ])
        
        super().__init__(meshData)
    
    