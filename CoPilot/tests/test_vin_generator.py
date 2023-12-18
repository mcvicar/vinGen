import unittest
from vin_generator import VINGenerator

class TestVINGenerator(unittest.TestCase): # This is a test class (subclass of unittest.TestCase)
    def setUp(self): # This method is called before each test
        self.vin_generator = VINGenerator() # Create an instance of VINGenerator

    def test_generate(self): # This is a test method
        vin = self.vin_generator.generate() # Generate a VIN
        self.assertEqual(len(vin), 17) # Test that the VIN is 17 characters long
        self.assertEqual(vin[8], 'X') # Test that the 9th character is an 'X'
        self.assertTrue(self.vin_generator.validate(vin)) # Test that the VIN is valid

    def test_validate(self): # This is a test method
        vin = '1M8GDM9AXKP042788' # This is a valid VIN
        self.assertTrue(self.vin_generator.validate(vin)) # Test that the VIN is valid
        vin = '1M8GDM9AXKP042789' # This is an invalid VIN
        self.assertFalse(self.vin_generator.validate(vin)) # Test that the VIN is invalid

    def tearDown(self): # This method is called after each test
        self.vin_generator = None # Delete the instance of VINGenerator