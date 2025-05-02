from importlib.metadata import metadata

infos = metadata(__name__)
__author__ = infos['Author']
__email__ = infos['Author-Email']
__version__ = infos['Version']
