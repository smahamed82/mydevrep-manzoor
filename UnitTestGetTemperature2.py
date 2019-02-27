import unittest
from RemoveObject import RemoveObject
import os
from unittest import mock
import sys


class TestRemoveObject(unittest.TestCase):

    def setUp(self, fname='testfile'):
        self.fname = fname
        with open(self.fname, 'w') as f:
            print ('Creating file and writing it')
            f.write('Delete Me')
            print (os.path.exists(self.fname))

    @mock.patch('RemoveObject.os')
    def test_RemoveObject(self, rm_os):
        print ('Who am is {}'.format(rm_os))
        RemoveObject(self.fname, rm_os)
        self.assertTrue(os.path.exists(self.fname))


## in jupyter notebook
#suite = unittest.TestLoader().loadTestsFromTestCase(TestRemoveObject)
#unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()
