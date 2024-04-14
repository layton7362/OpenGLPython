import Mesh
import Core
import Material


def scene_init(tree: Core.Base_SceneTree ):
    
    cube = Mesh.Cube().set_material(Material.DefaultMaterial())
    cube.scale([0.1,0.1,0.1])
    node = Core.Mesh3D()
    node.mesh = cube
    
    tree.add_node(node)
    
    cube = Mesh.Triangle2D().set_material(Material.DefaultMaterial())
    cube.scale([0.1,0.5,0.1]).translate([0.5,0,0])
    node = Core.Mesh3D()
    node.mesh = cube
    
    tree.add_node(node)
    
    
