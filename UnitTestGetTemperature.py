import unittest
from RemoveObject import RemoveObject
import os
from unittest import mock
import sys


class TestRemoveObject(unittest.TestCase):

    def setUp(self, fname='testfile'):
        self.fname = fname
        with open(self.fname, 'w') as f:
            f.write('Delete Me')


    @mock.patch('RemoveObject.os')
    def test_RemoveObject(self, rm_os):
        RemoveObject(self.fname)
        self.assertTrue(os.path.exists(self.fname))


## in jupyter notebook
#suite = unittest.TestLoader().loadTestsFromTestCase(TestRemoveObject)
#unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()
