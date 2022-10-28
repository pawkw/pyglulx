from typing import List

class Opcode:
    def __init__(self, code: str, name: str, IOs = []) -> None:
        self.name = name
        self.code = code
        self.IOs = IOs

    def __repr__(self) -> str:
        return f"{self.name} {self.code} {self.IOs}"

    def set_ios(self, ios: List[str]) -> None:
        self.IOs = ios