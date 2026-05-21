"""
Functions and routines associated with Enasis Network Project Basics.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from pathlib import Path
from re import MULTILINE
from re import findall as re_findall
from re import sub as re_sub
from sys import stdout
from typing import Literal
from typing import Optional



_PREFIX = Literal[
    'text', 'base', 'more']

_PATTERN = (
    r'\n([a-z]\S+)\:(\s+\\\n)?'
    r'((\s+[^\n]+){1,2})?\n'
    r'\s+\@##\s([^\n]+)?\n')



def makeout(
    string: str,
    prefix: Optional[_PREFIX] = None,
    method: Literal['stdout', 'print'] = 'stdout',
    color: Optional[int] = 7,
) -> None:
    """
    Print the ANSI colorized string to the standard output.

    .. note::
       This function is forgiving due to use with Makefile.

    :param string: String processed using inline directives.
    :param prefix: Determine if and which prefix prepended.
    :param method: Which method for standard output is used.
    :param color: Optional color override default ANSI gray.
    """

    pattern = r'\<c([\d\;]+)\>'
    replace = r'\033[0;\1m'


    if prefix is not None:

        string = (
            string
            .lstrip(' '))

        padding = 3
        _prefix = ''

        if prefix == 'base':
            padding = 0
            _prefix = '<cL>>>><c0>'

        elif prefix == 'more':
            padding = 2
            _prefix = '<cL>●<c0>'

        space: str = ' '

        string = (
            f'{space * padding}'
            f'{_prefix} {string}')


    string = (
        f'{string}'
        .replace(
            '<cD>',
            f'<c3{color}>')
        .replace(
            '<cL>',
            f'<c9{color}>'))

    string = re_sub(
        pattern,
        replace,
        string)


    if method == 'stdout':
        stdout.write(f'{string}\n')
    else:
        print(string)  # noqa: T201



def makeread(
    path: Path | str,
) -> str:
    """
    Return the contents using the provided filesystem path.

    :param path: Complete or relative path to the makefile.
    :returns: Contents using the provided filesystem path.
    """

    if isinstance(path, str):
        path = Path(path)

    return path.read_text(
        encoding='utf-8')



def makefile(
    path: Path | str = 'Makefile',
    *,
    name: Optional[str] = None,
    version: Optional[str] = None,
    method: Literal['stdout', 'print'] = 'stdout',
    color: Optional[int] = 7,
) -> None:
    """
    Print the Makefile summary in the human friendly format.

    :param path: Complete or relative path to the makefile.
    :param name: Name of the project to show in the console.
    :param version: Version of projects to show beside name.
    :param method: Which method for standard output is used.
    :param color: Optional color override default ANSI gray.
    """

    contents = makeread(path)

    matches = re_findall(
        pattern=_PATTERN,
        string=contents,
        flags=MULTILINE)

    if len(matches) == 0:
        return


    if name is not None:

        _version = (
            f'/<c37>{version}<c0>'
            if version is not None
            else '')

        makeout(
            f' <c3{color}>'
            f'{name}<c0>{_version}'
            f' <c90>Makefile<c0>\n')


    for match in matches:

        string = (
            (f'  <c9{color}>'
             f'{match[0]}  '
             f'<c0>{match[4]}')
            .rstrip('\n'))

        makeout(
            string=string,
            method=method,
            color=color)
