from unittest import TestCase

from helloUnitTesting import alternate_case
from helloUnitTesting import countPythonFile

class testFunctions(TestCase):

    # function name nedds to start with TestCase
    def testAlternateCase(self):
        self.assertEqual('hElLo', alternate_case('hello'))
        self.assertEqual('iTeC 2950 cApStOnE!', alternate_case('ITEC 2950 Capstone!'))
        self.assertEqual('hElP', alternate_case('help'))
        self.assertEqual('', alternate_case(''))


class testFileFilter(TestCase):

    def testPythonFile(self):
        self.assertEqual(2 , countPythonFile(['main.py', 'code.py', 'main.java', 'main.pyt']))
        self.assertEqual(0 , countPythonFile(['mine.yo','min.js','tots.food']))
        self.assertEqual(0 , countPythonFile(['hello.py.some', 'bee.pyth']))
        self.assertEqual(2 , countPythonFile(['main.PY', 'code.py', 'main.java', 'main.pyt']))
        self.assertEqual(0 , countPythonFile([]))
