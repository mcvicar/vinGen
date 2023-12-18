import random

class VINGenerator:
    def __init__(self):
        self.vin = ''
        self.vin_dict = {
            'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5',
            'F': '6', 'G': '7', 'H': '8', 'J': '1', 'K': '2',
            'L': '3', 'M': '4', 'N': '5', 'P': '7', 'R': '9',
            'S': '2', 'T': '3', 'U': '4', 'V': '5', 'W': '6',
            'X': '7', 'Y': '8', 'Z': '9'
        }
        self.vin_weights = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]

    def generate(self):
        self.vin = ''
        for i in range(0, 17):
            if i == 8:
                self.vin += 'X'
            else:
                self.vin += random.choice(list(self.vin_dict.keys()))
        self.vin = self.vin[0:8] + self.vin_dict[self.vin[8]] + self.vin[9:]
        self.vin = self.vin[0:8] + self.vin_dict[self.vin[8]] + self.vin[9:]
        return self.vin

    def validate(self, vin):
        if len(vin) != 17:
            return False
        vin = vin.upper()
        if vin[8] == 'X':
            vin = vin[0:8] + 'X' + vin[9:]
        vin = vin[0:8] + self.vin_dict[vin[8]] + vin[9:]
        vin = vin[0:8] + self.vin_dict[vin[8]] + vin[9:]
        sum = 0
        for i in range(0, 17):
            sum += self.vin_weights[i] * int(vin[i])
        return sum % 11 == 0