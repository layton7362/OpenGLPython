from copy import copy
import numpy as np
import sys
from OpenGL.GL import *
import glm

from Core import Base_Mesh, Base_Material

class Mesh(Base_Mesh):
    pass

class Cube(Mesh):
    def __init__(self, size=1.0, color=(1.0, 1.0, 1.0)) -> None:
        vertices = [
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
        ]

        super().__init__(vertices, None, None, None)
    
    

class Triangle2D(Mesh):
    def __init__(self, size=1.0, color=(1.0, 1.0, 1.0)) -> None:

        vertices = [
            -0.5, -0.5, 0.0,
            0.5, -0.5, 0.0,
            0.0,  1, 0.0
        ]

        super().__init__(vertices, None, None, None)
    
    