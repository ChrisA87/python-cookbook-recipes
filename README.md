# Python Cookbook Recipes

![ci workflow]
(https://github.com/ChrisA87/pyrecipes/actions/workflows/ci.yml/badge.svg)

Useful recipes from David Beazley & Brian K. Jones' O'Reilly book [Python Cookbook (3rd edition)](https://www.oreilly.com/library/view/python-cookbook-3rd/9781449357337/).

Original code samples at https://github.com/dabeaz/python-cookbook

This project implements a simple CLI tool to list, run and view recipes.

## Setup

1. Consider creating and activating a new [virtual environment](https://virtualenv.pypa.io/en/latest/)
2. Clone this repo
3. cd into the project root and run `pip install .`
4. Run `recipes` to confirm successful install 

---

## Example Usage

### Show recipes help and subcommands
```
recipes
```

### List all chapters
```
recipes chapters
```

### List all recipes
```
recipes ls
```

### List all recipes in a specific chapter
```
recipes ls -c 1
```

### List all recipes in a specific chapter with a short description
```
recipes ls -c 1 -d
```

### Show recipe code
```
recipes show 1 3
```

### Run the recipe as a script
```
recipes run 1 3
```

### Search for recipes containing a pattern
```
recipes search 'islice'
recipes search 'islice' --color green
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
