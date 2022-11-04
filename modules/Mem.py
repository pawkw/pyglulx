from ast import arg
from modules.Header import Header
from modules.GlulxObject import GlulxObject
from modules.opcode_defs import opcode_defs

class Mem:
    opcode_diffs = [0, 0, 0x8000, 0xC0000000]

    def __init__(self, ROM) -> None:
        self.data = ROM
        self.header = Header(self.data[0:36])
        self.pc = self.header.get("startFunc")
        # self.stack = Stack(self.header.get("stackSize"))
        if self.header.get("magicNumber") != 1198290284:
            raise ValueError("This is the wrong type of file.")
        print(f'Memory loaded {len(self.data)} bytes.')

    def read(self, numBytes: int) -> bytes:
        result = self.data[self.pc:self.pc+numBytes]
        self.pc += numBytes
        return result

    def read_int(self, numBytes: int) -> int:
        return int.from_bytes(self.read(numBytes), 'big')

    def peek(self, numBytes: int) -> bytes:
        return self.data[self.pc:self.pc+numBytes]

    def peek_int(self, numBytes: int) -> int:
        return int.from_bytes(self.peek(numBytes), 'big')

    def get_function(self):
        result = GlulxObject(0, [])
        result.type = self.read_int(1)
        
        if result.type not in [0xc0, 0xc1]:
            msg = f"Expected a function but got {hex(result.type)}."
            raise Exception(msg)

        print(f"Function type: {hex(result.type)}")
        data_list = []
        while True:
            data = self.read(2)
            print(f"Local args data: {data}")
            if int.from_bytes(data, 'big') == 0:
                break
            data_list.append([int.from_bytes(data(0)), int.from_bytes(data(1))])
        result.locals_list = data_list
        return result
 
    def get_arg(self, type) -> int:
        print(f'get_arg type = {type}.')
        numBytes = type % 4
        if numBytes == 0:
            return 0
        numBytes = 2**(numBytes-1)
        print(f'  arg number of bytes = {numBytes}.')
        print(f'  bytes = {self.peek(numBytes)}.')
        return self.read_int(numBytes)

    def get_opcode(self) -> int:
        data = self.data[self.pc]
        type = (data & 192) >> 6

        numBytes = 1 if type < 2 else 2**(type-1)
        print(f"Opcode type: {type} Number of bytes: {numBytes} Opcode: {data}")
        code = self.read_int(numBytes) - self.opcode_diffs[type]
        opcode = opcode_defs[code]
        print(opcode)

        numArgs = len(opcode.IOs)
        data = ""
        if numArgs > 0:
            data = self.read((numArgs+1)//2)
        print(f"Args data: {data}")

        for x in data:
            opcode.args.append(self.get_arg(0x0f & x))
            opcode.args.append(self.get_arg((0xf0 & x) >> 4))
        opcode.args = opcode.args[0:numArgs]
        print(f"args = {opcode.args}")
        return opcode
        