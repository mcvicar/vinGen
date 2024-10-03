import unittest
import re
from vin_generator import VINGenerator

class TestVINGenerator(unittest.TestCase):
    def setUp(self):
        self.vin_generator = VINGenerator()

    def test_generate_random_vin(self):
        vin = self.vin_generator.generate_valid_vin()
        self.assertEqual(len(vin), 17)
        self.assertTrue(all(c in self.vin_generator.valid_chars for c in vin))

    def test_generate_iso3779_vin(self):
        vin = self.vin_generator.generate_valid_vin(standard='ISO3779')
        self.assertEqual(len(vin), 17)
        self.assertTrue(all(c in self.vin_generator.valid_chars for c in vin))

    def test_generate_na_vin(self):
        vin = self.vin_generator.generate_valid_vin(region='NA', production_volume='>500')
        self.assertEqual(len(vin), 17)
        self.assertIn(vin[0], self.vin_generator.wmi_codes['NA'])
        self.assertTrue(vin[6].isdigit())

    def test_generate_eu_vin(self):
        vin = self.vin_generator.generate_valid_vin(region='EU', production_volume='<500')
        self.assertEqual(len(vin), 17)
        self.assertIn(vin[0], self.vin_generator.wmi_codes['EU'])
        self.assertTrue(vin[6].isalpha())

    def test_generate_row_vin(self):
        vin = self.vin_generator.generate_valid_vin(region='ROW')
        self.assertEqual(len(vin), 17)
        self.assertIn(vin[0], self.vin_generator.wmi_codes['ROW'])

    def test_check_digit_calculation(self):
        vin = self.vin_generator.generate_valid_vin()
        check_digit = self.vin_generator._calculate_check_digit(vin[:8] + vin[9:])
        self.assertEqual(vin[8], check_digit)

    def test_vin_uniqueness(self):
        vins = [self.vin_generator.generate_valid_vin() for _ in range(1000)]
        self.assertEqual(len(vins), len(set(vins)))

    def test_invalid_standard(self):
        with self.assertRaises(ValueError):
            self.vin_generator.generate_valid_vin(standard='INVALID')

    def test_invalid_region(self):
        with self.assertRaises(ValueError):
            self.vin_generator.generate_valid_vin(region='INVALID')

    def test_invalid_production_volume(self):
        with self.assertRaises(ValueError):
            self.vin_generator.generate_valid_vin(region='NA', production_volume='INVALID')

    def test_vin_format(self):
        vin = self.vin_generator.generate_valid_vin()
        self.assertTrue(re.match(r'^[A-HJ-NPR-Z0-9]{17}$', vin))

    def test_excluded_characters(self):
        vin = self.vin_generator.generate_valid_vin()
        self.assertNotIn('I', vin)
        self.assertNotIn('O', vin)
        self.assertNotIn('Q', vin)

    def test_production_volume_character(self):
        vin_high = self.vin_generator.generate_valid_vin(region='NA', production_volume='>500')
        self.assertTrue(vin_high[6].isdigit())
        
        vin_low = self.vin_generator.generate_valid_vin(region='NA', production_volume='<500')
        self.assertTrue(vin_low[6].isalpha())

    def test_na_year_character(self):
        vin = self.vin_generator.generate_valid_vin(region='NA')
        self.assertIn(vin[9], 'ABCDEFGHJKLMNPRSTVWXY123456789')

    def test_consistent_check_digit(self):
        vin = self.vin_generator.generate_valid_vin()
        for _ in range(100):
            self.assertEqual(vin[8], self.vin_generator._calculate_check_digit(vin[:8] + vin[9:]))

if __name__ == '__main__':
    unittest.main()
