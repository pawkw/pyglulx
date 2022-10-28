from modules.Mem import Mem
import sys
from modules.rawopcodes import opcodes

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print(f"Use: {sys.argv[0]} <name of ulx gamefile>.")
        exit(0)

    file_path = sys.argv[1]
    
    with open(file_path, "rb") as f:
        ROM = f.read()

    if not ROM:
        raise FileNotFoundError()
        
    memory = Mem(ROM)

    memory.get_object()
    opcode = memory.get_opcode()
    print(opcode)
