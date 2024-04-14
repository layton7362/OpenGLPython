import glfw
import Window

class Input():
    @staticmethod
    def is_pressed(key):
        return Window.GameWindow and glfw.get_key(Window.GameWindow, key) == glfw.PRESS

    @staticmethod
    def update_inputs():
        
        pass