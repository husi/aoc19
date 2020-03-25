import math
import sys
from heapq import heappush, heappop
from math import gcd

sm1 = """.#..#
.....
#####
....#
...##"""

sm2 = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""

sm3 = """.#......#...#.....#..#......#..##..#
..#.......#..........#..##.##.......
##......#.#..#..#..##...#.##.###....
..#........#...........#.......##...
.##.....#.......#........#..#.#.....
.#...#...#.....#.##.......#...#....#
#...#..##....#....#......#..........
....#......#.#.....#..#...#......#..
......###.......#..........#.##.#...
#......#..#.....#..#......#..#..####
.##...##......##..#####.......##....
.....#...#.........#........#....#..
....##.....#...#........#.##..#....#
....#........#.###.#........#...#..#
....#..#.#.##....#.........#.....#.#
##....###....##..#..#........#......
.....#.#.........#.......#....#....#
.###.....#....#.#......#...##.##....
...##...##....##.........#...#......
.....#....##....#..#.#.#...##.#...#.
#...#.#.#.#..##.#...#..#..#..#......
......#...#...#.#.....#.#.....#.####
..........#..................#.#.##.
....#....#....#...#..#....#.....#...
.#####..####........#...............
#....#.#..#..#....##......#...#.....
...####....#..#......#.#...##.....#.
..##....#.###.##.#.##.#.....#......#
....#.####...#......###.....##......
.#.....#....#......#..#..#.#..#.....
..#.......#...#........#.##...#.....
#.....####.#..........#.#.......#...
..##..#..#.....#.#.........#..#.#.##
.........#..........##.#.##.......##
#..#.....#....#....#.#.......####..#
..............#.#...........##.#.#.."""

sm = sm3


def read_map(_map):
    return [(char[0], line[0]) for line in enumerate(_map.split('\n')) for char in enumerate(line[1]) if char[1] == '#']


def vector(p1, p2):
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]
    _gcd = gcd(x, y)

    return (x // _gcd, y // _gcd), abs(x) + abs(y)

def get_angle(vector):
    return 180 - math.atan2(*vector) * 180 / math.pi

def get_vectors(station, stations):
    vectors = {}
    for s in stations:
        if s == station:
            continue
        v, d = vector(station, s)
        heappush(vectors.setdefault(v, []), (d, s))
    return vectors


if __name__ == '__main__':
    stations = read_map(sm)
    best_place = (None, {})
    for station in stations:
        vectors = get_vectors(station, stations)
        if len(best_place[1]) < len(vectors):
            best_place = (station, vectors)

    # sort by angle
    ordered = sorted(best_place[1].items(),key=lambda i: get_angle(i[0]))


    num = 1
    while True: # go round and pick only one from each angle till we find the one we need
        for i in ordered:
            if len(i[1]):
                station = heappop(i[1])
                if num == 200:
                    print(station)
                    sys.exit(1)
                num += 1

