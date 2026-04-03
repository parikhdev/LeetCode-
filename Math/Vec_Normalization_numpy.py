import numpy as np

def Normalized_vec(v):
    vector_array = np.array(v)
    # linalg -> linear_algebra and norm is the built in function for normalization
    magnitude = np.linalg.norm(vector_array)

    if magnitude == 0:
        return v
    # Norm_vec = np.round(vector_array/magnitude, 2)
    Norm_vec = vector_array/magnitude
    return Norm_vec
print(Normalized_vec([3,4]))
print(Normalized_vec([312,480]))
print(Normalized_vec([3000,40000]))