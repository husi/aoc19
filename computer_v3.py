import asyncio
from copy import copy

class Memory(object):
    def __init__(self,content=[]):
        self.__memory = copy(content)

    def __getitem__(self, item):
        return 0 if item >= self.size else self.__memory[item]

    def __setitem__(self, key, value):
        if key >= self.size:
            self.__memory.extend([0]*(key-self.size+1))

        self.__memory[key] = value

    @property
    def size(self):
        return len(self.__memory)


class Computer(object):
    def __init__(self, code, name='Noname'):
        self.code = code
        self.name = name
        self.__setup_instructions()

        self.__memory = None
        self.__inputs = None
        self.__outputs = None
        self.__relative_base = None

    async def run(self, inputs, outputs):
        # print("Start running: ", self.name)
        self.__inputs = inputs
        self.__outputs = outputs
        self.__memory = Memory(self.code)
        self.__relative_base = 0
        ip = 0

        while True:
            # print(ip,self.__memory[ip])
            step = await self.__instructions[self.__get_operation(self.__memory[ip])](ip)
            if not step:
                break
            ip += step

    def execute(self,inputs):
        async def _do():
            _inputs = asyncio.Queue()
            _outputs = asyncio.Queue()
            for i in inputs:
                _inputs.put_nowait(i)

            await self.run(_inputs, _outputs)

            r = []
            while not _outputs.empty():
                r.append(_outputs.get_nowait())
            return r

        return asyncio.run(_do())


    @staticmethod
    def __get_operation(opcode):
        return opcode % 100

    def __resolve_params(self, _ip, _num):
        resolve_function = {
            0: lambda ip: self.__memory[self.__memory[ip]],
            1: lambda ip: self.__memory[ip],
            2: lambda ip: self.__memory[self.__relative_base + self.__memory[ip]]
        }

        def resolve(types, ip, num):
            if types == 0:
                return [self.__memory[self.__memory[ip + i]] for i in range(num)]

            t = types % 10

            params = resolve(types // 10, ip + 1, num - 1)
            params.insert(0, resolve_function[t](ip))
            return params

        _types = self.__memory[_ip] // 100
        return resolve(_types, _ip + 1, _num)

    def __binary_op(self, op):
        async def do(ip):
            params = self.__resolve_params(ip, 2)
            # print(params,op(params[0],params[1]))
            address = self.__resolve_address(ip, 3)
            self.__memory[address] = op(params[0], params[1])
            return 4

        return do

    async def __exit(self, ip):
        # print('Done')
        return 0

    async def __output(self, ip):
        params = self.__resolve_params(ip, 1)
        # print("{} ==> {}".format(self.name, params[0]))
        await self.__outputs.put(params[0])
        return 2

    async def __input(self, ip):
        _input = await self.__inputs.get()
        # print("{} <== {}".format( self.name, _input))
        address = self.__resolve_address(ip,1)
        self.__memory[address] = _input
        return 2

    def __resolve_address(self, ip, offset):
        ref_type = (self.__memory[ip] // (100 * pow(10, offset-1))) % 10
        base = self.__relative_base if ref_type == 2 else 0
        address = self.__memory[ip + offset] + base
        return address

    def __jump_if(self, op):
        async def do(ip):
            params = self.__resolve_params(ip, 2)
            return params[1] - ip if op(params[0]) else 3

        return do

    async def __adjust_rb(self, ip):
        params = self.__resolve_params(ip,1)
        self.__relative_base += params[0]
        return 2

    def __setup_instructions(self):
        self.__instructions = {
            1: self.__binary_op(lambda x, y: x + y),
            2: self.__binary_op(lambda x, y: x * y),
            3: self.__input,
            4: self.__output,
            5: self.__jump_if(lambda val: val != 0),
            6: self.__jump_if(lambda val: val == 0),
            7: self.__binary_op(lambda x, y: 1 if x < y else 0),
            8: self.__binary_op(lambda x, y: 1 if x == y else 0),
            9: self.__adjust_rb,
            99: self.__exit
        }


def run():
    c = Computer([3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1101, 11, 91, 225, 1002, 121, 77, 224, 101, -6314, 224, 224,
         4, 224, 1002, 223, 8, 223, 1001, 224, 3, 224, 1, 223, 224, 223, 1102, 74, 62, 225, 1102, 82, 7, 224, 1001, 224,
         -574, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 3, 224, 1, 224, 223, 223, 1101, 28, 67, 225, 1102, 42, 15, 225,
         2, 196, 96, 224, 101, -4446, 224, 224, 4, 224, 102, 8, 223, 223, 101, 6, 224, 224, 1, 223, 224, 223, 1101, 86,
         57, 225, 1, 148, 69, 224, 1001, 224, -77, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 2, 224, 1, 223, 224, 223,
         1101, 82, 83, 225, 101, 87, 14, 224, 1001, 224, -178, 224, 4, 224, 1002, 223, 8, 223, 101, 7, 224, 224, 1, 223,
         224, 223, 1101, 38, 35, 225, 102, 31, 65, 224, 1001, 224, -868, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 5,
         224, 1, 223, 224, 223, 1101, 57, 27, 224, 1001, 224, -84, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 7, 224, 1,
         223, 224, 223, 1101, 61, 78, 225, 1001, 40, 27, 224, 101, -89, 224, 224, 4, 224, 1002, 223, 8, 223, 1001, 224,
         1, 224, 1, 224, 223, 223, 4, 223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227,
         247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0, 256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1,
         99999, 1006, 0, 99999, 1006, 227, 274, 1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101,
         294, 0, 0, 105, 1, 0, 1105, 1, 99999, 1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0,
         0, 1105, 1, 99999, 1008, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 329, 101, 1, 223, 223, 8, 226, 677, 224,
         102, 2, 223, 223, 1005, 224, 344, 101, 1, 223, 223, 1107, 226, 677, 224, 102, 2, 223, 223, 1006, 224, 359, 101,
         1, 223, 223, 1007, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 374, 101, 1, 223, 223, 7, 677, 677, 224, 102, 2,
         223, 223, 1005, 224, 389, 1001, 223, 1, 223, 108, 677, 677, 224, 1002, 223, 2, 223, 1005, 224, 404, 101, 1,
         223, 223, 1008, 226, 226, 224, 102, 2, 223, 223, 1005, 224, 419, 1001, 223, 1, 223, 1107, 677, 226, 224, 102,
         2, 223, 223, 1005, 224, 434, 1001, 223, 1, 223, 1108, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 449, 1001,
         223, 1, 223, 7, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 464, 101, 1, 223, 223, 1008, 677, 677, 224, 102, 2,
         223, 223, 1005, 224, 479, 101, 1, 223, 223, 1007, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 494, 101, 1,
         223, 223, 8, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 509, 101, 1, 223, 223, 1007, 677, 677, 224, 1002,
         223, 2, 223, 1006, 224, 524, 101, 1, 223, 223, 107, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 539, 101, 1,
         223, 223, 107, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 554, 1001, 223, 1, 223, 7, 677, 226, 224, 102, 2,
         223, 223, 1006, 224, 569, 1001, 223, 1, 223, 107, 677, 677, 224, 1002, 223, 2, 223, 1005, 224, 584, 101, 1,
         223, 223, 1107, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 599, 101, 1, 223, 223, 1108, 226, 677, 224, 102, 2,
         223, 223, 1006, 224, 614, 101, 1, 223, 223, 8, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 629, 101, 1, 223,
         223, 108, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 644, 1001, 223, 1, 223, 108, 226, 226, 224, 102, 2, 223,
         223, 1005, 224, 659, 101, 1, 223, 223, 1108, 677, 226, 224, 102, 2, 223, 223, 1006, 224, 674, 1001, 223, 1,
         223, 4, 223, 99, 226])



    out = c.execute([5])
    print(out)
    assert out[0] == 15724522

if __name__ == '__main__':
    run()
