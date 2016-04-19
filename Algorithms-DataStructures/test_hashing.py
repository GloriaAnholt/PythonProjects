# Algorithms and Data Structures: hash Tables & Hashing
# 4.19.2016
# @totallygloria



import unittest
from hashing import create_table, insert_hash, extend_hash, search_hash


class HashClassTester(unittest.TestCase):

    def test_create_table(self):
        self.assertEqual(create_table(0), [])
        self.assertEqual(create_table(1), [None, None])
        self.assertEqual(create_table(2), [None, None, None, None])
        self.assertEqual(create_table(8), ([None]*16))

    def test_insert_hash(self):
        h = create_table(5)
        insert_hash(10, h)
        self.assertEqual(h, [10, None, None, None, None, None, None, None, None, None])
        insert_hash(11, h)
        self.assertEqual(h, [10, 11, None, None, None, None, None, None, None, None])
        insert_hash(12, h)
        self.assertEqual(h, [10, 11, 12, None, None, None, None, None, None, None])
        insert_hash(17, h)
        self.assertEqual(h, [10, 11, 12, None, None, None, None, 17, None, None])
        insert_hash(109, h)
        self.assertEqual(h, [10, 11, 12, None, None, None, None, 17, None, 109])
        insert_hash(20, h)
        self.assertEqual(h, [set([10,20]), 11, 12, None, None, None, None, 17, None, 109])
        insert_hash(30, h)
        self.assertEqual(h, [set([10,20,30]), 11, 12, None, None, None, None, 17, None, 109])
        insert_hash(30, h)
        self.assertEqual(h, [set([10,20,30]), 11, 12, None, None, None, None, 17, None, 109])

    def test_extend_hash(self):
        h = create_table(5)
        extend_hash([10,11,12], h)
        self.assertEqual(h, [10, 11, 12, None, None, None, None, None, None, None])
        extend_hash([106,108,109], h)
        self.assertEqual(h, [10, 11, 12, None, None, None, 106, None, 108, 109])
        extend_hash([10,20,30,40], h)
        self.assertEqual(h, [set([10,20,30,40]), 11, 12, None, None, None, 106, None, 108, 109])

    def test_search_hash(self):
        h = create_table(5)
        extend_hash([10,11,12,106,108,109], h)
        extend_hash([10,20,30,40], h)
        self.assertTrue(search_hash(10, h))
        self.assertTrue(search_hash(20, h))
        self.assertTrue(search_hash(30, h))
        self.assertTrue(search_hash(106, h))
        self.assertTrue(search_hash(109, h))
        self.assertFalse(search_hash(50, h))
        self.assertFalse(search_hash(107, h))


if __name__ == '__main__':
    unittest.main()
