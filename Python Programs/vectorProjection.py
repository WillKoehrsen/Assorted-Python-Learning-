import numpy as np 
import math

def decompose(v, b):
	v = np.array(v)
	b = np.array(b)
	mag_v = np.linalg.norm(v)
	mag_b = np.linalg.norm(b)
	u_v = v / mag_v
	u_b = b / mag_b
	theta = math.acos(np.dot(v,b)/(mag_v * mag_b))
	mag_v_para = mag_v * math.cos(theta)
	mag_v_perp = mag_v * math.sin(theta)
	v_para = mag_v_para * u_b
	v_perp = v - v_para
	return v_para, v_perp

v_projection, v_perpendicular = (decompose([3.009, -6.172, 3.692, -2.51], [6.404, -9.144, 2.759, 8.718]))
print(v_perpendicular)
print(v_projection)
print(v_perpendicular + v_projection)