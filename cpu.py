class Registers(object):
    REG_A = "A"
    REG_P = "P"
    REG_Q = "Q"
    REG_LP = "LP"

class AGC(object):
    def __init__(self):

        #The AGC had four 16-bit registers for general computational use, called the central registers:

        # A:	The accumulator, for general computation
        # Z:	The program counter - the address of the next instruction to be executed
        # Q:	The remainder from the DV instruction, and the return address after TC instructions
        # LP:	The lower product after MP instructions

        #Central registers
        self.registers = {
            Registers.REG_A: 0x00,
            Registers.REG_P: 0x00,
            Registers.REG_Q: 0x00,
            Registers.REG_LP: 0x00
        }

        #There were also four locations in core memory, at addresses 20-23,
        #dubbed editing locations because whatever was stored there would
        #emerge shifted or rotated by one bit position, except for one that
        #shifted right seven bit positions, to extract one of the seven-bit
        #interpretive op. codes that were packed two to a word.
        #This was common to Block I and Block II AGCs.

        #The AGC had additional registers that were used internally in the course of operation:

        # S	:	12-bit memory address register, the lower portion of the memory address
        # Bank/Fbank	:	4-bit ROM bank register, to select the 1 kiloword ROM bank when addressing in the fixed-switchable mode
        # Ebank	:	3-bit RAM bank register, to select the 256-word RAM bank when addressing in the erasable-switchable mode
        # Sbank (super-bank)	:	1-bit extension to Fbank, required because the last 4 kilowords of the 36-kiloword ROM was not reachable using Fbank alone
        # SQ	:	4-bit sequence register; the current instruction
        # G	:	16-bit memory buffer register, to hold data words moving to and from memory
        # X	:	The 'x' input to the adder (the adder was used to perform all 1's complement arithmetic) or the increment to the program counter (Z register)
        # Y	:	The other ('y') input to the adder
        # U	:	Not really a register, but the output of the adder (the 1's complement sum of the contents of registers X and Y)
        # B	:	General-purpose buffer register, also used to pre-fetch the next instruction. At the start of the next instruction, the upper bits of B (containing the next op. code) were copied to SQ, and the lower bits (the address) were copied to S.
        # C	:	Not a separate register, but the 1's complement of the B register
        # IN	:	Four 16-bit input registers
        # OUT	:	Five 16-bit output registers

        self.otherRegisters = {

        }

    def setRegister(self, register, value):
        self.registers[register] = value

    def getRegister(self, register):
        return self.registers[register]


#Timing

#Memory

#Instruction Set

#Interrupts
