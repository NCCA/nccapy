from Math.Vec3 import Vec3

from .BaseMesh import BaseMesh, Face


class ObjParseError(Exception):
    pass


class Obj(BaseMesh):
    def __init__(self):
        super().__init__()
        # as faces can use negative index values keep track of index
        self._current_vertex_offset = 0
        self._current_normal_offset = 0
        self._current_uv_offset = 0

    def _parse_vertex(self, tokens):
        try:
            self.verts.append(
                Vec3(float(tokens[1]), float(tokens[2]), float(tokens[3]))
            )
            self._current_vertex_offset += 1
        except:
            raise ObjParseError

    def _parse_normal(self, tokens):
        try:
            self.normals.append(
                Vec3(float(tokens[1]), float(tokens[2]), float(tokens[3]))
            )
            self._current_normal_offset += 1
        except:
            raise ObjParseError

    def _parse_uv(self, tokens):
        try:
            # some DCC's use vec3 for UV so may as well support
            z = 0.0
            if len(tokens) == 4:
                z = float(tokens[3])
            self.uv.append((float(tokens[1]), float(tokens[2]), z))
            self._current_uv_offset += 1
        except:
            raise ObjParseError

    def _parse_face_vertex_normal_uv(self, tokens):
        pass

    def _parse_face_vertex(self, tokens):
        pass

    def _parse_face_vertex_normal(self, tokens):
        pass

    def _parse_face_vertex_uv(self, tokens):
        pass

    def _parse_face(self, tokens):
        """face parsing is complex we have different layouts.
        don't forget we can also have negative indices main combos are :-
        f v v v v
        f v//vn v//vn v//vn v//vn
        f v/vt v/vt v/vt v/vt
        f v/vt/vn v/vt/vn v/vt/vn v/vt/vn
        """
        # first let's find what sort of face we are dealing with I assume most likely case is all
        if tokens[1].count("/") == 2 and tokens[1].find("//") == -1:
            self._parse_face_vertex_normal_uv(tokens)
        elif tokens[1].find("/") == -1:
            self._parse_face_vertex(tokens)
        elif tokens[1].find("//") != -1:
            self._parse_face_vertex_normal(tokens)
        # if we have 1 / it is a VertUV format
        elif tokens[1].count("/") == 1:
            self._parse_face_vertex_uv(tokens)

    def load(self, file):
        with open(file, "r") as obj_file:
            lines = obj_file.readlines()
        for line in lines:
            line = line.strip()  # strip whitespace
            if len(line) > 0:  # skip empty lines
                tokens = line.split()
                if tokens[0] == "v":
                    self._parse_vertex(tokens)
                elif tokens[0] == "vn":
                    self._parse_normal(tokens)
                elif tokens[0] == "vt":
                    self._parse_uv(tokens)
                elif tokens[0] == "f":
                    self._parse_face(tokens)
        return True
