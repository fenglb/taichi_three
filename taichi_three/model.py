import numpy as np

def _crossProduct(a, b):
    x, y, z = a
    u, v, w = b
    return y * w - z * v, z * u - w * x, x * v - y * u

def _dotProduct(a, b):
    x, y, z = a
    u, v, w = b
    return x * u + y * v + z * w

def _vectorAdd(a, b):
    x, y, z = a
    u, v, w = b
    return x + u, y + v, z + w

def _vectorSub(a, b):
    x, y, z = a
    u, v, w = b
    return x - u, y - v, z - w

def _vectorMul(a, k):
    x, y, z = a
    return x * k, y * k, z * k


def readobj(path):
    vertices = []
    vertexNormals = []
    faces = []
    with open(path, 'r') as myfile:
        data = myfile.readlines()
        # cache vertices

        for line in data:
            if line.startswith('v '):
                splitted = line.split()
                vertex = [float(splitted[1]),
                          float(splitted[2]),
                          float(splitted[3])
                          ]
                vertices.append(vertex)
            if line.startswith('vn '):
                splitted = line.split()
                normal = [float(splitted[1]),
                          float(splitted[2]),
                          float(splitted[3])
                          ]
                vertexNormals.append(normal)

        # cache faces
        # DONT merge this 'for loop'
        # must initialize vertices for faces to work
        for line in data:
            # line looks like 'f 5/1/1 1/2/1 4/3/1'
            # or 'f 314/380/494 382/400/494 388/550/494 506/551/494' for quads
            if line.startswith('f '):
                splitted = line.split()
                faceVertices = []
                faceIndices = []

                for i in range(1, len(splitted)):
                    # splitted[i] should look like '5/1/1'
                    # for vertex/vertex UV coords/vertex Normal  (indexes number in the list)
                    # the index in 'f 5/1/1 1/2/1 4/3/1' STARTS AT 1 !!!
                    index = int((splitted[i].split('/'))[0]) - 1
                    faceIndices.append(index)
                    faceVertices.append(vertices[index])

                if len(faceVertices) == 4:
                    faces.append([
                        faceVertices[0], faceVertices[1], faceVertices[2]])
                    faces.append([
                        faceVertices[2], faceVertices[3], faceVertices[0]])
                else:
                    faces.append(faceVertices)

        return np.array(faces)
