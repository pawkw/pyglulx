
class Header:
    def __init__(self, header_bytes: bytes) -> None:
        self.data = {}
        self.data["magicNumber"] = int.from_bytes(header_bytes[0:4], 'big')
        self.data["majorVersion"] = int.from_bytes(header_bytes[4:6], 'big')
        self.data["minorVersion"] = int.from_bytes(header_bytes[6:7], 'big')
        self.data["miminorMinorVersion"] = int.from_bytes(header_bytes[7:8], 'big')
        self.data["RAMSTART"] = int.from_bytes(header_bytes[8:12], 'big')
        self.data["EXTSTART"] = int.from_bytes(header_bytes[12:16], 'big')
        self.data["ENDMEM"] = int.from_bytes(header_bytes[16:20], 'big')
        self.data["stackSize"] = int.from_bytes(header_bytes[20:24], 'big')
        self.data["startFunc"] = int.from_bytes(header_bytes[24:28], 'big')
        self.data["decodingTbl"] = int.from_bytes(header_bytes[28:32], 'big')
        self.data["checksum"] = int.from_bytes(header_bytes[32:36], 'big')

    def __repr__(self) -> str:
        result = ""
        for key, value in self.data.items():
            result += f"{key}: {value}\n"
        return result
        
    def get(self, key: str) -> int:
        return self.data[key]

