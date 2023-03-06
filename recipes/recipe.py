from pathlib import Path
from importlib import import_module


class Recipe:
    def __init__(self, path: Path):
        if not str(path).endswith('example.py'):
            raise ValueError(f'Expects a recipe module "example.py" - got {path}')
        self.path = path
        self._package = path.parent.parent.parent.stem
        self._chapter = path.parent.parent.stem
        self._example = path.parent.stem
        self._module = path.stem

    @property
    def package(self):
        return self._package

    @property
    def chapter(self):
        return self._clean_text(self._chapter).title()

    @property
    def example(self):
        return self._clean_text(self._example)

    @property
    def module(self):
        return self._module

    @staticmethod
    def _clean_text(text):
        num, text = text.split('_', maxsplit=1)
        return f"{int(num):>2}) {text.replace('_', ' ').capitalize()}"

    def exists(self):
        return self.path.exists()

    def get_module(self):
        if not self.exists():
            raise ModuleNotFoundError(f'This recipe couldn\'t be found:\n  {self}')
        return import_module(f"{self._package}.{self._chapter}.{self._example}.{self.module}")

    def get_docstring(self):
        return self.get_module().__doc__.replace('\n', ' ')

    def get_code(self):
        return self.path.read_text()

    def run(self):
        if self.exists():
            print('Running... \n')
            getattr(self.get_module(), 'main')()
            print()
        else:
            print(f'Couldn\'t find recipe {self.example}')

    def __repr__(self):
        return (f"{self.chapter}\n"
                f"  {self.example}")
