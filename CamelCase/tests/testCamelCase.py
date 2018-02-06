import unittest
from camelCase import camelCase

class TestCamelCase(unittest.TestCase):

    def testCamelCasePro(self):

        self.assertEqual('asdfAAsdfAsDfAdsf', camelCase.camelCaseMethod('asdf a asdf as df adsf '))
        self.assertEqual('helloAll', camelCase.camelCaseMethod('hello all'))
        self.assertEqual('helloMeThere', camelCase.camelCaseMethod(' hElLo me there'))
        self.assertEqual('joinMeAtTheOlympics', camelCase.camelCaseMethod('Join me at the olympics'))
