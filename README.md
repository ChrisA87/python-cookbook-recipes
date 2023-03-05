# Python Cookbook Recipes

Useful recipes from the O'Reilly book [Python Cookbook (3rd edition)](https://www.oreilly.com/library/view/python-cookbook-3rd/9781449357337/).

## Setup

1. Consider creating and activating a new [virtual environment](https://virtualenv.pypa.io/en/latest/)
2. Update `PYTHONPATH`
    ```
    export PYTHONPATH=.:$PYTHONPATH
    ```
3. Install dependencies
    ```
    pip install pip-tools
    make pip-install
    ```
4. Check setup by running tests
    ```
    make test
    ```

---

## Usage

### List all recipes
```
python recipes
```

### Run specific recipe
To run the recipe code for chapter 1, example 5:
```
python recipes 1 5
```

### Print recipe code
```
python recipes 1 5 --code
```

### Print the recipe docstring
```
python recipes 1 5 --doc
```

### Create new recipe skeleton
To create recipe 23 under chapter 1:
```
python recipes 1 23 --create "the name of the new recipe"
```

---

## Chapters
1. [Data structures and algorithms](./recipes/01_data_structures_and_algorithms/)
2. [Strings and text](./recipes/02_strings_and_text/)
