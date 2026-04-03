# Vector Normalization
# Vector -> Magnitude + Direction
# Normalization: Mathematically, dividing a vector by its magnitude is exactly what normalization is! 
import math
def normalize_vector(v):
    magnitude = math.sqrt(sum(x**2 for x in v))

    if magnitude == 0:
        return v
    
    normalized_vec = [round(x/magnitude, 2) for x in v]
    return normalized_vec

print(normalize_vector([3,4])) # 2d vector 
print(normalize_vector([312,480]))
print(normalize_vector([3000,40000])) 

