import unittest
from vin_generator import VINGenerator

class TestVINGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = VINGenerator()

    def test_generate_random_vin(self):
        vin = self.generator.generate()
        self.assertIsInstance(vin, str)
        self.assertEqual(len(vin), 17)

    def test_generate_north_america_vin(self):
        vin = self.generator.generate(standard='north_america')
        self.assertTrue(vin.startswith(('1G', '1N', '1Y', '2G', '2M', '2N', '3D', '3G', '3N', '4F')))
        self.assertEqual(len(vin), 17)

    def test_generate_europe_vin_more_than_500(self):
        vin = self.generator.generate(standard='europe', more_than_500=True)
        self.assertTrue(vin.startswith(('VF', 'W0', 'WV', 'WA', 'ZC', 'ZD', 'ZFA', 'ZFF', 'ZHW', 'ZLA')))
        self.assertEqual(len(vin), 17)

    def test_generate_iso3779_vin_500_or_less(self):
        vin = self.generator.generate(standard='iso3779', more_than_500=False)
        self.assertEqual(len(vin), 17)

    def test_generate_random_vin_more_than_500(self):
        vin = self.generator.generate(more_than_500=True)
        self.assertEqual(len(vin), 17)

    def test_generate_random_vin_500_or_less(self):
        vin = self.generator.generate(more_than_500=False)
        self.assertEqual(len(vin), 17)

    def test_generate_invalid_standard(self):
        with self.assertRaises(ValueError):
            self.generator.generate(standard='invalid_standard')

    def test_generate_invalid_region(self):
        with self.assertRaises(ValueError):
            self.generator.generate(standard='europe', region='invalid_region')

    def test_generate_invalid_more_than_500(self):
        with self.assertRaises(ValueError):
            self.generator.generate(more_than_500='invalid_value')


if __name__ == '__main__':
    unittest.main()
