from pathlib import Path
from importlib import import_module
from pyrecipes import ROOT
from pyrecipes.utils import extract_leading_numbers


class Recipe:
    module = "example"

    def __init__(self, chapter: int, number: int):
        self.chapter = chapter
        self.number = number

    @classmethod
    def from_recipe_path(cls, path: Path):
        chapter = extract_leading_numbers(path.parent.parent.stem)
        number = extract_leading_numbers(path.parent.stem)
        return cls(chapter, number)

    @property
    def path(self):
        result = list(ROOT.glob(f"{self.chapter:0>2}*/{self.number:0>2}*/example.py"))
        return None if not result else result[0]

    @property
    def package(self):
        if self.exists():
            return self.path.parent.parent.parent.stem

    @property
    def chapter_name(self):
        if self.exists():
            return self.path.parent.parent.stem

    @property
    def name(self):
        if self.exists():
            return self.path.parent.stem

    def exists(self):
        return self.path is not None

    def get_module(self):
        if not self.exists():
            raise ModuleNotFoundError(f"This recipe couldn't be found:\n  {self}")
        return import_module(
            f"{self.package}.{self.chapter_name}.{self.name}.{self.module}"
        )

    def get_docstring(self):
        return self.get_module().__doc__.replace("\n", " ")

    def get_code(self):
        return self.path.read_text()

    def run(self):
        if self.exists():
            print(f"Running {self.chapter}.{self.number} \n")
            getattr(self.get_module(), "main")()
            print()
        else:
            print(f"Couldn't find {self}")

    def render(self):
        """TODO"""

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(chapter={self.chapter}, number={self.number})"
        )
