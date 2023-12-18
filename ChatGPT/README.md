# ChatGPT

Using ChatGPT create a random vin generator. 

## Example usage:
`generator = VINGenerator()`

## Random VIN based on a random standard
```
vin_random = generator.generate()
print(vin_random)
```

## Random VIN based on the 'north_america' standard
```
vin_north_america = generator.generate(standard='north_america')
print(vin_north_america)
```

## Random VIN based on the 'europe' standard and more than 500 vehicles
```
vin_500_plus_eu = generator.generate(standard='europe', more_than_500=True)`
print(vin_500_plus_eu)
```

## Unit tests
### Run all tests
`python -m unittest discover tests`

### Run happy path tests only
`python -m unittest tests.test_vin_generator`

### Run sad path tests only
`python -m unittest tests.test_vin_generator_sad_path`

### Run additional tests only
`python -m unittest tests.test_vin_generator_additional`

