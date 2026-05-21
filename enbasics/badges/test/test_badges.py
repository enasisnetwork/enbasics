"""
Functions and routines associated with Enasis Network Project Basics.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from pathlib import Path

from encommon.types.classes import lattrs
from encommon.types.strings import inrepr
from encommon.types.strings import instr
from encommon.types.types import NCTrue
from encommon.utils.files import read_text
from encommon.utils.files import save_text
from encommon.utils.sample import ENPYRWS

from . import SAMPLES
from ..badges import Badge



def test_Badge(
    tmp_path: Path,
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param tmp_path: pytest object for temporal filesystem.
    """


    badge = Badge(
        label='Testing',
        value='success',
        count='69420',
        date='2026-04-20')


    attrs = lattrs(badge)

    assert attrs == ['html']


    assert inrepr(
        'badges.Badge',
        badge)

    assert isinstance(
        hash(badge), int)

    assert instr(
        'badges.Badge',
        badge)


    dumped = badge.html


    sample_path = (
        SAMPLES
        / 'badge.html')

    if ENPYRWS is NCTrue:
        save_text(
            sample_path,
            dumped)

    loaded = read_text(
        sample_path)

    assert dumped == loaded


    output = (
        tmp_path
        / 'badge.png')

    badge.write(output)


    result = output.read_bytes()

    assert b'PNG' in result[:10]



def test_Badge_cover() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    dumped: list[str] = []


    dumped.append(
        Badge(
            label='Testing',
            value='success')
        .html)

    dumped.append(
        Badge(
            label='Testing',
            value='failure')
        .html)

    dumped.append(
        Badge(
            label='Testing',
            value='100%')
        .html)

    dumped.append(
        Badge(
            label='Testing',
            value='81%')
        .html)

    dumped.append(
        Badge(
            label='Testing',
            value='79%')
        .html)

    dumped.append(
        Badge(
            label='Testing',
            value='unknown%')
        .html)


    joined = '\n'.join(dumped)

    sample_path = (
        SAMPLES / 'badges.html')

    if ENPYRWS is NCTrue:
        save_text(
            sample_path,
            joined)

    loaded = read_text(
        sample_path)

    assert joined == loaded
