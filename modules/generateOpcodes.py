
from typing import TextIO, List, Dict
from Opcode import Opcode

def get_heading(f: TextIO) -> str:
    while True:
        line = f.readline()
        if not line:
            return None

        if line.startswith("#"):
            return line[1:].strip()

def get_codeblock(f: TextIO) -> List[str]:
    result = []
    inBlock = False
    while True:
        line = f.readline()
        if not line:
            return None

        line = line.strip()
        
        if inBlock:
            if line == "```":
                break

            result.append(line)
            continue

        if line == "```":
            inBlock = True
    return result

def parse_codeblock(codeblock: List[str], opcodes: Dict[str, Opcode]) -> None:
    for line in codeblock:
        parts = line.split(' ')
        name = parts[0]
        if len(parts) < 2:
            return
        opcodes[name].IOs = parts[1:]
        return

if __name__ == "__main__":
    with open('modules/opcodes.txt', 'r') as f:
        heading = get_heading(f)
        print(f"'{heading}'")

        if heading != "Codes":
            raise ValueError("Could not find 'Codes' heading.")

        opcodes = {}
        
        while True:
            line = f.readline().strip()

            if line == "":
                break

            pair = line.split(':')
            opcode = Opcode(pair[0], pair[1].strip())
            opcodes[opcode.name] = opcode
        
        heading = get_heading(f)
        print(f"'{heading}'")

        if heading != "Defs":
            raise ValueError("Could not find 'Defs' heading.")

        while True:
            codeblock = get_codeblock(f)

            if not codeblock:
                break

            print(codeblock)

            parse_codeblock(codeblock, opcodes)
    with open("modules/rawopcodes.py", 'w') as f:
        f.write("opcodes = {\n")
        for key in opcodes.keys():
            opcode = opcodes[key]
            args = ', '.join(opcode.IOs)
            f.write(f"    {opcode.code}: lambda {args}: 0, #{opcode.name}\n")
        f.write("}\n")

    with open("modules/opcode_defs.py", 'w') as f:
        f.write(
"""
from typing import List, Dict
from modules.Opcode import Opcode

opcode_defs = {
"""
        )
        for key in opcodes.keys():
            opcode = opcodes[key]
            f.write(f"    {opcode.code}: Opcode({opcode.code}, '{opcode.name}', {opcode.IOs}),\n")
        f.write("}\n")

        

        