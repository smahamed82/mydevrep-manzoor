import unittest
from RemoveObject import RemoveObject
import os
from unittest import mock
from mock import Mock
import sys


class TestRemoveObject(unittest.TestCase):

    def setUp(self, fname='testfile'):
        self.fname = fname
        self.Mobj  = Mock()
        print ('Creating file ')
        with open(self.fname, 'w') as f:
            f.write('Delete Me')

    def test_RemoveObject(self):
        print ('My name is {}'.format(self.Mobj))
        RemoveObject(self.fname, self.Mobj)
        self.Mobj.remove.assert_called_with(self.fname)


## in jupyter notebook
#suite = unittest.TestLoader().loadTestsFromTestCase(TestRemoveObject)
#unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()
