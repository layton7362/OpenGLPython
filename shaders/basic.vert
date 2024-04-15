#version 330 core
layout (location = 0) in vec3 aPos;

uniform float time = 0;
uniform mat4 matrix;

void main()
{   
    vec4 res =  vec4(aPos, 1) * matrix ;
    gl_Position = res;
}