#version 330 core
out vec4 FragColor;

uniform float time;
void main()
{
    FragColor = vec4(1.0f * sin(time * time), 0.5f, 0.2f, 1.0f);
}