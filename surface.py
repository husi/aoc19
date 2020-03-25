import os


class Surface:
    def __init__(self, default, mapping):
        self.default = default
        self.mapping = mapping
        self.surface = {}

        self.top_left = None
        self.bottom_right = None

    def set(self, x, y, value):
        if self.top_left == None:  # first insert
            self.top_left = [x, y]
            self.bottom_right = [x, y]
        else:
            self.top_left[0] = min(self.top_left[0], x)
            self.top_left[1] = min(self.top_left[1], y)
            self.bottom_right[0] = max(self.bottom_right[0], x)
            self.bottom_right[1] = max(self.bottom_right[1], y)

        self.surface[(x, y)] = value

    def print_surface(self,  mx=0, my=0, mark=None):
        surface = [''.join([mark if mx==x and y==my and mark else self.mapping[self.surface.setdefault((x, y), self.default)] for x in
                            range(self.top_left[0], self.bottom_right[0] + 1)]) for y in
                   range(self.top_left[1], self.bottom_right[1] + 1)]
        # os.system('cls')
        print("\n".join(surface),'\n')
