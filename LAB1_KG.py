import numpy as np
from PIL import Image
from math import *

v = []
f = []
#чтение файла
file = open('model.obj')
for s in file:
    s1 = s.split()
    if s1[0] == 'v':
        v.append(s1[1:4])
    if s1[0] == 'f':
        f.append([int(x.split('/')[0]) for x in s1[1:4]])
v = [list(map(float, k)) for k in v]

img_mat = np.zeros((1000, 1000, 3), dtype=np.uint8)
def line(x0, y0, x1, y1, img_mat):
    dmax = max(abs(floor(x0) - floor(x1)), abs(floor(y0) - floor(y1)))  # наиб расстояние
    L = dmax + 1  # количество точек
    if L == 1:
        img_mat[floor(y0), floor(x0)] = 255
        return

    dx = (x1 - x0) / (L - 1)
    dy = (y1 - y0) / (L - 1)

    for _ in range(L):
        img_mat[floor(y0), floor(x0)] = [145, 0, 255]
        x0 += dx
        y0 += dy

for i in range(len(v)):
    img_mat[floor(-v[i][1]*6300), floor(v[i][0]*6300-470)] = [155, 0, 255]
for i in range(len(f)):
    x0 = v[f[i][0] - 1][0]*6300-470
    y0 = -v[f[i][0] - 1][1]*6300
    x1 = v[f[i][1] - 1][0]*6300-470
    y1 = -v[f[i][1] - 1][1]*6300
    x2 = v[f[i][2] - 1][0] * 6300 - 470
    y2 = -v[f[i][2] - 1][1] * 6300
    line(x0, y0, x1, y1, img_mat)
    line(x0, y0, x2, y2, img_mat)
    line(x1, y1, x2, y2, img_mat)

img = Image.fromarray (img_mat)
img.save('img.png')
