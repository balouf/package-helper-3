"""Top-level package for {{ cookiecutter.project_name }}."""

from importlib.metadata import metadata

from {{ cookiecutter.package_name }}.sub_package_1.my_class_1 import MyClass1 as MyClass1
from {{ cookiecutter.package_name }}.sub_package_2.my_class_2 import MyClass2 as MyClass2
from {{ cookiecutter.package_name }}.sub_package_2.my_class_3 import MyClass3 as MyClass3


infos = metadata(__name__)
__version__ = infos["Version"]
__author__ = "{{ cookiecutter.full_name }}"
__email__ = "{{ cookiecutter.email }}"
