import asyncio
from asyncio import Queue, FIRST_COMPLETED

from computer_v3 import Computer

code = [3, 8, 1005, 8, 330, 1106, 0, 11, 0, 0, 0, 104, 1, 104, 0, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10, 4, 10, 1008, 8,
        0, 10, 4, 10, 102, 1, 8, 29, 3, 8, 1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10, 1008, 8, 0, 10, 4, 10, 101, 0, 8,
        51, 1, 1103, 2, 10, 1006, 0, 94, 1006, 0, 11, 1, 1106, 13, 10, 3, 8, 1002, 8, -1, 10, 101, 1, 10, 10, 4, 10,
        1008, 8, 1, 10, 4, 10, 1001, 8, 0, 87, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10, 4, 10, 1008, 8, 0, 10, 4, 10, 1001,
        8, 0, 109, 2, 1105, 5, 10, 2, 103, 16, 10, 1, 1103, 12, 10, 2, 105, 2, 10, 3, 8, 102, -1, 8, 10, 1001, 10, 1,
        10, 4, 10, 108, 1, 8, 10, 4, 10, 1001, 8, 0, 146, 1006, 0, 49, 2, 1, 12, 10, 2, 1006, 6, 10, 1, 1101, 4, 10, 3,
        8, 1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10, 108, 0, 8, 10, 4, 10, 1001, 8, 0, 183, 1, 6, 9, 10, 1006, 0, 32, 3,
        8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10, 1008, 8, 1, 10, 4, 10, 101, 0, 8, 213, 2, 1101, 9, 10, 3, 8, 1002, 8,
        -1, 10, 1001, 10, 1, 10, 4, 10, 1008, 8, 1, 10, 4, 10, 101, 0, 8, 239, 1006, 0, 47, 1006, 0, 4, 2, 6, 0, 10,
        1006, 0, 58, 3, 8, 1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10, 1008, 8, 0, 10, 4, 10, 102, 1, 8, 274, 2, 1005, 14,
        10, 1006, 0, 17, 1, 104, 20, 10, 1006, 0, 28, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10, 108, 1, 8, 10, 4,
        10, 1002, 8, 1, 309, 101, 1, 9, 9, 1007, 9, 928, 10, 1005, 10, 15, 99, 109, 652, 104, 0, 104, 1, 21101, 0,
        937263411860, 1, 21102, 347, 1, 0, 1105, 1, 451, 21101, 932440724376, 0, 1, 21102, 1, 358, 0, 1105, 1, 451, 3,
        10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 0,
        3, 10, 104, 0, 104, 1, 21101, 0, 29015167015, 1, 21101, 0, 405, 0, 1106, 0, 451, 21102, 1, 3422723163, 1, 21101,
        0, 416, 0, 1106, 0, 451, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 0, 21101, 0, 868389376360, 1, 21101, 0, 439,
        0, 1105, 1, 451, 21102, 825544712960, 1, 1, 21102, 1, 450, 0, 1106, 0, 451, 99, 109, 2, 21201, -1, 0, 1, 21101,
        0, 40, 2, 21102, 482, 1, 3, 21102, 1, 472, 0, 1106, 0, 515, 109, -2, 2106, 0, 0, 0, 1, 0, 0, 1, 109, 2, 3, 10,
        204, -1, 1001, 477, 478, 493, 4, 0, 1001, 477, 1, 477, 108, 4, 477, 10, 1006, 10, 509, 1101, 0, 0, 477, 109, -2,
        2106, 0, 0, 0, 109, 4, 2101, 0, -1, 514, 1207, -3, 0, 10, 1006, 10, 532, 21102, 1, 0, -3, 22101, 0, -3, 1,
        22102, 1, -2, 2, 21102, 1, 1, 3, 21101, 551, 0, 0, 1106, 0, 556, 109, -4, 2105, 1, 0, 109, 5, 1207, -3, 1, 10,
        1006, 10, 579, 2207, -4, -2, 10, 1006, 10, 579, 22102, 1, -4, -4, 1106, 0, 647, 21201, -4, 0, 1, 21201, -3, -1,
        2, 21202, -2, 2, 3, 21102, 1, 598, 0, 1106, 0, 556, 22101, 0, 1, -4, 21101, 1, 0, -1, 2207, -4, -2, 10, 1006,
        10, 617, 21102, 0, 1, -1, 22202, -2, -1, -2, 2107, 0, -3, 10, 1006, 10, 639, 21201, -1, 0, 1, 21102, 639, 1, 0,
        105, 1, 514, 21202, -2, -1, -2, 22201, -4, -2, -4, 109, -5, 2105, 1, 0]


class Robot():
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def __init__(self):
        self.surface = {(0, 0): (1, 0)}
        self.pos = (0, 0)
        self.direction = 0

        self.top_left = [0, 0]
        self.bottom_right = [0, 0]

    def print_surface(self):
        surface = [''.join(['#' if self.surface.setdefault((x, y), (0, 0))[0] else ' ' for x in
                            range(self.top_left[0], self.bottom_right[0] +1)]) for y in
                   range(self.top_left[1], self.bottom_right[1] + 1)]
        print("\n".join(surface))

    async def robot_loop(self, cameraq, instructionq):
        def change_color(color):
            current = self.surface[self.pos]
            self.surface[self.pos] = (color, current[1] | color)

        def move(_instruction):
            self.direction = (self.direction + (1 if _instruction else -1) + 4) % 4
            self.pos = (
                self.pos[0] + self.directions[self.direction][0], self.pos[1] + self.directions[self.direction][1])

            self.top_left[0] = min(self.top_left[0], self.pos[0])
            self.top_left[1] = min(self.top_left[1], self.pos[1])
            self.bottom_right[0] = max(self.bottom_right[0], self.pos[0])
            self.bottom_right[1] = max(self.bottom_right[1], self.pos[1])

        while True:
            color = self.surface.setdefault(self.pos, (0, 0))[0]
            # print("pushing color {} from: {}".format(color, self.pos))
            await cameraq.put(color)

            new_color = await instructionq.get()
            change_color(new_color)
            instruction = await instructionq.get()
            move(instruction)

            # print("output:",color,instruction)
            # print(self.pos, self.directions[self.direction])


async def run():
    c = Computer(code)
    r = Robot()
    camera = Queue()
    instructions = Queue()

    print("starting tasks")
    await asyncio.wait([r.robot_loop(camera, instructions), c.run(camera, instructions)], return_when=FIRST_COMPLETED)
    print('computer finished')

    r.print_surface()


if __name__ == '__main__':
    asyncio.run(run())
