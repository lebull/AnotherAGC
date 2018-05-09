from screen import Screen



class MemorySpace(object):
    def __init__(self, totalBits, wordSize):
        self.data = [0 for i in range(totalBits)]
        self.totalBits = totalBits
        self.wordSize = wordSize

    def __len__(self):
        return len(self.data)/self.wordSize

    def read(self, address):
        return self.data[address]

    def write(self, address, data):
        self.data[address] = bin(data)

    def getMaxAddress(self):
        return self.totalBits/sel.wordSize

#
# class VisualMemory(MemorySpace):
#     def __init__(self, wordsPerRow, *args, **kwargs):
#         super(self, VisualMemory).__init__(*args, **kwargs)
#         rowWidth = self.wordSize * wordsPerRow
#         numRows = float(self.totalBits)/rowWidth
#         self.screen = Screen((rowWidth, numRows))
#
#     def draw(self):

if __name__ == "__main__":
    import unittest

    class TestMemorySpace(unittest.TestCase):
        def testCreate(self):
            space = MemorySpace(0xFFFF, 0x10)
            self.assertEqual(len(space), 0xFFF)

        def testReadWrite(self):
            space = MemorySpace(0xFFFF, 0x10)
            data = 0x1A2B
            address = 0xFF
            space.write(address, data)
            readData = space.read(address)
            self.assertEqual(data, readData)

        #TODO:
        # Test writing a value that is too large
        # Test writing to an address that is out of range
        

    unittest.main()
