import unittest
from RemoveObject1 import RemoveObj
import os
from unittest import mock
from mock import Mock
import sys


class TestRemoveObject(unittest.TestCase):

    def setUp(self, fname='testfile'):
        self.fname = fname
        self.Mobj  = Mock(spec=RemoveObj)
        print ('Creating file ')
        with open(self.fname, 'w') as f:
            f.write('Delete Me')

    def test_RemoveObject(self):
        m = RemoveObj()
        print ('My name is {}'.format(self.Mobj.RemoveObject.os))
        m.RemoveObject(self.fname, self.Mobj.RemoveObject.os)
        self.Mobj.RemoveObject.os.remove.assert_called_with(self.fname)


## in jupyter notebook
#suite = unittest.TestLoader().loadTestsFromTestCase(TestRemoveObject)
#unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()
