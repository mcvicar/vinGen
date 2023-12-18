import random

class VINGenerator:
    
    def __init__(self):
        self.regions = {
            'iso3779': {'wmi': [], 'vds': []},
            'europe': {'wmi': ['VF', 'W0', 'WV', 'WA', 'ZC', 'ZD', 'ZFA', 'ZFF', 'ZHW', 'ZLA'], 'vds': []},
            'north_america': {'wmi': ['1G', '1N', '1Y', '2G', '2M', '2N', '3D', '3G', '3N', '4F'], 'vds': []},
            'rest_of_world': {'wmi': ['JT', 'JN', 'JA', 'JF', 'JL', 'JU', 'JS', 'J5', 'J6', 'J7', 'J8', 'JD', 'JE', 'JH', 'J3', 'J4', 'J9', 'KL', 'KM', 'KN', 'KP', 'K3', 'K4', 'K5', 'K6', 'K7', 'LA', 'LJ', 'LL', 'L5', 'L6', 'L9', 'LT', 'LV', 'L8', 'LS', 'L0', 'LU'], 'vds': []}
        }

    def generate(self, standard=None, more_than_500=None):
        if standard:
            if standard not in self.regions:
                raise ValueError(f"Invalid standard: {standard}")
        else:
            standard = random.choice(list(self.regions.keys()))

        wmi = self._get_random_wmi(standard)
        vds = self._get_random_vds(standard)

        if more_than_500 is not None:
            if more_than_500:
                vis = self._get_random_more_than_500_vis()
            else:
                vis = self._get_random_500_or_less_vis()
        else:
            vis = self._get_random_vis()

        check_digit = self._calculate_check_digit(wmi + vds + vis)
        return wmi + vds + vis + check_digit

    def _get_random_wmi(self, standard):
        if not self.regions[standard]['wmi']:
            raise ValueError(f"No valid WMI codes for {standard} standard.")
        return random.choice(self.regions[standard]['wmi'])

    def _get_random_vds(self, standard):
        if not self.regions[standard]['vds']:
            self.regions[standard]['vds'] = [''.join(random.choices('0123456789ABCDEFGHJKLMNPRSTUVWXYZ', k=1)) for _ in range(6)]
        return random.choice(self.regions[standard]['vds'])

    def _get_random_vis(self):
        return ''.join(random.choices('0123456789ABCDEFGHJKLMNPRSTUVWXYZ', k=8))

    def _get_random_more_than_500_vis(self):
        return ''.join(random.choices('0123456789ABCDEFGHJKLMNPRSTUVWXYZ', k=7)) + '1'

    def _get_random_500_or_less_vis(self):
        return ''.join(random.choices('0123456789ABCDEFGHJKLMNPRSTUVWXYZ', k=8))

    def _calculate_check_digit(self, vin):
        weights = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
        total = sum(int(digit) * weight for digit, weight in zip(vin, weights))
        remainder = total % 11
        if remainder == 10:
            return 'X'
        else:
            return str(remainder)
