import cProfile
import time
from math import gcd

s0 = '12345678'
s1 = '80871224585914546619083218645595'
s2 = '03036732577212944063491565474664'
sr = '59734319985939030811765904366903137260910165905695158121249344919210773577393954674010919824826738360814888134986551286413123711859735220485817087501645023012862056770562086941211936950697030938202612254550462022980226861233574193029160694064215374466136221530381567459741646888344484734266467332251047728070024125520587386498883584434047046536404479146202115798487093358109344892308178339525320609279967726482426508894019310795012241745215724094733535028040247643657351828004785071021308564438115967543080568369816648970492598237916926533604385924158979160977915469240727071971448914826471542444436509363281495503481363933620112863817909354757361550'

s = s0

multiplier = 10000


def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)


def compute_digit(i, signal):
    def compute_one(_i, _signal):
        t1 = time.time()
        sign = [1, 0, -1, 0]
        pos = _i - 1
        length = len(_signal)
        sign_index = 0
        d = 0
        steps = 0
        while pos < length:
            steps += 1
            if sign[sign_index:]:
                d += sign[sign_index] * sum(_signal[pos:pos + _i])
            pos = pos + _i
            sign_index = (sign_index + 1) % 4

        print('Compute {} in {} steps {}'.format(_i, steps, time.time() - t1))
        return d

    t0 = time.time()

    pattern_length = i * 4
    signal_length = len(signal)

    compute_multiplier = min(lcm(pattern_length, signal_length) // signal_length, multiplier)
    computable = signal * compute_multiplier

    computable_length = len(computable)

    full_length = signal_length * multiplier
    m = full_length // computable_length
    r = full_length % computable_length

    remainder = (signal * (r // len(signal) + 1))[:r]

    result = compute_one(i, computable) * m + compute_one(i, remainder)

    print('{} length = {} + {}  {}'.format(i, computable_length, r, time.time() - t0))
    return abs(result) % 10


def compute(signal):
    return [compute_digit(i, signal) for i in range(1, len(signal) * multiplier + 1)]


if __name__ == '__main__':
    signal = [int(c) for c in s]
    # cProfile.run('compute(signal)')
    for i in range(100):
        signal = compute(signal)
        print(i, signal[0:8])
