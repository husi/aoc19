from __future__ import annotations
from collections import namedtuple
from typing import Iterable

Vector = namedtuple('Vector', ['x', 'y', 'z'])


def gravity(m1: int, m2: int) -> int:
    diff = m2 - m1
    return diff // abs(diff) if diff != 0 else 0


def energy(v: Vector) -> int:
    return sum([abs(i) for i in v])


class Moon:

    def __init__(self, pos):
        self.pos = pos
        self.velocity = Vector(0, 0, 0)

    def update_velocity(self, moons: Iterable[Moon]):
        for moon in moons:
            self.velocity = Vector._make([v + gravity(s, m) for v, s, m in zip(self.velocity, self.pos, moon.pos)])

    def update_pos(self):
        self.pos = Vector._make([p + v for p, v in zip(self.pos, self.velocity)])

    def __repr__(self):
        return "pos:{} velocity:{}".format(self.pos, self.velocity)


def print_moons(moons: Iterable[Moon]):
    for moon in moons:
        print(moon)


if __name__ == '__main__':
    moons = [Moon(v) for v in [Vector(-4, 3, 15), Vector(-11, -10, 13), Vector(2, 2, 18), Vector(7, -1, 0)]]

    moves = 0
    # print_moons(moons)

    while moves < 1000:
        for m in moons: m.update_velocity(moons)
        for m in moons: m.update_pos()
        # print_moons(moons)
        moves += 1
    print_moons(moons)
    print(sum([energy(m.pos) * energy(m.velocity) for m in moons]))
