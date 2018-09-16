import mock
import unittest

import leet382_linked_list_random_node as linked_list_random_node


class Test382(unittest.TestCase):

    @mock.patch('os.urandom')
    def test_linked_list_random_node(self, mock_random):
        expected = [2, 30]
        mock_random.side_effect = ['\x00\x00\x00\x00\x00\x00\x00\x01',
                                   '\x00\x00\x00\x00\x00\x00\x00\x04']

        for entry, input in enumerate(linked_list_random_node.myinput):
            self.assertEqual(linked_list_random_node.leetSolve(input),
                             expected[entry])

    @mock.patch('os.urandom')
    def test_linked_list_random_node_clever(self, mock_random):
        expected = [2, 30]
        mock_random.side_effect = ['\x00\x00\x00\x00\x00\x00\x00\x02',
                                   '\x00\x00\x00\x00\x00\x00\x00\x05']

        for entry, input in enumerate(linked_list_random_node.myinput):
            self.assertEqual(linked_list_random_node.leetSolveClever(input),
                             expected[entry])
