import unittest
from version_string import compare_version, CompareResult


class VersionCompareTest(unittest.TestCase):
    def test_ordinary_versions(self):
        self.assertEqual(CompareResult.LESS, compare_version('2.3', '2.2'))
        self.assertEqual(CompareResult.GREATER, compare_version('2.2', '2.3'))
        self.assertEqual(CompareResult.EQUAL, compare_version('2.2', '2.2'))
        self.assertEqual(CompareResult.LESS, compare_version('2.3.b', '2.3.a'))
        self.assertEqual(CompareResult.GREATER, compare_version('2.2.a', '2.2.z'))
        self.assertEqual(CompareResult.EQUAL, compare_version('2.2.3', '2.2.3'))

    def test_special_versions_compare(self):
        self.assertEqual(CompareResult.GREATER, compare_version('2', '2.2'))
        self.assertEqual(CompareResult.LESS, compare_version('2.2', '2'))
        self.assertEqual(CompareResult.LESS, compare_version('2.2.a', '2.2'))
        self.assertEqual(CompareResult.LESS, compare_version('2.2.a', '2'))
        self.assertEqual(CompareResult.EQUAL, compare_version('02.0', '2'))
