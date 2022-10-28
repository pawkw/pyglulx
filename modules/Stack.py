from decimal import Underflow


class Stack:
    def __init__(self, size: int) -> None:
        self.data = bytes(size)
        self.pointer = 0
        self.max = size

    def push(self, data: bytes) -> None:
        numBytes = len(data)
        if self.pointer + numBytes > self.max:
            raise OverflowError("Stack overflow.")

        self.data[self.pointer] = data
        self.pointer += numBytes

    def pop(self, numBytes: int) -> bytes:
        if self.pointer - numBytes < 0:
            raise Underflow("Stack underflow.")

        self.pointer -= numBytes
        return self.data[self.pointer:self.pointer+numBytes]

    def get_pointer(self) -> int:
        return self.pointer