# Claude

Using Claude create a random vin generator. 

## Example usage:
`vin_generator = VINGenerator()`

## Random VIN based on a random standard
```
random_vin = vin_generator.generate_valid_vin()
print(random_vin)
```

## Random VIN based on the 'ISO 3779' standard
```
iso_vin = vin_generator.generate_valid_vin(standard='ISO3779')
print(iso_vin)
```

## Generate a North American VIN for a manufacturer producing more than 500 vehicles per year
```
na_vin = vin_generator.generate_valid_vin(region='NA', production_volume='>500')`
print(na_vin)
```

## Generate a European VIN for a manufacturer producing less than 500 vehicles per year
```
eu_vin = vin_generator.generate_valid_vin(region='EU', production_volume='<500')
print(eu_vin)
```

## Unit tests
### Run all tests
`python -m unittest discover tests`

### Run tests
`python -m unittest test_vin_generator.py`
