# test_cryptovault.py
"""
Tests for CryptoVault module.
"""

import unittest
from cryptovault import CryptoVault

class TestCryptoVault(unittest.TestCase):
    """Test cases for CryptoVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoVault()
        self.assertIsInstance(instance, CryptoVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
