# Algorithms and Data Structures: hash Tables & Hashing
# 4.19.2016
# @totallygloria



import unittest
from hash_open_addressing import create_table, insert_hash, search_hash, remove_item


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
        self.assertEqual(h, [10, 11, None, None, 12, None, None, None, None, None])
        insert_hash(8, h)
        self.assertEqual(h, [10, 11, None, None, 12, 8, None, None, None, None])
        insert_hash(109, h)
        self.assertEqual(h, [10, 11, 109, None, 12, 8, None, None, None, None])
        insert_hash(7, h)
        self.assertEqual(h, [10, 11, 109, None, 12, 8, None, None, None, 7])
        insert_hash(13, h)
        self.assertEqual(h, [10, 11, 109, 13, 12, 8, None, None, None, 7])

    def test_search_hash(self):
        h = create_table(5)
        insert_hash(10, h), insert_hash(11, h), insert_hash(12, h)
        insert_hash(8, h), insert_hash(109, h)
        self.assertEqual(h, [10, 11, 109, None, 12, 8, None, None, None, None])
        self.assertTrue(search_hash(10, h))
        self.assertTrue(search_hash(11, h))
        self.assertTrue(search_hash(109, h))
        self.assertTrue(search_hash(12, h))
        self.assertTrue(search_hash(8, h))
        insert_hash(7, h), insert_hash(13, h)
        self.assertEqual(h, [10, 11, 109, 13, 12, 8, None, None, None, 7])

    def test_remove_item(self):
        h = create_table(5)
        insert_hash(10, h), insert_hash(11, h), insert_hash(12, h)
        insert_hash(8, h), insert_hash(109, h)
        self.assertEqual(h, [10, 11, 109, None, 12, 8, None, None, None, None])
        self.assertTrue(remove_item(10, h))
        self.assertEqual(h, ['USED', 11, 109, None, 12, 8, None, None, None, None])
        self.assertFalse(search_hash(10, h))
        self.assertTrue(remove_item(109, h))
        self.assertEqual(h, ['USED', 11, 'USED', None, 12, 8, None, None, None, None])
        self.assertFalse(search_hash(109, h))
        self.assertTrue(remove_item(8, h))
        self.assertEqual(h, ['USED', 11, 'USED', None, 12, 'USED', None, None, None, None])
        self.assertFalse(search_hash(8, h))
        insert_hash(10, h)
        self.assertEqual(h, [10, 11, 'USED', None, 12, 'USED', None, None, None, None])
        self.assertTrue(search_hash(10, h))
        insert_hash(7, h), insert_hash(13, h)  # A collision which requires wrapping
        self.assertEqual(h, [10, 11, 13, None, 12, 'USED', None, None, None, 7])
        self.assertTrue(remove_item(13, h))
        self.assertEqual(h, [10, 11, 'USED', None, 12, 'USED', None, None, None, 7])
        insert_hash(11, h)
        self.assertEqual(h, [10, 11, 11, None, 12, 'USED', None, None, None, 7])
        insert_hash(11, h)
        self.assertEqual(h, [10, 11, 11, 11, 12, 'USED', None, None, None, 7])
        self.assertTrue(remove_item(11, h))
        self.assertEqual(h, [10, 'USED', 11, 11, 12, 'USED', None, None, None, 7])
        self.assertTrue(remove_item(11, h))
        self.assertEqual(h, [10, 'USED', 'USED', 11, 12, 'USED', None, None, None, 7])
        self.assertTrue(remove_item(11, h))
        self.assertEqual(h, [10, 'USED', 'USED', 'USED', 12, 'USED', None, None, None, 7])


if __name__ == '__main__':
    unittest.main()
