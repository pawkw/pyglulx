from pip import main
from modules.Header import Header
import sys

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print(f"Use: {sys.argv[0]} <name of ulx gamefile>.")
        exit(0)

    file_path = sys.argv[1]
    
    with open(file_path, "rb") as f:
        ROM = f.read()

    if not ROM:
        raise FileNotFoundError()
        
    header = Header(ROM[0:36])

    if header.get("magicNumber") != 1198290284:
        raise ValueError("This is the wrong type of file.")
    
    print(header)