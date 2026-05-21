"""
Functions and routines associated with Enasis Network Project Basics.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from pathlib import Path

from _pytest.capture import CaptureFixture

from encommon.types.types import NCTrue
from encommon.utils.files import read_text
from encommon.utils.files import save_text
from encommon.utils.sample import ENPYRWS
from encommon.utils.stdout import strip_ansi

from . import SAMPLES
from ..makefile import makefile
from ..makefile import makeout
from ... import PROJECT



def test_makeout(
    capsys: CaptureFixture[str],
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param capsys: pytest object for capturing print message.
    """

    makeout(
        string='Testing',
        prefix='base',
        method='print')

    makeout(
        string='Testing',
        prefix='more',
        method='print')

    makeout(
        string='Testing',
        prefix='text',
        method='print')

    output = capsys.readouterr().out

    dumped = strip_ansi(output)


    sample_path = (
        SAMPLES / 'makeout.txt')

    if ENPYRWS is NCTrue:
        save_text(
            sample_path,
            dumped)

    loaded = read_text(
        sample_path)

    assert dumped == loaded



def test_makefile(
    capsys: CaptureFixture[str],
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param capsys: pytest object for capturing print message.
    """

    path = (
        PROJECT.parent
        / 'Makefile')

    makefile(
        path=str(path),
        name='Project',
        version='4.2.0',
        method='print')

    output = capsys.readouterr().out

    dumped = strip_ansi(output)


    sample_path = (
        SAMPLES / 'makefile.txt')

    if ENPYRWS is NCTrue:
        save_text(
            sample_path,
            dumped)

    loaded = read_text(
        sample_path)

    assert dumped == loaded



def test_makefile_cover(
    capsys: CaptureFixture[str],
    tmp_path: Path,
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param capsys: pytest object for capturing print message.
    :param tmp_path: pytest object for temporal filesystem.
    """

    path = (
        tmp_path
        / 'Makefile')

    path.touch()

    makefile(path)

    output = capsys.readouterr().out

    dumped = strip_ansi(output)

    assert len(dumped) == 0
