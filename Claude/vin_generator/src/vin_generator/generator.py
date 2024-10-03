import random
import string

class VINGenerator:
    def __init__(self):
        self.wmi_codes = {
            'NA': ['1', '2', '3', '4', '5'],
            'EU': ['W', 'S', 'K', 'L', 'Y', 'V', 'T', 'Z'],
            'ROW': ['6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'M', 'N', 'P', 'R']
        }
        self.check_digits = '0123456789X'
        self.valid_chars = string.ascii_uppercase.replace('I', '').replace('O', '').replace('Q', '') + string.digits

    def generate_vin(self, standard=None, region=None, production_volume=None):
        if standard == 'ISO3779':
            return self._generate_iso3779_vin()
        elif region in ['NA', 'EU', 'ROW']:
            return self._generate_regional_vin(region, production_volume)
        else:
            return self._generate_random_vin()

    def _generate_iso3779_vin(self):
        wmi = ''.join(random.choices(self.valid_chars, k=3))
        vds = ''.join(random.choices(self.valid_chars, k=6))
        vis = ''.join(random.choices(self.valid_chars, k=8))
        return wmi + vds + vis

    def _generate_regional_vin(self, region, production_volume):
        wmi = random.choice(self.wmi_codes[region])
        wmi += ''.join(random.choices(self.valid_chars, k=2))
        
        vds = ''.join(random.choices(self.valid_chars, k=5))
        vds += self._get_production_volume_char(production_volume)
        
        vis = self._generate_vis(region)
        
        return wmi + vds + vis

    def _generate_random_vin(self):
        region = random.choice(['NA', 'EU', 'ROW'])
        production_volume = random.choice(['>500', '<500'])
        return self._generate_regional_vin(region, production_volume)

    def _get_production_volume_char(self, production_volume):
        if production_volume == '>500':
            return random.choice(string.digits)
        elif production_volume == '<500':
            return random.choice(string.ascii_uppercase)
        else:
            return random.choice(self.valid_chars)

    def _generate_vis(self, region):
        if region == 'NA':
            year_char = random.choice('ABCDEFGHJKLMNPRSTVWXY123456789')
            plant_code = random.choice(self.valid_chars)
            serial = ''.join(random.choices(string.digits, k=6))
        else:
            year_char = random.choice(self.valid_chars)
            plant_code = random.choice(self.valid_chars)
            serial = ''.join(random.choices(self.valid_chars, k=6))
        
        return year_char + plant_code + serial

    def _calculate_check_digit(self, partial_vin):
        weights = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
        letter_values = {char: index + 1 for index, char in enumerate(string.ascii_uppercase)}
        total = 0

        for i, char in enumerate(partial_vin):
            if char.isalpha():
                value = letter_values[char]
            else:
                value = int(char)
            total += value * weights[i]

        remainder = total % 11
        return 'X' if remainder == 10 else str(remainder)

    def generate_valid_vin(self, **kwargs):
        while True:
            vin = self.generate_vin(**kwargs)
            check_digit = self._calculate_check_digit(vin[:8] + vin[9:])
            if check_digit == vin[8]:
                return vin
