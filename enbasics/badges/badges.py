"""
Functions and routines associated with Enasis Network Project Basics.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from datetime import datetime
from datetime import timezone
from io import BytesIO
from pathlib import Path
from typing import Literal
from typing import Optional

from dateutil import parser
from dateutil.parser import ParserError

from .common import BadgeColors



_STAMP = '%m/%d/%Y'

_SUCCESS = ['success', 'passing']
_FAILURE = ['failure', 'failing']

_STYLES = (
    Path(__file__).parent
    / 'badges.css')



class Badge:
    """
    Construct the badge image and output to the image file.
    """

    html: str


    def __init__(
        self,
        label: str,
        value: str,
        *,
        count: Optional[int | str] = None,
        color: Optional[Literal[BadgeColors]] = None,
        date: Optional[str] = None,
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        _value = (
            value
            .strip()
            .lower())

        if _value[:7] == 'unknown':
            _value = 'unknown'


        _count = (
            ''
            if count is None
            else count)


        _color = (
            'gray'
            if color is None
            else color)

        if color is None:

            if _value[-1] == '%':

                eulav = int(
                    float(_value[:-1]))

                if eulav == 100:
                    _color = 'green'

                elif eulav >= 80:
                    _color = 'yellow'

                elif eulav >= 0:
                    _color = 'red'

                _value = f'{eulav}%'

            if _value in _SUCCESS:
                _color = 'green'

            if _value in _FAILURE:
                _color = 'red'


        date = (
            (datetime
             .now(tz=timezone.utc)
             .strftime(_STAMP))
            if date is None
            else date)

        try:
            stamp = (
                parser.parse(date)
                .strftime(_STAMP))

        except ParserError:
            stamp = 'unknown'


        self.html = '\n'.join([
            '<style>',
            f'{_STYLES.read_text()}',
            '</style>',
            f'<table class="{_color}">',
            '  <tbody>',
            '    <tr>',
            f'      <td class="label">{label}</td>',
            f'      <td class="value">{_value}</td>',
            f'      <td class="count">{_count}</td>',
            f'      <td class="stamp">{stamp}</td>',
            '    </tr>',
            '  </tbody>',
            '</table>'])


    def write(
        self,
        output: str | Path,
    ) -> None:
        """
        Ouput badge to the complete or relative filesystem path.

        :param output: Where to write the generated badge image.
        """

        from wand.color import Color  # type: ignore[import-untyped]
        from wand.image import Image  # type: ignore[import-untyped]
        from weasyprint import HTML  # type: ignore[import-untyped]

        output = str(output)

        bytes = BytesIO()

        (HTML(string=self.html)
         .write_pdf(bytes))

        bytes.seek(0)

        origin = Image(
            file=bytes,
            resolution=300)

        with origin as image:

            image.trim(
                Color('transparent'))

            image.format = 'png'

            image.save(
                filename=output)
