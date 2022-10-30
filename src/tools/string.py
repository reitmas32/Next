######################################################################
# author = Rafael Zamora
# copyright = Copyright 2020-2022, Next Project
# date = 02/06/2022
### license = PSF
# version = 3.4.0
# maintainer = Rafael Zamora
### email = rafa.zamora.ram@gmail.com
### status = Production
######################################################################

# System Packages
import re

# Local Package
from src.domain.types.null_smart_t import NullSmart_t

def stripComments(code: str) -> str:
    """strip Comments from source use '#'

    Args:
        code (str): Source Code

    Returns:
        str: Source Code Without comments
    """
    code = str(code)
    return re.sub(r'(?m)^ *#.*\n?', '', code)


def countWord(text: str, separator: str = " ") -> int:
    """Count Words on text

    Args:
        text (str): Text
        separator (str, optional): Separator Char. Defaults to " ".

    Returns:
        int: Num Words in text
    """
    text_list = listToStr(text, sep=separator)
    return len(text_list)


def listToStr(list: list, separator: str = NullSmart_t) -> str:
    """Generate Str from list

    Args:
        list (list): List input
        separator (str, optional): Separator Char. Defaults to NullType_t.

    Returns:
        str: String output
    """
    str1 = ""
    for e in list:
        str1 += e
        if separator:
            str1 += separator
    return str1
