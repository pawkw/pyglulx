from modules.Mem import Mem
from modules.Stack import Stack
import sys
from modules.rawopcodes import opcodes
from modules.run import run

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
    stack = Stack(memory.header.get('stackSize'))

    run(memory, stack)
    
