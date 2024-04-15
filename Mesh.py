from OpenGL.GL import *
import Util

from Core import Base_Mesh, Base_Material, MeshData

class Mesh(Base_Mesh):
    pass

class Cube(Mesh):
    def __init__(self, size=1.0, color=(1.0, 1.0, 1.0)) -> None:
        
        meshData = [None for i in range(len(MeshData))]
        
        meshData[MeshData.VERTEX.value] = Util.to_float_array([
        # Vorderseite
        -size, -size, size,
        size, -size, size,
        size, size, size,
        -size, size, size,
        # Rückseite
        -size, -size, -size,
        -size, size, -size,
        size, size, -size,
        size, -size, -size,
        # Links
        -size, -size, -size,
        -size, -size, size,
        -size, size, size,
        -size, size, -size,
        # Rechts
        size, -size, -size,
        size, size, -size,
        size, size, size,
        size, -size, size,
        # Oben
        -size, size, -size,
        -size, size, size,
        size, size, size,
        size, size, -size,
        # Unten
        -size, -size, -size,
        size, -size, -size,
        size, -size, size,
        -size, -size, size,
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
        
        super().__init__(meshData)
    
    