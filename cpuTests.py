import unittest
from cpu import Registers, AGC

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.cpu = AGC()

    def tearDown(self):
        del self.cpu

    def test_setProgramCounter(self):
        newValue = 4
        self.cpu.setRegister(Registers.REG_P, newValue)
        self.assertEqual(self.cpu.getRegister(Registers.REG_P), newValue)

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')
    #
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
