import glfw
from OpenGL.GL import glViewport

SCR_WIDTH = 800
SCR_HEIGHT = 600

GameWindow = None

fragment_shader_source: str = None
with open("shaders/basic.frag", 'r') as data:
    fragment_shader_source = data.read()
    
def process_input(window):
    if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
        glfw.set_window_should_close(window, True)

def framebuffer_size_callback(window, width, height):
    glViewport(0, 0, width, height)

def init():
    global GameWindow
    
    if not glfw.init():
        return -1

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    GameWindow = glfw.create_window(SCR_WIDTH, SCR_HEIGHT, "GAME", None, None)
    
    if not GameWindow:
        glfw.terminate()
        return -1
    
    glfw.make_context_current(GameWindow)
    glfw.set_framebuffer_size_callback(GameWindow, framebuffer_size_callback)
    
def dispose():
    glfw.terminate()