class Face:
    slots = ("vert", "uv", "normal")

    def __init__(self):
        self.vert = []
        self.uv = []
        self.normal = []


class BaseMesh:
    def __init__(self):
        self.verts = []
        self.normals = []
        self.uv = []
        self.faces = []
