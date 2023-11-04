# Python Cookbook Recipes

Useful recipes from David Beazley & Brian K. Jones' O'Reilly book [Python Cookbook (3rd edition)](https://www.oreilly.com/library/view/python-cookbook-3rd/9781449357337/).

Original code samples at https://github.com/dabeaz/python-cookbook

This project implements a simple CLI tool to list, run and view recipes.

## Setup

1. Consider creating and activating a new [virtual environment](https://virtualenv.pypa.io/en/latest/)
2. Clone this repo
3. cd into the project root and run `pip install .`
4. Run `recipes` to confirm successful install 

---

## Usage

### List all recipes
```
recipes
```

### List all recipes in chapter 1
```
recipes 1
```

### Run specific recipe
To run the recipe code for chapter 1, example 5:
```
recipes 1 5
```

### Print recipe code
```
recipes 1 5 --code
```

### Print the recipe docstring
```
recipes 1 5 --doc
```

### Create new recipe skeleton
To create recipe 23 under chapter 1:
```
recipes 1 23 --create "the name of the new recipe"
```

---

## Chapters
1. [Data structures and algorithms](./pyrecipes/01_data_structures_and_algorithms/)
2. [Strings and text](./pyrecipes/02_strings_and_text/)
3. [Numbers, dates and times](./pyrecipes/03_numbers_dates_and_times/)
4. [Iterators and generators](./pyrecipes/04_iterators_and_generators/)
5. [Files and I/O](./pyrecipes/05_files_and_io/)
6. [Data Encoding and Processing](./pyrecipes/06_data_encoding_and_processing/)
7. [Functions](./pyrecipes/07_functions/)
8. [Classes and Objects](./pyrecipes/08_classes_and_objects/)
9. [Metaprogramming](./pyrecipes/09_metaprogramming/)
10. [Modules and Packages](./pyrecipes/10_modules_and_packages/)
11. [Networking and Web Programming](./pyrecipes/11_networking_and_web_programming/)
12. [Concurrency](./pyrecipes/12_concurrency/)
