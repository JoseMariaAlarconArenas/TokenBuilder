# test_tokenbuilder.py
"""
Tests for TokenBuilder module.
"""

import unittest
from tokenbuilder import TokenBuilder

class TestTokenBuilder(unittest.TestCase):
    """Test cases for TokenBuilder class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TokenBuilder()
        self.assertIsInstance(instance, TokenBuilder)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TokenBuilder()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
