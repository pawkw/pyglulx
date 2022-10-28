opcodes = {
    0: lambda : 0, #nop
    16: lambda L1, L2, S1: 0, #add
    17: lambda L1, L2, S1: 0, #sub
    18: lambda L1, L2, S1: 0, #mul
    19: lambda L1, L2, S1: 0, #div
    20: lambda L1, L2, S1: 0, #mod
    21: lambda L1, S1: 0, #neg
    24: lambda L1, L2, S1: 0, #bitand
    25: lambda L1, L2, S1: 0, #bitor
    26: lambda L1, L2, S1: 0, #bitxor
    27: lambda L1, S1: 0, #bitnot
    28: lambda L1, L2, S1: 0, #shiftl
    29: lambda L1, L2, S1: 0, #sshiftr
    30: lambda L1, L2, S1: 0, #ushiftr
    32: lambda L1: 0, #jump
    34: lambda L1, L2: 0, #jz
    35: lambda L1, L2: 0, #jnz
    36: lambda L1, L2, L3: 0, #jeq
    37: lambda L1, L2, L3: 0, #jne
    38: lambda L1, L2, L3: 0, #jlt
    39: lambda : 0, #jge
    40: lambda : 0, #jgt
    41: lambda : 0, #jle
    42: lambda L1, L2, L3: 0, #jltu
    43: lambda : 0, #jgeu
    44: lambda : 0, #jgtu
    45: lambda : 0, #jleu
    48: lambda L1, L2, S1: 0, #call
    49: lambda L1: 0, #return
    50: lambda S1, L1: 0, #catch
    51: lambda L1, L2: 0, #throw
    52: lambda L1, L2: 0, #tailcall
    64: lambda L1, S1: 0, #copy
    65: lambda L1, S1: 0, #copys
    66: lambda L1, S1: 0, #copyb
    68: lambda L1, S1: 0, #sexs
    69: lambda L1, S1: 0, #sexb
    72: lambda L1, L2, S1: 0, #aload
    73: lambda L1, L2, S1: 0, #aloads
    74: lambda L1, L2, S1: 0, #aloadb
    75: lambda L1, L2, S1: 0, #aloadbit
    76: lambda L1, L2, L3: 0, #astore
    77: lambda L1, L2, L3: 0, #astores
    78: lambda L1, L2, L3: 0, #astoreb
    79: lambda L1, L2, L3: 0, #astorebit
    80: lambda S1: 0, #stkcount
    81: lambda L1, S1: 0, #stkpeek
    82: lambda : 0, #stkswap
    83: lambda L1, L2: 0, #stkroll
    84: lambda L1: 0, #stkcopy
    112: lambda L1: 0, #streamchar
    113: lambda L1: 0, #streamnum
    114: lambda L1: 0, #streamstr
    115: lambda L1: 0, #streamunichar
    256: lambda L1, L2, S1: 0, #gestalt
    257: lambda L1: 0, #debugtrap
    258: lambda S1: 0, #getmemsize
    259: lambda L1, S1: 0, #setmemsize
    260: lambda L1: 0, #jumpabs
    272: lambda L1, S1: 0, #random
    273: lambda L1: 0, #setrandom
    288: lambda : 0, #quit
    289: lambda S1: 0, #verify
    290: lambda : 0, #restart
    291: lambda L1, S1: 0, #save
    292: lambda L1, S1: 0, #restore
    293: lambda S1: 0, #saveundo
    294: lambda S1: 0, #restoreundo
    295: lambda L1, L2: 0, #protect
    296: lambda S1: 0, #hasundo
    297: lambda : 0, #discardundo
    304: lambda L1, L2, S1: 0, #glk
    320: lambda S1: 0, #getstringtbl
    321: lambda L1: 0, #setstringtbl
    328: lambda S1, S2: 0, #getiosys
    329: lambda L1, L2: 0, #setiosys
    336: lambda L1, L2, L3, L4, L5, L6, L7, S1: 0, #linearsearch
    337: lambda L1, L2, L3, L4, L5, L6, L7, S1: 0, #binarysearch
    338: lambda L1, L2, L3, L4, L5, L6, S1: 0, #linkedsearch
    352: lambda L1, S1: 0, #callf
    353: lambda : 0, #callfi
    354: lambda : 0, #callfii
    355: lambda : 0, #callfiii
    368: lambda L1, L2: 0, #mzero
    369: lambda L1, L2, L3: 0, #mcopy
    376: lambda L1, S1: 0, #malloc
    377: lambda L1: 0, #mfree
    384: lambda L1, L2: 0, #accelfunc
    385: lambda L1, L2: 0, #accelparam
    400: lambda L1, S1: 0, #numtof
    401: lambda L1, S1: 0, #ftonumz
    402: lambda L1, S1: 0, #ftonumn
    408: lambda L1, S1: 0, #ceil
    409: lambda : 0, #floor
    416: lambda L1, L2, S1: 0, #fadd
    417: lambda : 0, #fsub
    418: lambda : 0, #fmul
    419: lambda : 0, #fdiv
    420: lambda L1, L2, S1, S2: 0, #fmod
    424: lambda L1, S1: 0, #sqrt
    425: lambda : 0, #exp
    426: lambda : 0, #log
    427: lambda L1, L2, S1: 0, #pow
    432: lambda L1, S1: 0, #sin
    433: lambda : 0, #cos
    434: lambda : 0, #tan
    435: lambda : 0, #asin
    436: lambda : 0, #acos
    437: lambda : 0, #atan
    438: lambda L1, L2, S1: 0, #atan2
    448: lambda L1, L2, L3, L4: 0, #jfeq
    449: lambda L1, L2, L3, L4: 0, #jfne
    450: lambda L1, L2, L3: 0, #jflt
    451: lambda : 0, #jfle
    452: lambda : 0, #jfgt
    453: lambda : 0, #jfge
    456: lambda L1, L2: 0, #jisnan
    457: lambda L1, L2: 0, #jisinf
    512: lambda L1, S1, S2: 0, #numtod
    513: lambda L1, L2, S1: 0, #dtonumz
    514: lambda L1, L2, S1: 0, #dtonumn
    515: lambda L1, S1, S2: 0, #ftod
    516: lambda L1, L2, S1: 0, #dtof
    520: lambda L1, L2, S1, S2: 0, #dceil
    521: lambda : 0, #dfloor
    528: lambda L1, L2, L3, L4, S1, S2: 0, #dadd
    529: lambda : 0, #dsub
    530: lambda : 0, #dmul
    531: lambda : 0, #ddiv
    532: lambda L1, L2, L3, L4, S1, S2: 0, #dmodr
    533: lambda : 0, #dmodq
    536: lambda L1, L2, S1, S2: 0, #dsqrt
    537: lambda : 0, #dexp
    538: lambda : 0, #dlog
    539: lambda L1, L2, L3, L4, S1, S2: 0, #dpow
    544: lambda L1, L2, S1, S2: 0, #dsin
    545: lambda : 0, #dcos
    546: lambda : 0, #dtan
    547: lambda : 0, #dasin
    548: lambda : 0, #dacos
    549: lambda : 0, #datan
    550: lambda L1, L2, L3, L4, S1, S2: 0, #datan2
    560: lambda L1, L2, L3, L4, L5, L6, L7: 0, #jdeq
    561: lambda L1, L2, L3, L4, L5, L6, L7: 0, #jdne
    562: lambda L1, L2, L3, L4, L5: 0, #jdlt
    563: lambda : 0, #jdle
    564: lambda : 0, #jdgt
    565: lambda : 0, #jdge
    568: lambda L1, L2, L3: 0, #jdisnan
    569: lambda L1, L2, L3: 0, #jdisinf
}
