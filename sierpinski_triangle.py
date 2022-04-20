import matplotlib.pyplot as plt
import random

vertex_1 = (0, 0)
vertex_2 = (100, 0)
vertex_3 = (50, 100)

initial_tri_coords = [vertex_1, vertex_2, vertex_3]

def get_random_vertex():
    rand_index = random.randint(0, 2)
    return initial_tri_coords[rand_index]

def get_midpoint(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return [(x1 + x2) / 2, (y1 + y2) / 2]

def get_area(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)
    
def inside(test_p, p1 = vertex_1, p2 = vertex_2, p3 = vertex_3):
    a = get_area(p1, p2, p3)
    a1 = get_area(p1, p2, test_p)
    a2 = get_area(p1, test_p, p3)
    a3 = get_area(test_p, p2, p3)
    return True if a == (a1 + a2 + a3) else False

def get_random_point():
    return random.uniform(0, 100), random.uniform(0, 100)

def get_start_point():
    current_point = get_random_point()
    while not inside(current_point):
        current_point = get_random_point()
    return current_point


#plot_triangle(ax, n = 1000) #75 sec for n = 10000
boundary = True
fig, ax = plt.subplots()
n = 100
if boundary:
    initial_tri_coords = [vertex_1, vertex_2, vertex_3, vertex_1]
    x, y = zip(*initial_tri_coords)
    plt.plot(x, y, linewidth = 1)

x_values = []
y_values = []
current_point = get_start_point()
x_values.append(current_point[0])
y_values.append(current_point[1])

for trial in range(n):
    rand_vertex = get_random_vertex()
    midpoint = get_midpoint(current_point, rand_vertex)
    x_values.append(midpoint[0])
    y_values.append(midpoint[1])
    plt.scatter(x_values, y_values, s = 2)
    plt.pause(0.01)
    current_point = midpoint 

plt.show()