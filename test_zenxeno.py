# test_zenxeno.py
"""
Tests for ZenXeno module.
"""

import unittest
from zenxeno import ZenXeno

class TestZenXeno(unittest.TestCase):
    """Test cases for ZenXeno class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZenXeno()
        self.assertIsInstance(instance, ZenXeno)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZenXeno()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
