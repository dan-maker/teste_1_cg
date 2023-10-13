# ============================================
# usp
# cg 2023
# nome1 num1
# nome2 num2
# trabalho 1
# ============================================

# ============================================
# bibliotecas 
import polyscope as ps
import numpy as np
# ============================================

# ============================================
# iniciar polyscope
ps.init()

# matriz de transformação para malha 1
transformacao_1 = np.matrix([
    [0.5, 0.0, 0.0, 0],
    [0.0, 0.5, 0.0, 0],
    [0.0, 0.0, 0.5, 0],
    [0.0, 0.0, 0.0, 1]])

# criar malha 1
vertices = np.array([
    [1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0]])

faces = np.array([
    [0,1,2]])

#registrar malha 1 no polyscope
mesh = ps.register_surface_mesh("objeto_1", vertices, faces)
mesh.set_transform(transformacao_1)



# View the point cloud and mesh we just registered in the 3D UI
ps.show()