### Hexlet tests and linter status:
[![Actions Status](https://github.com/ArturIash/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/ArturIash/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/d9575c9ee1ab0f245fe9/maintainability)](https://codeclimate.com/github/ArturIash/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/d9575c9ee1ab0f245fe9/test_coverage)](https://codeclimate.com/github/ArturIash/python-project-50/test_coverage)


# Difference Generator – gendiff

Program that prints the difference between two files (JSON or YAML) in following formats: stylish, plain, json.

### Installation:
Clone this repository via command:
```bash
git clone git@github.com:ArturIash/python-project-50.git
```

### Makefile
#### Makefile helps you generate packages for your virtual environment.
```make install``` install poetry packages. \
```make build``` build poetry packages. \
```make package-install``` install built package to start using simple commands. \
```make publish``` publish the project to PyPI after making a build.


### Use

to run enter the command:
```gendiff```

for help use: 

```gendiff -h```

for example:

```gendiff path_to_first_file path_to_second_file```

### You can also use format: 
```stylish```  ```plain```    ```json```

for example: 

```gendiff --format json path_to_first_file path_to_second_file```
