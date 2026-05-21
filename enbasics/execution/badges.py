"""
Functions and routines associated with Enasis Network Project Basics.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from argparse import ArgumentParser
from sys import argv as sys_argv
from typing import Any
from typing import Optional
from typing import get_args

from ..badges.badges import Badge
from ..badges.common import BadgeColors



def arguments(
    args: Optional[list[str]] = None,
) -> dict[str, Any]:
    """
    Construct arguments which are associated with the file.

    :param args: Override the source for the main arguments.
    :returns: Construct arguments from command line options.
    """

    parser = ArgumentParser()

    args = args or sys_argv[1:]


    parser.add_argument(
        '--output',
        required=True,
        help=(
            'complete or relative '
            'path to output file'))

    parser.add_argument(
        '--label',
        required=True,
        help=(
            'friendly name for '
            'first badge cell'))

    parser.add_argument(
        '--value',
        required=True,
        help=(
            'actual value for '
            'second badge cell'))

    parser.add_argument(
        '--count',
        help=(
            'optional count for '
            'third badge cell'))

    parser.add_argument(
        '--color',
        choices=list(get_args(BadgeColors)),
        help=(
            'color for the value '
            'else automatic'))

    parser.add_argument(
        '--date',
        help=(
            'date for the value '
            'else automatic'))


    return vars(
        parser
        .parse_args(args))



def operation(
    # NOCVR
    pargs: dict[str, Any],
) -> None:
    """
    Perform whatever operation is associated with the file.

    :param pargs: Arguments specified from the command line.
    """

    output = pargs['output']

    badge = Badge(
        label=pargs['label'],
        value=pargs['value'],
        count=pargs['count'],
        color=pargs['color'],
        date=pargs['date'])

    badge.write(output)



def execution(
    # NOCVR
    args: Optional[list[str]] = None,
) -> None:
    """
    Perform whatever operation is associated with the file.

    :param args: Override the source for the main arguments.
    """

    operation(
        arguments(args))



if __name__ == '__main__':
    execution()  # NOCVR
