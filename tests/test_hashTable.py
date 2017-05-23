from unittest import TestCase


class TestHashTable(TestCase):
    def test_set(self):
        try:
            from build import HashTable
        except ImportError:
            self.assertFalse("no function found")
        hash_table = HashTable(10)
        hash_table.set(0, 'foo')
        hash_table.set(1, 'bar')
        self.assertEqual(hash_table.get(1), 'bar')

    def test_get(self):
        try:
            from build import HashTable
        except ImportError:
            self.assertFalse("no function found")
        hash_table = HashTable(10)
        self.assertRaises(KeyError, hash_table.get, 0)

    def test_remove(self):
        try:
            from build import HashTable
        except ImportError:
            self.assertFalse("no function found")
        hash_table = HashTable(10)
        hash_table.set(0, 'foo')
        hash_table.set(1, 'bar')
        hash_table.remove(1)
        self.assertRaises(KeyError, hash_table.get, 1)
        hash_table.remove(0)
        self.assertRaises(KeyError, hash_table.get, 0)