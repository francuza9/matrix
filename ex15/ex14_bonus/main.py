from projection import projection
from Matrix import Matrix
from math import radians

fov = radians(90.0)   # 90 degrees FOV
ratio = 16/9          # widescreen aspect ratio
near = 0.1
far = 100.0

P = projection(fov, ratio, near, far)

# Write to "proj" file in row-major printing order
with open("proj", "w") as f:
	for row in range(4):
		line = ", ".join(str(P.data[col][row]) for col in range(4))
		f.write(line + "\n")

print("Projection matrix written to proj")