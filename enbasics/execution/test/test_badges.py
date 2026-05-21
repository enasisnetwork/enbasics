"""
Functions and routines associated with Enasis Network Project Basics.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from ..badges import arguments



def test_arguments() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    sargs = arguments([
        '--output', 'output',
        '--label', 'label',
        '--value', 'value',
        '--count', 'count',
        '--date', 'date'])

    assert sargs == {
        'color': None,
        'count': 'count',
        'date': 'date',
        'label': 'label',
        'output': 'output',
        'value': 'value'}
