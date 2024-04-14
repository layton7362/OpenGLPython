 vs = ShaderVertex("shaders/basic.vert")
    fs = ShaderFragment("shaders/basic.frag")
    mat = Material([vs,fs])
    
    # vs = ShaderVertex("shaders/basic.vert")
    fs = ShaderFragment("shaders/basic2.frag")
    mat2 = Material([vs,fs])

    verticesLeft = np.array([
        -0.9, -0.5, 0.0,  # left 
        -0.0, -0.5, 0.0,  # right
        -0.45, 0.5, 0.0  # top 
    ], dtype= np.float32)
    
    verticesRight = np.array([
        0.0, -0.5, 0.0,  # left
        0.9, -0.5, 0.0,  # right
        0.45, 0.5, 0.0   # top 
    ], dtype= np.float32)
    
    meshes.append(Mesh(verticesLeft, None, None).set_material(mat))
    meshes.append(Mesh(verticesRight, None, None).set_material(mat2))
    meshes.append(Cube(0.1).scale([4,2,2]).set_material(mat))