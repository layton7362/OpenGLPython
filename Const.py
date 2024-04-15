from enum import Enum

class MeshData(Enum):
    VERTEX = 0
    NORMAL = 1
    COLOR = 2
    UV1 = 3
    UV2 = 4
    INDEX = 5

class ShaderData(Enum):
    VERTEX = 0
    FRAGMENT = 1
    TESSELATION = 2
    GEOMETRY = 3
    COMPUTE = 4
