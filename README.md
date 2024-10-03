# VINGen
A few moons ago I was working on something that was generating fake user data using [Faker](https://github.com/joke2k/faker). One of the things we wanted was to generate a [VIN](https://en.wikipedia.org/wiki/Vehicle_identification_number) in our "fake" dataset, which Faker doesn't do. We considered creating our own provider, but decided against it, as it wasn't super important that it be valid.

The advent of AI started, and it has become by go-to for asking AI to create a class and unit tests in Python.

## The Prompts

### The class prompt. 
```
Write a class in python that will generate a random compliant VIN to the ISO 3779, European, North American and Rest of World standards. When I call the class it should return any valid random VIN from those standards. However, I should be able to optionally specify the specific standard I want generated, such as the ISO 3779 standard, or if there are more than or less than 500 vehicles per year in a specific region (NA, EU, Rest of World).
Write this class as if my personal and professional reputation is at stake.
```

### The unit test prompt
```
Lets create some happy and sad path unit tests for this class. 
Write these unit tests as if my personal and professional reputation is at stake.
```

### The code structure
```
What filename and directory structure should I give the class and unit tests?
```


## I didn't write this
Let me repeat this, I didn't write any of this code. I merely created the prompts that generated the code. The prompts are saved as git commit messages. 

I haven't put a license on this because of all the issues with AI generated code. This is just an experiment to track how well different AI systems generate this class and unit test using a well published rule set. 
