import glm
from typing import List, Set, TypeVar
def to_float_array(list: List[glm.float32]):
    return (glm.float32 * len(list))(*list) 

def to_int_array(list):
    return (glm.int32 * len(list))(*list) 

def to_vec3_array(list):
    return (glm.fvec3 * len(list))(*list) 

def to_vec2_array(list):
    return (glm.fvec2 * len(list))(*list) 
