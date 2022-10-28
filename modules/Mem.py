from modules.Header import Header
from modules.Stack import Stack
from modules.opcode_defs import opcode_defs

class Mem:
    opcode_diffs = [0, 0, 0x8000, 0xC0000000]

    def __init__(self, ROM) -> None:
        self.data = ROM
        self.header = Header(self.data[0:36])
        self.pc = self.header.get("startFunc")
        self.stack = Stack(self.header.get("stackSize"))
        if self.header.get("magicNumber") != 1198290284:
            raise ValueError("This is the wrong type of file.")

    def read(self, number: int) -> bytes:
        result = self.data[self.pc:self.pc+number]
        self.pc += number
        return result

    def read_int(self, number: int) -> int:
        return int.from_bytes(self.read(number), 'big')

    def peek(self, number: int) -> bytes:
        return self.data[self.pc:self.pc+number]

    def get_func(self):
        type = self.read_int(1)
        
        if type not in [0xc0, 0xc1]:
            msg = f"Expected a function but got {hex(type)}."
            raise Exception(msg)

        print(f"Function type: {hex(type)}")
        while True:
            data = self.read(2)
            print(f"Data: {data}")
            if int.from_bytes(data, 'big') == 0:
                break
        return
 
    def get_opcode(self) -> int:
        data = self.data[self.pc]
        type = (data & 192) >> 6

        numBytes = 1 if type < 2 else 2**(type-1)
        print(f"Type: {type} Number of bytes: {numBytes} Bytes: {data}")
        opcode = int.from_bytes(self.data[self.pc:self.pc+numBytes], 'big') - self.opcode_diffs[type]
        self.pc += numBytes
        print(opcode_defs[opcode])
        return opcode
        