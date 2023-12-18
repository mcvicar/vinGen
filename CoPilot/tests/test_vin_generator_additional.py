import unittest
from vin_generator import VINGenerator

class TestVINGeneratorAdditional(unittest.TestCase):   
    def test_vin_generator_additional(self):
        vin_generator = VINGenerator()
        self.assertEqual(vin_generator.generate_vin('1M8GDM9A_KP042788', '2019-01-01', '2019-01-01'), '1M8GDM9A_KP042788')
        self.assertEqual(vin_generator.generate_vin('1M8GDM9A_KP042788', '2019-01-01', '2019-01-02'), '1M8GDM9A_KP042788')
        self.assertEqual(vin_generator.generate_vin('1M8GDM9A_KP042788', '2019-01-01', '2019-01-03'), '1M8GDM9A_KP042788')
        self.assertEqual(vin_generator.generate_vin('1M8GDM9A_KP042788', '2019-01-01', '2019-01-04'), '1M8GDM9A_KP042788')
        self.assertEqual(vin_generator.generate_vin('1M8GDM9A_KP042788', '2019-01-01', '2019-01-05'), '1M8GDM9A_KP042788')
        self.assertEqual(vin_generator.generate_vin('1M8GDM9A_KP042788', '2019-01-01', '2019-01-06'), '1M8GDM9A_KP042788')
        self.assertEqual(vin_generator.generate_vin('1M8GDM9A_KP042788', '2019-01-01', '2019-01-07'), '1M8GDM9A_KP042788')
        self.assertEqual(vin_generator.generate_vin('1M8GDM9A_KP042788', '2019-01-01', '2019-01-08'), '1M8GDM9A_KP042788')
        self.assertEqual(vin_generator.generate_vin('1M8GDM9A_KP042788', '2019-01-01', '2019-01-09'), '1M8GDM9A_KP042788')

        self.assertEqual(vin_generator.generate_vin('1M8GDM9A_KP042788', '2019-01-01', '2019-02-01'), '1M8GDM9A_KP042788')
        self.assertEqual(vin_generator.generate_vin('1M8GDM9A_KP042788', '2019-01-01', '2020-01-01'), '1M8GDM9A_KP042788')