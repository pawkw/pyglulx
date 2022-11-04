from modules.Mem import Mem
from modules.Stack import Stack
from modules.GlulxObject import GlulxObject

def run(memory: Mem, stack: Stack) -> int:
    # Get the initial object.
    glulx_object = memory.get_function()
    print(f"run got glulx_object: {glulx_object}")

    # Set up call frame
    