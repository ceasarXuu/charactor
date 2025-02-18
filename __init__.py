"""Top-level package for charactor."""

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY",
]

__author__ = """charactor"""
__email__ = "zhangxu.201712@gmail.com"
__version__ = "0.0.1"

from .src.charactor.nodes import NODE_CLASS_MAPPINGS
from .src.charactor.nodes import NODE_DISPLAY_NAME_MAPPINGS

WEB_DIRECTORY = "./web"
