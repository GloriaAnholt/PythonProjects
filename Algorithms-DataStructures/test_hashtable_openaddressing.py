# Algorithms and Data Structures: Hash Tables & Hashing
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
        # Check basic insertion works
        insert_hash(10, h)
        self.assertEqual(h, [10, None, None, None, None, None, None, None, None, None])
        insert_hash(11, h)
        self.assertEqual(h, [10, 11, None, None, None, None, None, None, None, None])
        # Check that a collision moves to the next open slot
        insert_hash(12, h)  # needs slot 4
        self.assertEqual(h, [10, 11, None, None, 12, None, None, None, None, None])
        insert_hash(8, h)   # needs slot 4
        self.assertEqual(h, [10, 11, None, None, 12, 8, None, None, None, None])
        insert_hash(109, h)  # needs slot 1
        self.assertEqual(h, [10, 11, 109, None, 12, 8, None, None, None, None])
        # Check that a collision wraps around the list to first free slot
        insert_hash(7, h)   # needs slot 9
        self.assertEqual(h, [10, 11, 109, None, 12, 8, None, None, None, 7])
        insert_hash(13, h)  # also needs 9
        self.assertEqual(h, [10, 11, 109, 13, 12, 8, None, None, None, 7])
        # Check that duplicate entries don't do anything
        insert_hash(13, h)
        self.assertEqual(h, [10, 11, 109, 13, 12, 8, None, None, None, 7])
        insert_hash(109, h)
        self.assertEqual(h, [10, 11, 109, 13, 12, 8, None, None, None, 7])

    def test_search_hash(self):
        h = create_table(5)
        # Populate the table
        insert_hash(10, h), insert_hash(11, h), insert_hash(12, h)
        insert_hash(8, h), insert_hash(109, h)
        self.assertEqual(h, [10, 11, 109, None, 12, 8, None, None, None, None])
        # Check that each entry can be found
        self.assertTrue(search_hash(10, h))
        self.assertTrue(search_hash(11, h))
        self.assertTrue(search_hash(109, h))
        self.assertTrue(search_hash(12, h))
        self.assertTrue(search_hash(8, h))
        # Check that same-hash-different-value items can't be found
        self.assertFalse(search_hash(100, h))
        self.assertFalse(search_hash(21, h))
        # Create a wrapping collision, make sure each can be found
        insert_hash(7, h), insert_hash(13, h)
        self.assertEqual(h, [10, 11, 109, 13, 12, 8, None, None, None, 7])
        self.assertTrue(search_hash(13, h))
        self.assertTrue(search_hash(7, h))

    def test_remove_item(self):
        h = create_table(5)
        # Populate the table with starting values
        insert_hash(10, h), insert_hash(11, h), insert_hash(12, h)
        insert_hash(8, h), insert_hash(109, h)
        self.assertEqual(h, [10, 11, 109, None, 12, 8, None, None, None, None])
        # Remove item, make sure it can't be found
        self.assertTrue(remove_item(10, h))
        self.assertEqual(h, ['USED', 11, 109, None, 12, 8, None, None, None, None])
        self.assertFalse(search_hash(10, h))
        # Remove collision-bumped items, make sure they can't be found
        self.assertTrue(remove_item(109, h))
        self.assertEqual(h, ['USED', 11, 'USED', None, 12, 8, None, None, None, None])
        self.assertFalse(search_hash(109, h))
        self.assertTrue(remove_item(8, h))
        self.assertEqual(h, ['USED', 11, 'USED', None, 12, 'USED', None, None, None, None])
        self.assertFalse(search_hash(8, h))
        # Insert into a used slot, make sure item can be found
        insert_hash(10, h)
        self.assertEqual(h, [10, 11, 'USED', None, 12, 'USED', None, None, None, None])
        self.assertTrue(search_hash(10, h))
        # Cause a collision which requires wrapping, remove collided item
        insert_hash(7, h), insert_hash(13, h)
        self.assertEqual(h, [10, 11, 13, None, 12, 'USED', None, None, None, 7])
        self.assertTrue(remove_item(13, h))
        self.assertEqual(h, [10, 11, 'USED', None, 12, 'USED', None, None, None, 7])
        # Check that the same item can't be added, and the one entry is successfully removed
        insert_hash(11, h)
        self.assertEqual(h, [10, 11, 'USED', None, 12, 'USED', None, None, None, 7])
        self.assertTrue(remove_item(11, h))
        self.assertEqual(h, [10, 'USED', 'USED', None, 12, 'USED', None, None, None, 7])
        self.assertFalse(remove_item(11, h))
        # Create a collision which requires wrapping, first remove sets hashed slot to used,
        # locate collided item and remove it
        insert_hash(7, h), insert_hash(13, h)
        self.assertEqual(h, [10, 13, 'USED', None, 12, 'USED', None, None, None, 7])
        self.assertTrue(remove_item(7, h))
        self.assertEqual(h, [10, 13, 'USED', None, 12, 'USED', None, None, None, 'USED'])
        self.assertTrue(remove_item(13, h))
        self.assertEqual(h, [10, 'USED', 'USED', None, 12, 'USED', None, None, None, 'USED'])


if __name__ == '__main__':
    unittest.main()
