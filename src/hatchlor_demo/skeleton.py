"""
This is a skeleton file that can serve as a starting point for a Python
console script. This is accomplished via the following lines in `pyproject.toml`:

```toml
[project.scripts]
fibonacci = "hatchlor_demo.skeleton:app"
```

Then run `hatch run fibonacci 10` to execute this in your default environment or
`hatch shell` to enter the default environment, followed by `fibonacci 10`.

Note:
    This file can be renamed depending on your needs or safely removed if not needed.

References:
    - https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""

import enum
import logging
import sys
from typing import Annotated

import typer

from hatchlor_demo import __version__

_logger = logging.getLogger(__name__)


class LogLevel(str, enum.Enum):
    CRITICAL = 'critical'
    ERROR = 'error'
    WARNING = 'warning'
    INFO = 'info'
    DEBUG = 'debug'


def fib(n: int) -> int:
    """Fibonacci example function"""
    if not n > 0:
        msg = f'{n} must be larger than 0!'
        raise RuntimeError(msg)
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a


def setup_logging(log_level: LogLevel):
    """Setup basic logging"""
    log_format = '[%(asctime)s] %(levelname)s:%(name)s:%(message)s'
    numeric_level = getattr(logging, log_level.upper(), None)
    logging.basicConfig(level=numeric_level, stream=sys.stdout, format=log_format, datefmt='%Y-%m-%d %H:%M:%S')


app = typer.Typer(
    name=f'Hatchlor demo project {__version__}',
    help='Python project featuring the Python project manager hatch powerd by the Hatchlor.',
)


@app.command()
def main(
    n: Annotated[int, typer.Argument(..., min=1, help='Positive integer')],
    log_level: Annotated[LogLevel, typer.Option(help='Log level')] = LogLevel.INFO,
):
    """Wrapper allowing :func:`fib` to be called with string arguments in a CLI fashion

    Instead of returning the value from :func:`fib`, it prints the result to the
    `stdout` in a nicely formatted message.
    """
    setup_logging(log_level)
    _logger.debug('Starting crazy calculations...')
    print(f'The {n}-th Fibonacci number is {fib(n)}')  # noqa: T201
    _logger.info('Script ends here')


if __name__ == '__main__':
    app()
