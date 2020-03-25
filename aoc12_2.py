from __future__ import annotations
from collections import namedtuple
from functools import reduce
from math import gcd
from operator import mul
from typing import Iterable

Vector = namedtuple('Vector', ['x', 'y', 'z'])


def gravity(m1: int, m2: int) -> int:
    diff = m2 - m1
    return diff // abs(diff) if diff != 0 else 0


def energy(v: Vector) -> int:
    return sum([abs(i) for i in v])


class Moon:
    zero = Vector(0, 0, 0)

    def __init__(self, pos):
        self.pos = pos
        self.orig_pos = pos
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


def get_plane(moons: Iterable[Moon], plane: int):
    return tuple([z for z in zip(*[(moon.pos[plane], moon.velocity[plane]) for moon in moons])])


def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)


if __name__ == '__main__':
    moons = [Moon(v) for v in [Vector(-4, 3, 15), Vector(-11, -10, 13), Vector(2, 2, 18), Vector(7, -1, 0)]]

    orig_planes = [get_plane(moons, i) for i in range(3)]
    identities = [None, None, None]

    moves = 0
    # print_moons(moons)

    identities_found = 0
    while True:
        for m in moons:
            m.update_velocity(moons)
        for m in moons:
            m.update_pos()
        moves += 1

        for i in range(3):
            if identities[i] is None and orig_planes[i] == get_plane(moons, i):
                identities[i] = moves
                identities_found += 1
                print('Identity found on plane: {} at step {}'.format(i, moves))
                print_moons(moons)

        if identities_found == 3:
            break

    print(identities)
    print (reduce(lcm,identities,1))