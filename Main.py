
# import Core
import Window
from Window import GameWindow
import Input
import SceneTree
import time

## PROGRAM START

tree: SceneTree.SceneTree = None

def init():
    global tree
    
    Window.init()
    
    tree = SceneTree.SceneTree()

# TODO REMOVE
    import Scene_Test
    Scene_Test.scene_init(tree)    
    
def main_loop():
    global tree

    # Setze die gewünschte Framerate
    FRAME_RATE = 60.0  # Ändere hier die Framerate nach Bedarf
    FRAME_TIME = 1.0 / FRAME_RATE

    # Startzeit initialisieren
    time_start = time.time()
    time_current = time_start

    # Zähler für Schleifendurchläufe pro Sekunde
    loop_count = 0
    last_second = time.time()

    while not Window.glfw.window_should_close(Window.GameWindow):
        # Zeit für diesen Schleifendurchlauf abrufen
        loop_time = time.time() - time_current
        
        if loop_time >= FRAME_TIME:
            # Delta-Zeit berechnen
            delta = loop_time
            
            # Aktualisiere die aktuelle Zeit
            time_current = time.time()
            
            # Eingabe verarbeiten
            Input.Input.update_inputs()
            Window.process_input(Window.GameWindow)
            
            # Logik aktualisieren
            tree.main_update()
            tree.main_deferred()
            
            # Rendern
            tree.render()
            
            # Puffer tauschen und Ereignisse verarbeiten
            Window.glfw.swap_buffers(Window.GameWindow)
            Window.glfw.poll_events()

            # # Zähler für Schleifendurchläufe pro Sekunde aktualisieren
            loop_count += 1
            current_time = time.time()
            if current_time - last_second >= 1.0:
                # print("Schleifendurchläufe pro Sekunde:", loop_count)
                loop_count = 0
                last_second = current_time

            # # Wartezeit einhalten, falls der Schleifendurchlauf zu schnell war
            # excess_time = time.time() - time_current
            # if excess_time < FRAME_TIME:
            #     time.sleep(FRAME_TIME - excess_time)

    

if __name__ == "__main__":
    init()
    main_loop()